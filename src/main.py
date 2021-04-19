import pygame
from pygame.locals import *
import quantum

pygame.init()

QUBE_UNITY = 32
NUMBER_COLUMN = 20
NUMBER_ROW = 10
HEIGHT = NUMBER_ROW * QUBE_UNITY
WIDTH = NUMBER_COLUMN * QUBE_UNITY
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Qube")

def prepare_sprite(file_name):
    return pygame.transform.scale(pygame.image.load(f"sprites/{file_name}").convert_alpha(), (QUBE_UNITY, QUBE_UNITY))

sky_image = prepare_sprite("sky.gif")

floor_image = prepare_sprite("floor.gif")

generated = quantum.generate_floor_v3(10, [0, 0, 1, 1, 1, 1, 1, 1, 1, 1])

def to_pygame(y, height = HEIGHT, obj_height = QUBE_UNITY):
    return (height - y - obj_height)

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        x *= QUBE_UNITY
        y *= QUBE_UNITY
        y = to_pygame(y)
        super().__init__()
        self.surf = pygame.Surface((QUBE_UNITY, QUBE_UNITY))
        self.surf = floor_image
        self.rect = self.surf.get_rect(topleft = (x, y))

    def move(self):
        self.rect.x -= 1

class Sky(pygame.sprite.Sprite):
    def __init__(self, x, y):
        x *= QUBE_UNITY
        y *= QUBE_UNITY
        y = to_pygame(y)
        super().__init__()
        self.surf = pygame.Surface((QUBE_UNITY, QUBE_UNITY))
        self.surf = sky_image
        self.rect = self.surf.get_rect(topleft = (x, y))


    def move(self):
        self.rect.x -= 1

all_sprites = pygame.sprite.Group()
for i, ii in enumerate(generated):
    for j, jj in enumerate(reversed(ii)):
        if jj == 1:
            all_sprites.add(Floor(i, j))
        if jj == 0:
            all_sprites.add(Sky(i, j))

move = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move = QUBE_UNITY
                wait = FPS


    displaysurface.fill((0,0,0))

    for entity in all_sprites:
        if move > 0:
            if wait > 0:
                wait -= 1
            else:
                wait = FPS
                for s in all_sprites:
                    s.move()
                move -= 1
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
