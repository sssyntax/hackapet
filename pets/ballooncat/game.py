import pygame
import os
import random
import sys

pygame.init()

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 128
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ascending Balloons")

clock = pygame.time.Clock()

def load_image(path, size=None):
    try:
        image = pygame.image.load(path).convert_alpha()
        if size:
            image = pygame.transform.scale(image, size)
        return image
    except pygame.error as e: 
        print(f"Unable to load image at path: {path}")
        raise SystemExit(e)

backgrounds = [
    load_image("assets/backgrounds/start_ground.png", (SCREEN_WIDTH, SCREEN_HEIGHT)),      # 0: Start Screen Background
    load_image("assets/backgrounds/start_no_text.png", (SCREEN_WIDTH, SCREEN_HEIGHT)),    # 1: Game Over Background (Unused)
    load_image("assets/backgrounds/sky1.png", (SCREEN_WIDTH, SCREEN_HEIGHT)),              # 2: Playing Background 1
    load_image("assets/backgrounds/sky2.png", (SCREEN_WIDTH, SCREEN_HEIGHT)),              # 3: Playing Background 2
    load_image("assets/backgrounds/sky3.png", (SCREEN_WIDTH, SCREEN_HEIGHT)),              # 4: Playing Background 3
]

cat_frames = {
    "no_balloons": load_image("assets/cat/cat_no_balloons.png", (32, 32)),
    "3_balloons": load_image("assets/cat/cat_3_balloons.png", (32, 32)),
    "3_balloons_pop": load_image("assets/cat/cat_3_balloons_pop.png", (32, 32)),
    "2_balloons": load_image("assets/cat/cat_2_balloons.png", (32, 32)),
    "2_balloons_pop": load_image("assets/cat/cat_2_balloons_pop.png", (32, 32)),
    "1_balloon": load_image("assets/cat/cat_1_balloon.png", (32, 32)),
    "1_balloon_pop": load_image("assets/cat/cat_1_balloon_pop.png", (32, 32)),
}

bird_frames = [
    load_image("assets/birds/bird1.png", (18, 18)),
    load_image("assets/birds/bird2.png", (18, 18)),
]

font = pygame.font.SysFont("Arial", 8)

HIGH_SCORE_FILE = "high_score.txt"

def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            try:
                return int(file.read())
            except:
                return 0
    return 0

def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))

START = "start"
PLAYING = "playing"

current_state = START

score = 0
high_score = load_high_score()
start_ticks = 0

background_switch_time = 5000 
last_background_switch = pygame.time.get_ticks()
current_background_index = 2  

bird_speed = 1.0  
speed_increase_interval = 10000  
last_speed_increase = pygame.time.get_ticks()
speed_increment = 0.1  
max_bird_speed = 5.0  

class Cat(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.balloon_count = 3
        self.current_frame = "3_balloons"
        self.image = cat_frames[self.current_frame]
        self.rect = self.image.get_rect(center=pos)
        self.speed_x = 5
        self.popping = False
        self.pop_duration = 250
        self.pop_start_time = 0

    def update_sprite(self):
        if self.balloon_count == 3:
            self.current_frame = "3_balloons"
        elif self.balloon_count == 2:
            self.current_frame = "2_balloons_pop"
        elif self.balloon_count == 1:
            self.current_frame = "1_balloon_pop"
        else:
            self.current_frame = "no_balloons"
        self.image = cat_frames[self.current_frame]

    def lose_balloon(self):
        if self.balloon_count > 0 and not self.popping:
            self.popping = True
            self.pop_start_time = pygame.time.get_ticks()
            if self.balloon_count == 1:
                pop_frame = "1_balloon_pop"
            else:
                pop_frame = f"{self.balloon_count}_balloons_pop"
            self.current_frame = pop_frame
            self.image = cat_frames[self.current_frame]
            self.balloon_count -= 1

    def update(self):
        if self.popping:
            current_time = pygame.time.get_ticks()
            if current_time - self.pop_start_time >= self.pop_duration:
                self.popping = False
                if self.balloon_count > 0:
                    if self.balloon_count == 1:
                        normal_frame = "1_balloon"
                    else:
                        normal_frame = f"{self.balloon_count}_balloons"
                    self.current_frame = normal_frame
                else:
                    self.current_frame = "no_balloons"
                self.image = cat_frames[self.current_frame]

    def move_left(self):
        self.rect.x -= self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += self.speed_x
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_y):
        super().__init__()
        self.images = bird_frames
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_y = speed_y
        self.animation_time = 300 
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_time:
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]
            self.last_update = now

