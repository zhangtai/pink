from PIL import ImageDraw

from config import pi as settings
from core.draw import draw_text_box
from core.wttr import get_weather


if __name__ == "__main__":
    mode = settings.modes.landscape
    display = settings.get_display(mode.rotate)
    weather = get_weather(['Guangzhou'])
    draw = ImageDraw.Draw(display.frame_buf)
    display.clear()
    draw_text_box(mode, draw, weather, font_size=23)
    display.draw_partial(settings.constants.DisplayModes.GC16)
