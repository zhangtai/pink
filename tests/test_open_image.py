from PIL import Image, ImageDraw

from config import settings
from core.draw import draw_cross


def test_frame_can_map_to_display():
    for _, display in settings.display.__dict__.items():
        img = Image.new(mode="RGB", size=display.size, color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        for point in display.frame_points():
            draw_cross(draw, point)
        img.show()


# def test_draw_multiline_text():
#     display = settings.display.landscape
