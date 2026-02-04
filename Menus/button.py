import pygame

class Button():
	def __init__(self, x, y, image):
		width = image.get_width()
		height = image.get_height()
		self.image = image
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.topleft = (self.x, self.y)

		self.clicked = False

	def draw(self, surface):
		"""Draws the button on a surface

		Args:
			surface (Surface): Surface to draw the button on

		"""
		surface.blit(self.image, (self.rect.x, self.rect.y))

		
	def pressed(self):
		"""Tell if button was pressed

		Returns:
			bool: True if button was pressed, False if not
		"""
		action = False
		#get mouse position
		mouse_position = pygame.mouse.get_pos()
		
		#check mouseover and clicked conditions
		if self.rect.collidepoint(mouse_position):
			
		
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == True:
				self.clicked = False
				action = False
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

			

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action