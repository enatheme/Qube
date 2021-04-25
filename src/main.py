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

generated = quantum.generate_floor_v2(10, [0, 0, 1, 1, 1, 1, 1, 1, 1, 1])

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

def display_column(column_number, column):
    for j, jj in enumerate(reversed(column)):
        if jj == 1:
            all_sprites.add(Floor(column_number, j))
        if jj == 0:
            all_sprites.add(Sky(column_number, j))

for i, ii in enumerate(generated):
    display_column(i, ii)

move = 0
columns_ready = 10
generated = quantum.generate_floor_v2(10, generated[9])

display_new_column = False
automatic_scrolling = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move = QUBE_UNITY
                display_new_column = True
            if event.key == pygame.K_u:
                if automatic_scrolling:
                    automatic_scrolling = False
                else:
                    automatic_scrolling = True
    if automatic_scrolling:
        if move == 0:
            move = QUBE_UNITY
            display_new_column = True

    displaysurface.fill((0,0,0))

    if display_new_column:
        if move == 0 or move == QUBE_UNITY:
            display_new_column = False
            display_column(20, generated[columns_ready - 9])
            columns_ready -= 1
            if columns_ready <= 0:
                columns_ready = 10
                generated = quantum.generate_floor_v2(10, generated[9])
                print("generating new columns")

    if move > 0:
        move -= 1
        for s in all_sprites:
            s.move()

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
