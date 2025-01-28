import random
from . import spriteHandler 
import config
import math


class UFO:
   def __init__(self, group):
      self.sprite, self.frames = spriteHandler.load_sprite_sheet("./assets/ufo.bmp", 16, 16)
      self.sprite.x = -32
      self.sprite.y = 30
      self.speed = random.uniform(3, 7)
      self.wave_amplitude = random.randint(10, 30) 
      self.wave_freq = random.uniform(1.0, 2.0)     
      self.time = 0
      self.group = group
      self.group.append(self.sprite)
      self.isReset = False

   def update(self):
       self.time += 1 / config.LOCK_FPS
       self.sprite.x = int(self.sprite.x + self.speed)  # Convert to int
       self.sprite.y = int(30 + math.sin(self.time * self.wave_freq) * self.wave_amplitude) 
       if self.sprite.x > 160:
           self.reset()
           
   def reset(self):
       self.group.remove(self.sprite)
       self.isReset = True

