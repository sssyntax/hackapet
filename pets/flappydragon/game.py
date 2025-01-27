import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time
import random

pygame.init()

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

DRAGON_WIDTH = 32
DRAGON_HEIGHT = 32

PET_SPEED = DRAGON_HEIGHT
BIRDPLANE_SPEED = 4
GRAVITY = 4

frame = 0
game_over = False

sky_background = displayio.OnDiskBitmap("sky-background.bmp")
bg = displayio.TileGrid(
    sky_background, 
    pixel_shader=sky_background.pixel_shader
)
splash.append(bg)

dragon_sheet = displayio.OnDiskBitmap("dragon-sheet.bmp")
dragon = displayio.TileGrid(
    dragon_sheet,
    pixel_shader=dragon_sheet.pixel_shader,
    width=1,
    height=1,
    tile_width=DRAGON_WIDTH,
    tile_height=DRAGON_HEIGHT,
    default_tile=0,
    x=(display.width - dragon_sheet.width) // 2,  
    y=display.height - dragon_sheet.height
)
splash.append(dragon)

birdplane_bitmap = displayio.OnDiskBitmap("birdplane.bmp")
birdplane = displayio.TileGrid(
    birdplane_bitmap,
    pixel_shader=birdplane_bitmap.pixel_shader,
    width=1,
    height=1,
    tile_width=birdplane_bitmap.width,
    tile_height=birdplane_bitmap.height,
)
splash.append(birdplane)

restart_bitmap = displayio.OnDiskBitmap("restart.bmp")
restart = displayio.TileGrid(
    restart_bitmap,
    pixel_shader=restart_bitmap.pixel_shader,
    width=1,
    height=1,
    tile_width=64,
    tile_height=32,
    default_tile=0,
    x=(display.width - 64) // 2,  
    y=(display.height - 32) // 2  
)

def spawn_birdplane():
    birdplane.x = display.width
    birdplane.y = random.randint(0, (display.height // birdplane_bitmap.height) - 1) * birdplane_bitmap.height
    
def check_collision(sprite1, sprite2, w1=32, h1=32, w2=32, h2=32):
    return (
        sprite1.x < sprite2.x + w1 and
        sprite1.x + w2 > sprite2.x and
        sprite1.y < sprite2.y + h1 and
        sprite1.y + h2 > sprite2.y
    )

spawn_birdplane()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and game_over == True:
                splash.remove(restart)
                game_over = False
                dragon.y = display.height - DRAGON_HEIGHT
                spawn_birdplane()

    if game_over: continue

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        dragon.y = dragon.y - PET_SPEED if dragon.y - PET_SPEED > 0 else 0

    birdplane.x -= 5

    dragon.y += GRAVITY if dragon.y < display.height else 0

    if birdplane.x <= -birdplane_bitmap.width:
        spawn_birdplane()
    elif check_collision(dragon, birdplane, w1=64):
        game_over = True
        splash.append(restart)

    dragon[0] = frame
    frame = (frame + 1) % (dragon_sheet.width // DRAGON_WIDTH)

    time.sleep(0.1)
