import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time

pygame.init()
display = PyGameDisplay(width=128,height=128)
splash = displayio.Group()
display.show(splash)

currentbg = 0
backgrounds = [displayio.OnDiskBitmap("assets/winterforest.bmp"), displayio.OnDiskBitmap("assets/springforest.bmp"),displayio.OnDiskBitmap("assets/summerforest.bmp"),displayio.OnDiskBitmap("assets/fallforest.bmp")]
bg = displayio.OnDiskBitmap("assets/winterforest.bmp")
bgs = displayio.TileGrid(
    bg,
    pixel_shader=bg.pixel_shader
)
splash.append(bgs)

dog = displayio.OnDiskBitmap("assets/blizzard.bmp")
blizzard_sprite = displayio.TileGrid(
    dog,
    pixel_shader=dog.pixel_shader,
    width=1,
    height=1,
    tile_height=96,
    tile_width=96,
    default_tile=0,
    x=(display.width - 96) // 2,
    y=display.height - 96 - 10
)
splash.append(blizzard_sprite)

eat = displayio.OnDiskBitmap("assets/eat.bmp")
drink = displayio.OnDiskBitmap("assets/drink.bmp")
action = displayio.TileGrid(
    eat,
    pixel_shader=eat.pixel_shader,
    x=(display.width - 96) // 2,
    y=display.height - 96 - 10
)
splash.append(action)

lowH = displayio.OnDiskBitmap("assets/lowHunger.bmp")
lowT = displayio.OnDiskBitmap("assets/lowThirst.bmp")
warning = displayio.TileGrid(
    lowH,
    pixel_shader=lowH.pixel_shader,
    x=(display.width - 96) // 2,
)
splash.append(warning)

hunger = 22.5
thirst = 35.0

frame = 0
ticks = 0

while True:
    ticks += 1

    if ticks >= 120:
        ticks = 0
        currentbg = (currentbg + 1) % 4
        bgs.bitmap = backgrounds[currentbg]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        blizzard_sprite.hidden = True
        action.hidden = False
        action.bitmap = eat
        hunger += 15
        time.sleep(1)
        blizzard_sprite.hidden = False
        action.hidden = True
    elif keys[pygame.K_LEFT]:
        blizzard_sprite.hidden = True
        action.hidden = False
        action.bitmap = drink
        thirst += 20
        time.sleep(1)
        blizzard_sprite.hidden = False
        action.hidden = True
    else:
        action.hidden = True

    blizzard_sprite[0] = frame
    frame = (frame + 1) % 4

    if hunger <= 20:
        warning.bitmap = lowH
        warning.hidden = False
        blizzard_sprite[0] = 4
    elif thirst <= 20:
        warning.bitmap = lowT
        warning.hidden = False
    else:
        warning.hidden = True
    
    time.sleep(0.25)

    hunger -= .15
    thirst -= .25

    if hunger <= 0: hunger = 0
    if thirst <= 0: thirst = 0
    if hunger >= 100: hunger = 100
    if thirst >= 100: thirst = 100
    print(hunger,thirst)
