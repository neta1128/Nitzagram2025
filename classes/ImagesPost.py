import pygame
from constants import *
from helpers import screen
from Post import Post


class ImagePost(Post):
    def __int__(self,username,location,description,image_path):
        super().__int__(username,location,description)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scala(self.image,(POST_WIDTH , POST_HEIGHT))



    def display(self):
        screen.blit(self.image,(POST_X_POS , POST_Y_POS))
        super().display()