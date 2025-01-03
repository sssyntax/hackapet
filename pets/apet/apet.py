import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time

pygame.init()

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

forest_background = displayio.OnDiskBitmap("forestbackground.bmp")
bg_sprite = displayio.TileGrid(forest_background, pixel_shader=forest_background.pixel_shader)
splash.append(bg_sprite)

cat_sheet = displayio.OnDiskBitmap("cat-Sheet.bmp") #note this isn't actually a bmp file - bmp files don't allow for transparent backgrounds so will need to be edited on actual hackapet circuitpython code

tile_width = 32
tile_height = 32

cat_sprite = displayio.TileGrid(
    cat_sheet,
    pixel_shader=cat_sheet.pixel_shader,
    width=1,
    height=1,
    tile_width=tile_width,
    tile_height=tile_height,
    default_tile=0,
    x=(display.width - tile_width) // 2,  
    y=display.height - tile_height       
)

splash.append(cat_sprite)

frame = 0
speed = 2  

# gameloop

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat_sprite.x -= speed
            elif event.key == pygame.K_RIGHT:
                cat_sprite.x += speed

    cat_sprite[0] = frame
    frame = (frame + 1) % (cat_sheet.width // tile_width)

    time.sleep(0.1)