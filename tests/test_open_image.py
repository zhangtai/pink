from PIL import Image, ImageDraw

from config import settings
from core.draw import draw_cross


def test_frame_can_map_to_display():
    display_settings = settings.display.portait
    img = Image.new(mode="RGB", size=display_settings.display_size, color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    # print(display_settings.frame_points)
    for point in display_settings.frame_points():
        draw_cross(draw, point)
    img.show()
