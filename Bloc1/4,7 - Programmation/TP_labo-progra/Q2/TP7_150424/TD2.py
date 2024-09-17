import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Définition des dimensions de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Classe représentant le serpent
class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 50]]
        self.radius = 10
        self.dx = 5  # vitesse de déplacement horizontale
        self.dy = 0  # vitesse de déplacement verticale

    # Méthode pour dessiner le serpent sur l'écran
    def draw(self, surface):
        for element in self.elements:
            pygame.draw.circle(surface, WHITE, element, self.radius)

    # Méthode pour déplacer le serpent
    def move(self):
        if self.size > 1:
            for i in range(self.size - 1, 0, -1):
                self.elements[i] = list(self.elements[i - 1])
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    # Méthode pour vérifier les collisions avec les bords de l'écran
    def check_boundaries(self):
        if self.elements[0][0] > SCREEN_WIDTH or self.elements[0][0] < 0:
            return True
        if self.elements[0][1] > SCREEN_HEIGHT or self.elements[0][1] < 0:
            return True
        return False

    # Méthode pour vérifier les collisions avec le corps du serpent
    def check_self_collision(self):
        for i in range(1, self.size):
            if self.elements[0] == self.elements[i]:
                return True
        return False

    # Méthode pour faire grandir le serpent
    def grow(self):
        self.size += 1
        self.elements.append([0, 0])


# Classe représentant la pomme
class Apple:
    def __init__(self):
        self.position = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
                         random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        self.radius = 10

    # Méthode pour dessiner la pomme sur l'écran
    def draw(self, surface):
        pygame.draw.circle(surface, RED, self.position, self.radius)


# Fonction principale
def main():
    # Création de la fenêtre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Initialisation du serpent et de la pomme
    snake = Snake()
    apple = Apple()

    # Boucle principale du jeu
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.dy == 0:
                    snake.dx = 0
                    snake.dy = -5
                elif event.key == pygame.K_DOWN and snake.dy == 0:
                    snake.dx = 0
                    snake.dy = 5
                elif event.key == pygame.K_LEFT and snake.dx == 0:
                    snake.dx = -5
                    snake.dy = 0
                elif event.key == pygame.K_RIGHT and snake.dx == 0:
                    snake.dx = 5
                    snake.dy = 0

        # Effacement de l'écran
        screen.fill(BLACK)

        # Déplacement et dessin du serpent et de la pomme
        snake.move()
        snake.draw(screen)
        apple.draw(screen)

        # Vérification des collisions
        if snake.check_boundaries() or snake.check_self_collision():
            running = False
        if snake.elements[0] == apple.position:
            snake.grow()
            apple = Apple()

        # Rafraîchissement de l'écran
        pygame.display.flip()
        pygame.time.Clock().tick(20)

    # Quitter Pygame
    pygame.quit()


# Appel de la fonction principale
if __name__ == "__main__":
    main()
