from datetime import datetime
import textwrap

from IT8951 import constants
from IT8951.display import AutoEPDDisplay
from PIL import Image, ImageDraw, ImageFont

margins = (60, 40)
wrap_width = 60

rotate = None
if rotate == "CCW":
    margins = (40, 40)
    wrap_width = 68

display = AutoEPDDisplay(vcom=-1.42, rotate=rotate, mirror=True, spi_hz=24_000_000)


def _place_text(img, text, x_offset=0, y_offset=0):
    """
    Put some centered text at a location on the image.
    """
    fontsize = 32

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf", fontsize
        )
    except OSError:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf", fontsize
        )
    wrapped_text = "\n".join(textwrap.wrap(text, width=wrap_width))
    text_size = draw.textsize(text=wrapped_text, font=font)
    draw.text(margins, wrapped_text, font=font)
    box_size = [
        (margins[0] - 15, margins[1] - 15),
        (margins[0] + text_size[0] + 15, margins[1] + text_size[1] + 15),
    ]
    draw.rounded_rectangle(box_size, radius=20, outline="rgb(0,0,0)", width=4)


if __name__ == "__main__":
    display.clear()
    text = """The initial approach was to create tiny spheres which were half white and half black, and which, depending on the electric charge, would rotate such that the white side or the black side would be visible on the display. Albert and Comiskey were told this approach was impossible by most experienced chemists and materials scientists and they had trouble creating these perfectly half-white, half-black spheres; during his experiments, Albert accidentally created some all-white spheres.[1]

Comiskey experimented with charging and encapsulating those all-white particles in microcapsules mixed in with a dark dye. The result was a system of microcapsules that could be applied to a surface and could then be charged independently to create black and white images.[1] A first patent was filed by MIT for the microencapsulated electrophoretic display in October 1996.[6]

The scientific paper was featured on the cover of Nature, something extremely unusual for work done by undergraduates. The advantage of the microencapsulated electrophoretic display and its potential for satisfying the practical requirements of electronic paper were summarized in the abstract of the Nature paper:

    It has for many years been an ambition of researchers in display media to create a flexible low-cost system that is the electronic analogue of paper ... viewing characteristic[s] result in an "ink on paper" look. But such displays have to date suffered from short lifetimes and difficulty in manufacture. Here we report the synthesis of an electrophoretic ink based on the microencapsulation of an electrophoretic dispersion. The use of a microencapsulated electrophoretic medium solves the lifetime issues and permits the fabrication of a bistable electronic display solely by means of printing. This system may satisfy the practical requirements of electronic paper.[7]"""
    _place_text(display.frame_buf, text)
    display.draw_partial(constants.DisplayModes.GC16)
