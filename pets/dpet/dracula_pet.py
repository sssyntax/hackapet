import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time
import random
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

pygame.init()

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

forest_background = displayio.OnDiskBitmap("desert.bmp")
bg_sprite = displayio.TileGrid(forest_background, pixel_shader=forest_background.pixel_shader)
splash.append(bg_sprite)


def display_found_it():
    yellow_background = displayio.Bitmap(display.width, display.height, 1)
    yellow_palette = displayio.Palette(1)
    yellow_palette[0] = 0xFFFF00
    yellow_bg_sprite = displayio.TileGrid(yellow_background, pixel_shader=yellow_palette)
    splash.append(yellow_bg_sprite)
    font = bitmap_font.load_font("./helvR12.bdf")
    text_area = label.Label(font, text="YOU FOUND IT!", color=0x000000, x=(display.width - 100) // 2,
                            y=(display.height - 10))
    splash.append(text_area)
    game_over_image = displayio.OnDiskBitmap("restart.bmp")
    game_over_sprite = displayio.TileGrid(
        game_over_image,
                pixel_shader=game_over_image.pixel_shader
                )
    splash.append(game_over_sprite)
    global game_over
    game_over = True


cat_sheet = displayio.OnDiskBitmap("doggy.bmp")
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
    y=display.height - tile_height - 10
)
splash.append(cat_sprite)

grid_step = 4


def get_random_treasure_position():
    x = random.randint(0, (display.width - tile_width) // grid_step) * grid_step
    possible_y_values = list(range(-2, 99, grid_step))
    y = random.choice(possible_y_values)
    return x, y


restart_ready = False
game_over_time = 0  # To track when the game over happened

def reset_game():
    global cat_sprite, treasure_x, treasure_y, fireballs, game_over, frame, restart_ready
    # Reset sprite positions
    cat_sprite.x = (display.width - tile_width) // 2
    cat_sprite.y = display.height - tile_height - 10
    treasure_x, treasure_y = get_random_treasure_position()
    fireballs = []
    game_over = False
    frame = 0
    restart_ready = False  # Reset the restart flag

    # Clear all sprites from the group
    while len(splash) > 0:
        splash.pop()

    # Re-add the background and cat sprite
    splash.append(bg_sprite)
    splash.append(cat_sprite)


treasure_x, treasure_y = get_random_treasure_position()

fireball_bitmap = displayio.OnDiskBitmap("fireball.bmp")
fireballs = []


def spawn_fireball():
    x_position = random.randint(0, display.width - tile_width)
    fireball = displayio.TileGrid(
        fireball_bitmap,
        pixel_shader=fireball_bitmap.pixel_shader,
        width=1,
        height=1,
        tile_width=tile_width,
        tile_height=tile_height,
        x=x_position,
        y=-tile_height
    )
    fireballs.append(fireball)
    splash.append(fireball)


def get_proximity():
    distance_x = abs(cat_sprite.x - treasure_x)
    distance_y = abs(cat_sprite.y - treasure_y)
    distance = distance_x + distance_y

    if distance == 0:
        return "YOU FOUND IT!"
    elif distance <= 10:
        return "HOT!"
    elif distance <= 30:
        return "WARM!"
    else:
        return "COLD!"


def display_proximity_message(message):
    for sprite in splash:
        if isinstance(sprite, label.Label):
            splash.remove(sprite)
    font = bitmap_font.load_font("./helvR12.bdf")
    text_area = label.Label(font, text=message, color=0x000000, x=display.width - 5 - len(message) * 8,
                            y=display.height - 20)
    splash.append(text_area)


frame = 0
speed = 4
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_LEFT] and cat_sprite.x > 0:
            cat_sprite.x -= speed
        if keys[pygame.K_RIGHT] and cat_sprite.x < display.width - tile_width:
            cat_sprite.x += speed
        if keys[pygame.K_UP] and cat_sprite.y > 0:
            cat_sprite.y -= speed
        if keys[pygame.K_DOWN] and cat_sprite.y < display.height - tile_height:
            cat_sprite.y += speed

        message = get_proximity()
        display_proximity_message(message)

        if cat_sprite.x == treasure_x and cat_sprite.y == treasure_y:
            display_found_it()

        if random.random() < 0.02:
            spawn_fireball()

        for fireball in fireballs[:]:
            fireball.y += 4

            if fireball.y > display.height:
                splash.remove(fireball)
                fireballs.remove(fireball)
            elif cat_sprite.x < fireball.x + tile_width and cat_sprite.x + tile_width > fireball.x and cat_sprite.y < fireball.y + tile_height and cat_sprite.y + tile_height > fireball.y:
                game_over = True
                game_over_time = time.time()  # Record the time when the game ended
                display_proximity_message("GAME OVER!")
                game_over_image = displayio.OnDiskBitmap("restart.bmp")
                game_over_sprite = displayio.TileGrid(
                    game_over_image,
                    pixel_shader=game_over_image.pixel_shader
                )
                splash.append(game_over_sprite)

    else:  # Game is over, check for restart
        if not restart_ready and time.time() - game_over_time >= 1.5:
            restart_ready = True  # Enable restart after 1 second

        if restart_ready and keys[pygame.K_UP]:
            reset_game()

    cat_sprite[0] = frame
    frame = (frame + 1) % (cat_sheet.width // tile_width)

    time.sleep(0.1)