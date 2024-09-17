import pygame
import random

# Définition des constantes pour la fenêtre
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 500
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
MOUNTAIN = pygame.image.load("TD1/mountain.png")

global_score = 0
# Initialisation de Pygame
pygame.init()


class BackgroundMoving(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("TD1/cailloux.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        # Dupliquer l'image pour un mouvement continu
        self.second_image = pygame.image.load("TD1/cailloux.png")
        self.second_rect = self.second_image.get_rect()
        self.second_rect.x = 1500
        self.second_rect.y = 0

        self.speed = 2

    def update(self):
        # Déplacer les deux images simultanément
        self.rect = self.rect.move(-self.speed, 0)
        self.second_rect = self.second_rect.move(-self.speed, 0)

        # Si la première image sort de l'écran, la remettre à droite de la deuxième image
        if (self.rect.x) <= -1501:
            self.rect.x = 1500

        # Si la deuxième image sort de l'écran, la remettre à droite de la première image
        if (self.second_rect.x) <= -1501:
            self.second_rect.x = 1500


# Classe représentant le joueur
class Player(pygame.sprite.Sprite):
    sprites = (
        pygame.image.load("TD1/bird_01.png"),
        pygame.image.load("TD1/bird_02.png"),
        pygame.image.load("TD1/bird_03.png"),
        pygame.image.load("TD1/bird_04.png"),
        pygame.image.load("TD1/bird_05.png"),
        pygame.image.load("TD1/bird_06.png")
    )

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 2)

    def update_image(self):
        self.image = self.sprites[pygame.time.get_ticks() // 100 % 6]

    def update(self, pressed_key):
        if pressed_key[pygame.K_UP]:
            self.rect.y -= 5
        if pressed_key[pygame.K_DOWN]:
            self.rect.y += 5
        if pressed_key[pygame.K_LEFT]:
            self.rect.x -= 5
        if pressed_key[pygame.K_RIGHT]:
            self.rect.x += 5
        self.update_image()

        # Assurer que le joueur ne sorte pas de l'écran
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))


# Classe représentant l'ennemi
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("TD1/fireball.png")
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed = random.randint(5, 10)

    def update(self):
        global global_score
        self.rect.x -= self.speed
        # Détruire l'objet une fois complètement sorti de la zone de jeu
        if self.rect.right < 0:
            if not global_score > 0:
                global_score = 0
            global_score += 1
            self.kill()


# Initialisation de la fenêtre de jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Avoid the Enemies")

# Création des groupes de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

background = BackgroundMoving()
all_sprites.add(background)


# Création du joueur
player = Player()
all_sprites.add(player)


# Variables pour le score et le texte du score
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

# Boucle principale du jeu
while running:
    screen.fill(WHITE)
    screen.blit(MOUNTAIN, (0, 0))

    pressed_keys = pygame.key.get_pressed()

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Création d'un nouvel ennemi à intervalles aléatoires
    if random.randint(0, 250) < 5:
        new_enemy = Enemy()
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)

    # Mise à jour du joueur
    player.update(pressed_keys)

    # Vérification des collisions entre le joueur et les ennemis
    collisions = pygame.sprite.spritecollide(player, enemies, True)
    if collisions:
        # Réinitialiser le score si le joueur est touché par un ennemi
        print(f"Highscore: {global_score}")
        global_score = 0

    # Mise à jour des ennemis
    for enemy in enemies:
        enemy.update()

    # Mise à jour de l'arrière-plan
    background.update()

    # Affichage du score
    score_text = font.render("Score: " + str(global_score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Affichage des sprites
    all_sprites.draw(screen)

    # Rafraîchissement de l'affichage
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
