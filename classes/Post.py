import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, descprition ,user_name,location): #TODO: add parameters
        self.descprition = descprition
        self.user_name = user_name
        self.location = location
        self.comments = []
        self.like_counter = 0
        self.comments_display_index = 0

    def add_like(self):
        self.like_counter+=1

    def add_comment(self,text):

        self.comments.append(text)




    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        # TODO: write me!
        font =pygame.font.SysFont('chalkduster.ttf',UI_FONT_SIZE )

        username= font.render(self.user_name,True,BLACK)
        screen.blit(username,(LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS))

        location = font.render(self.location,True,BLACK)
        screen.blit(location,(DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS))

        like_count = font.render(str(self.like_counter),True,BLACK)
        screen.blit(like_count,(LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS))

        describtion = font.render(self.descprition, True, BLACK)
        screen.blit(describtion, (USER_NAME_X_POS, USER_NAME_Y_POS))



    def display_comments(self,comments):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break
