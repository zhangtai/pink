import itertools
import textwrap
from PIL import ImageDraw

from config import tm as settings


def draw_printer_text_box():
    pass


def test_print_display():
    printer = settings.printer
    text = """Returns bounding box (in pixels) of given text relative to given anchor when rendered in font with provided direction, features, and language. Only supported for TrueType fonts.

Use textlength() to get the offset of following text with 1/64 pixel precision. The bounding box includes extra margins for some fonts, e.g. italics or accents."""
    wrapper = textwrap.TextWrapper(width=34)
    mylist = [wrapper.wrap(i) for i in text.split('\n') if i != '']
    text_list = list(itertools.chain(*mylist))
    draw = ImageDraw.Draw(printer.image)
    draw.multiline_text(
        (0, 0),
        "\n".join(text_list),
        font=printer.font,
        fill=10
    )
    img = printer.image.crop((
        0,
        0,
        settings.PAPER_WIDTH,
        draw.multiline_textbbox(
            (0, 0),
            "\n".join(text_list),
            font=printer.font
        )[3]
    ))
    img.show()
    printer.device.image(img)
    printer.device.cut()
