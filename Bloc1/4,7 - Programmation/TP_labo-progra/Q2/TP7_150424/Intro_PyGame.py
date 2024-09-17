import pygame
pygame.init()

resolution = (800, 600)
surface = pygame.display.set_mode(resolution)

pygame.display.set_icon(pygame.image.load("logo.webp"))
pygame.display.set_caption("My first Pygame window")

surface.fill((200, 200, 255))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
