import board
import displayio
import busio
import adafruit_imageload
from adafruit_ssd1351 import SSD1351

displayio.release_displays()
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
tft_cs = board.GP3
tft_dc = board.GP4
reset_pin = board.GP5

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=reset_pin, baudrate=16000000
)

display = SSD1351(display_bus, width=128, height=128)
display.rotation=180

# Make the display context
group = displayio.Group()
display.root_group = group
# group.x = 128
# group.y = 128

forest_bg_file = open("/images/bg_forest.bmp", "rb")
forest_bg = displayio.OnDiskBitmap(forest_bg_file)
forest_bg_sprite = displayio.TileGrid(forest_bg, pixel_shader=getattr(forest_bg, 'pixel_shader', displayio.ColorConverter()))

group.append(forest_bg_sprite)

cat_filename = "/images/cat_pbg.bmp"
cat_img, cat_pal = adafruit_imageload.load(cat_filename)
cat_pal.make_transparent(0)
cat_tilegrid = displayio.TileGrid(cat_img, pixel_shader=cat_pal)

group.append(cat_tilegrid)



while True:
    pass