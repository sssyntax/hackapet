import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
import random

pygame.init()
display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

background = displayio.OnDiskBitmap("bgl.bmp")

bg_sprite = displayio.TileGrid(
	background, 
	pixel_shader=background.pixel_shader
)


# add the ferris sprite here:
ferris_sheet = displayio.OnDiskBitmap("ferris-sheet.bmp")

ferris_sprite = displayio.TileGrid(
	ferris_sheet,
	pixel_shader=ferris_sheet.pixel_shader,
	width=1,
	height=1,
	tile_width=64,
	tile_height=64,
	default_tile=0,
	x=(display.width - 64) // 2,
	y=display.height - 64 - 10
)
ferris_sprite[0] = 3

frame = 0
dialoge = 1
question = None

ferris_dialoge = [
	"Hello,\nI'm Ferris!",
	("I usually live\nin a terminal", 1),
	"But right now\nIm on vacation!",
	"The problem is\nall the users",
	"keep aksing me\nto debug code",
	"So I cant\nrelax at all!",
	("...", 0),
	("Say, do you\nknow Rust?", 3),
	"You can learn\non the job!",
	"What job?",
	"You're going to\ndebug for me!",
	("It's pretty\nsimple...", 1),
	("Just choose\nthe correct answer!",2),
	"Well, actually\nthe incorrect one",
	"We are looking\nfor bugs after all!",
	"Ooh, perfect\ntiming!",
	("File Incoming\n",	0),
	0,
	1,
	2,
	3,
	("Well, it looks\nlike you've got it!", 2),
	("I'll be over here\n taking a nap", 1),
	"Keep up the good\nwork!",
	"I'll be over here\n taking a nap",
	("zzz...", 0),
	4,
]

questions = [
	{
		"options": ["print(a)", "print!(a)"],
		"correct": 0
	},
	{
		"options": ["a = 4", "let a = 4"],
		"correct": 0,
	},
	{
		"options": ["fn foo(){}", "fn (foo) {}"],
		"correct": 1,
	},
	{
        "options": ["fn main(){}", "fn main()"],
        "correct": 1,
	},
	{
		"options": ["let a: i32 = '4'","let a: i32 = 4"],
		"correct": 0,
	}
]

good_responses = [
	"Correct!",
	"Good job!",
	"Nice work!",
	"Keep it up!",
	"Just Like\ni'd do it!",
	"Perfect!",
	"Great!",
]

bad_responses = [
	"Incorrect!",
	"Try again!",
	"Oops!",
	"Keep trying!",
	"Close!",
	"Almost!",
	"Did you read\nthe docs?",
	"watch the\nsyntax!",
	"You're making\nme look like python",
]

def display_questions(dialoge, font):
	options = questions[dialoge]["options"]
	option1_text.text = options[0]
	option2_text.text = options[1]

def clear_options():
	option1_text.text = ""
	option2_text.text = ""

option1_text = label.Label(bitmap_font.load_font("9x18.bdf"), text="", color=0x000200, line_spacing=0.75)
option1_text.x = 2
option1_text.y = 40

option2_text = label.Label(bitmap_font.load_font("9x18.bdf"), text="", color=0x000200, line_spacing=0.75)
option2_text.x = 2
option2_text.y = 80


def handle_answer(answer, question):
	if question is None:
		return
	global dialoge
	if questions[question]["correct"] == answer:
		text_area.text = random.choice(good_responses)
		question = None
	else:
		text_area.text = random.choice(bad_responses)
		question = None
	dialoge += 1
	clear_options()
	if ferris_dialoge[dialoge] is str:
		text_area.text = ferris_dialoge[dialoge]

ferris_text = ferris_dialoge[0]
font = bitmap_font.load_font("9x18b.bdf")
text_area = label.Label(font, text=ferris_text, color=0x000000, line_spacing=0.75)
text_area.x = 2
text_area.y = 5

text_boxes = displayio.OnDiskBitmap("text-box.bmp")
text_boxes_sprite = displayio.TileGrid(
	text_boxes,
	pixel_shader=text_boxes.pixel_shader,
	width=1,
	height=1,
	tile_width=128,
	tile_height=128,
	default_tile=0,
	x=0,
	y=0
)

splash.append(bg_sprite)
splash.append(text_area)
splash.append(ferris_sprite)
splash.append(text_boxes_sprite)
splash.append(option1_text)
splash.append(option2_text)


def advance_dialoge():
	global dialoge
	dialoge += 1
	if dialoge >= len(ferris_dialoge):
		dialoge = 0

while True:
	if question is not None:
		# show textbox
		text_boxes_sprite.x = 0
		text_boxes_sprite.y = 0
		pass
	else:
		# hide textbox
		text_boxes_sprite.x = 0
		text_boxes_sprite.y = 128
		pass
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				
				if isinstance(ferris_dialoge[dialoge], str):
					question = None
					text_area.text = ferris_dialoge[dialoge]
					advance_dialoge()
					
				elif isinstance(ferris_dialoge[dialoge], tuple):
					question = None
					ferris_sprite[0] = ferris_dialoge[dialoge][1]
					text_area.text = ferris_dialoge[dialoge][0]
					advance_dialoge()

				elif isinstance(ferris_dialoge[dialoge], int):
					question = ferris_dialoge[dialoge]
					display_questions(ferris_dialoge[dialoge], font)
			if event.key == pygame.K_x:
				handle_answer(0, question)
			if event.key == pygame.K_c:
				handle_answer(1, question)

