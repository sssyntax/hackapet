import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time
from adafruit_display_text import label
import random
#import terminalio

# init
pygame.init()
display = PyGameDisplay(width=128, height=128)
screen = displayio.Group()
display.show(screen)
tileW= 32
tileH = 32

#background
background = displayio.OnDiskBitmap("background.bmp")
displaybg = displayio.TileGrid(background, pixel_shader=background.pixel_shader)
screen.append(displaybg)

defaultbingus = displayio.OnDiskBitmap("closedbingus.bmp")
hungrybingus = displayio.OnDiskBitmap("openbingus.bmp")



# falling stuff (nuggies + carrots)
class Droppings:
    def __init__(self,image):
        self.image = image

    def spawn(self):
        xpos = random.randint(0, display.width - self.image.width)
        self.thing = displayio.TileGrid(
            self.image,
            pixel_shader=self.image.pixel_shader,
            width=1,
            height=1,
            tile_width=self.image.width,
            tile_height=self.image.height,
            x=xpos,
            y=-32
        )
        screen.append(self.thing)
        return self.thing


# check sprite collision
def check_collision(sprite1,sprite2):
    return (
        sprite1.y < sprite2.y + 16 and
        sprite1.y + 16 > sprite2.y and

        sprite1.x < sprite2.x + 16 and
        sprite1.x + 16 > sprite2.x
    )
    

dead = displayio.OnDiskBitmap("end.bmp")

def died():
    screen.append(deadDis)

    for i in nuggies:
        screen.remove(i)
    nuggies.clear()

    for i in carrots:
        screen.remove(i)
    carrots.clear()


# draw bingus
bingus = displayio.TileGrid(
    defaultbingus,
    pixel_shader=defaultbingus.pixel_shader,
    width=1,
    height=1,
    tile_width=tileH,
    tile_height=tileH,
    default_tile=0,
    x=(display.width - tileH) // 2,  
    y=display.height - tileH - 20     
)
screen.append(bingus)

# init dead screen
deadDis = displayio.TileGrid(
        dead,
        pixel_shader=defaultbingus.pixel_shader,
        width=1,
        height=1,
        default_tile=0,
        x=10,
        y=5
    )

# begin game
speed = 6
Game = True
bingusstate = True

score = 0 # terminalio doesnt work rn

nuggies = []
nugget = Droppings(displayio.OnDiskBitmap("nuggie.bmp"))

carrots = []
carrot = Droppings(displayio.OnDiskBitmap("carrot.bmp"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not Game:
                score = 0
                screen.remove(deadDis)
                Game = True


    keys = pygame.key.get_pressed()

    if Game:
        # move bingus
        if keys[pygame.K_LEFT]:
            bingus.x -= speed
        
        if keys[pygame.K_RIGHT]:
            bingus.x += speed
        
        # switch bingus state
        if keys[pygame.K_UP]:
            bingusstate = not bingusstate
            n_bingus = displayio.TileGrid(
                [hungrybingus,defaultbingus][bingusstate],
                pixel_shader=defaultbingus.pixel_shader,
                width=1,
                height=1,
                tile_width=tileW,
                tile_height=tileH,
                default_tile=0,
                x=bingus.x,  
                y=bingus.y     
            )
            screen[screen.index(bingus)] = n_bingus
            bingus = n_bingus

        # spawning nuggies and carrots
        if random.random() < 0.06:  
            nuggies.append(nugget.spawn())
            carrots.append(carrot.spawn())

    for nug in nuggies:
        nug.y += 8
        if nug.y > display.height:
            screen.remove(nug)
            nuggies.remove(nug)

        if not bingusstate:
            if check_collision(bingus,nug):
                score += 1
                screen.remove(nug)
                nuggies.remove(nug)

    for carr in carrots:
        carr.y += 5 
        if carr.y > display.height:
            screen.remove(carr)
            carrots.remove(carr)

        if not bingusstate:
            if check_collision(bingus,carr):
                Game = False
                died()

    #scoreshow= label.Label(terminalio.FONT, scale=1, text=f"Score: {score}", color=0xFFFFFF) # terminalio doesnt work rn
    #screen.append(scoreshow) # terminalio doesnt work rn

    time.sleep(0.1)