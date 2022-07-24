from PIL import Image, ImageDraw

from config import settings


def test_frame_can_map_to_display():
    display_size = (settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT)
    img = Image.new(mode="RGB", size=display_size, color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    img.show()
