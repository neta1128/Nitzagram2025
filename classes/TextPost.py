import pygame

from constants import *
from helpers import screen, from_text_to_array, center_text
from classes.Post import Post


class TextPost(Post):
    def __init__(self, username, location, description, text, text_color, background_color):
        super()._init_(username, location, description)
        self.text_array = from_text_to_array(text)
        self.text_color = text_color
        self.background_color = background_color

    def display(self):

        pygame.draw.rect(screen, self.background_color, pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))

        font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE, bold=False)

        for index, line in enumerate(self.text_array):
            rendered_text = font.render(line, True, self.text_color)
            text_position = center_text(len(self.text_array), rendered_text, index)
            screen.blit(rendered_text, text_position)

        super().display()