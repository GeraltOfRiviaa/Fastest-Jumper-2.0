import pygame
from os.path import join
class Button():
	def __init__(self, x, y, image,game):
		self.game = game
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
		#if self.rect.collidepoint(mouse_position):
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
		
	def load_image(self, width, height, name ,  position_x, position_y ,scale, *directory, ):
		"""Loads an image

		Args:
			size (int): size of each block
			name (string): name of the file
			position_x (int, optional): x position of the block on the sheet.
			position_y (int, optional): y position of the block on the sheet.
			*directory (tuple): directorys used to access the image

		Returns:
			Surface()
		"""

		path = join("assets", *directory, name)
		image = pygame.image.load(path).convert_alpha()
		surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
		rect = pygame.Rect(position_x, position_y, width, height)
		surface.blit(image, (0,0), rect)

		if scale:
			return pygame.transform.scale(surface, (width * scale, height * scale))
		else:
			return surface