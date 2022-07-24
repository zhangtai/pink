from PIL import ImageDraw

from config import base as settings
from core.draw import draw_text_box
from core.wttr import get_weather


def test_can_get_and_display_weather():
    mode = settings.modes.landscape
    img = mode.image()
    draw = ImageDraw.Draw(img)

    weather = get_weather(['Guangzhou'])
    draw_text_box(mode, draw, weather, font_size=23)
    img.show()
