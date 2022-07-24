import itertools
import textwrap
from typing import Optional

from PIL import ImageDraw, ImageFont

from config import base as settings


def draw_cross(draw: ImageDraw, point: tuple[int, int]) -> None:
    draw.line(
        [
            ((point[0] - 5), (point[1] - 5)),
            ((point[0] + 5), (point[1] + 5)),
        ],
        fill=(0, 0, 0),
        width=2,
    )
    draw.line(
        [
            ((point[0] + 5), (point[1] - 5)),
            ((point[0] - 5), (point[1] + 5)),
        ],
        fill=(0, 0, 0),
        width=2,
    )


def draw_text_box(
    mode: settings.DisplayMode,
    draw: ImageDraw,
    text: str,
    font_size: Optional[int] = None,
) -> None:
    final_font_size = font_size if font_size else settings.BODY_FONT_SIZE
    final_font = ImageFont.truetype(settings.FONT_PATH, final_font_size)

    width = int(2240/final_font_size) \
        if mode.name == "PORTRAIT" \
        else int(2960/final_font_size)
    wrapper = textwrap.TextWrapper(width=width)
    mylist = [wrapper.wrap(i) for i in text.split('\n') if i != '']
    text_list = list(itertools.chain(*mylist))
    # text_size =
    # draw.textbbox(paddings, text="\n".join(text_list), font=settings.FONT)
    draw.multiline_text(
        mode.paddings,
        "\n".join(text_list),
        font=final_font,
        fill=10
    )