all_sprites = pygame.sprite.Group()
bird_sprites = pygame.sprite.Group()
cat_sprite = None

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))

def start_screen():
    screen.blit(backgrounds[0], (0, 0)) 
    global cat_sprite
    cat_sprite = Cat(pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))
    all_sprites.add(cat_sprite)
    all_sprites.draw(screen)
    draw_text("Press Space to Start", font, WHITE, screen, 30, 60)
    draw_text(f"High Score: {high_score}", font, WHITE, screen, 35, 80)
    pygame.display.flip()

def playing_state():
    global score, last_background_switch, current_background_index
    score = (pygame.time.get_ticks() - start_ticks) // 1000
    now = pygame.time.get_ticks()
    if now - last_background_switch > background_switch_time:
        current_background_index = 2 + (current_background_index - 2 + 1) % 3
        last_background_switch = now
    screen.blit(backgrounds[current_background_index], (0, 0))
    all_sprites.draw(screen)
    draw_text(f"Score: {score}", font, WHITE, screen, 5, 5)
    pygame.display.flip()

start_screen()

def spawn_bird():
    if len(bird_sprites) < 10:  
        x = random.randint(20, SCREEN_WIDTH - 38)
        y = -random.randint(10, 30)
        bird = Bird(x, y, bird_speed)
        all_sprites.add(bird)
        bird_sprites.add(bird)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if current_state == START:
                    current_state = PLAYING
                    all_sprites.empty()
                    bird_sprites.empty()
                    cat_sprite = Cat(pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))
                    all_sprites.add(cat_sprite)
                    for _ in range(5):
                        spawn_bird()
                    start_ticks = pygame.time.get_ticks()
                    last_background_switch = pygame.time.get_ticks()
                    current_background_index = 2
                    playing_state()
                elif current_state == PLAYING:
                    pass

    keys = pygame.key.get_pressed()
    if current_state == PLAYING:
        if keys[pygame.K_a]:
            cat_sprite.move_left()
        if keys[pygame.K_d]:
            cat_sprite.move_right()

        now = pygame.time.get_ticks()
        if now - last_speed_increase > speed_increase_interval:
            if bird_speed < max_bird_speed:
                bird_speed += speed_increment
            last_speed_increase = now

        if random.randint(1, 100) <= 1:
            spawn_bird()

        all_sprites.update()

        hits = pygame.sprite.spritecollide(cat_sprite, bird_sprites, True)
        if hits and not cat_sprite.popping:
            cat_sprite.lose_balloon()
            if cat_sprite.balloon_count == 0:
                if score > high_score:
                    high_score = score
                    save_high_score(score)

        if cat_sprite.balloon_count == 0 and not cat_sprite.popping:
            current_state = START
            all_sprites.empty()
            bird_sprites.empty()
            start_screen()

        playing_state()


    elif current_state == START:
        screen.blit(backgrounds[0], (0, 0))  
        all_sprites.empty()
        cat_sprite = Cat(pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))
        all_sprites.add(cat_sprite)
        all_sprites.draw(screen)
        draw_text("Space to Start", font, WHITE, screen, 30, 60)
        draw_text(f"High Score: {high_score}", font, WHITE, screen, 35, 80)
        pygame.display.flip()

pygame.quit()
