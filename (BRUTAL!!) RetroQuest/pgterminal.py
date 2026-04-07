import pygame
import time

class interfaceButton:
    def __init__(self, posx, posy, largura, altura, text, color):

        self.rect = pygame.Rect(posx, posy, largura, altura)
        self.text = text
        self.color = color
        self.overcolor = (255, 0, 0)

    def drawbutton(self, screen):

        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            actual_color = self.overcolor
        else:
            actual_color = self.color

        pygame.draw.rect(screen, actual_color, self.rect)

    def buttonclicked(self):

        mouse = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True

            return False



pygame.init()
screen = pygame.display.set_mode((900,600))
displaygamename = pygame.display.set_caption("KIMERAHALLA")
displaygameimage = pygame.image.load("Images/placeholder01.jpeg")
gamefont = pygame.font.SysFont(None, 40)
pygame.display.set_icon(displaygameimage)
clock = pygame.time.Clock()
runninggame=True

butaoteste = interfaceButton(200, 200, 250, 250, "OI", (0, 255, 0))

while runninggame:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runninggame = False

        if butaoteste.buttonclicked():
            print("ISSO FOI UM CLIQUE ÚNICO!")
    
    mouse_pos = pygame.mouse.get_pos()

    screen.fill((0,0,0))

    butaoteste.drawbutton(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()