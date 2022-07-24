import itertools
import textwrap

from PIL import ImageDraw

from config import settings


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
        draw: ImageDraw, text: str, display: settings.DisplayMode) -> None:
    width = int(2240/settings.BODY_FONT_SIZE) \
        if display.mode == "PORTRAIT" \
        else int(3000/settings.BODY_FONT_SIZE)
    wrapper = textwrap.TextWrapper(width=width)
    mylist = [wrapper.wrap(i) for i in text.split('\n') if i != '']
    text_list = list(itertools.chain(*mylist))
    # text_size =
    # draw.textbbox(paddings, text="\n".join(text_list), font=settings.FONT)
    draw.multiline_text(
        display.paddings,
        "\n".join(text_list),
        font=settings.BODY_FONT, fill=(0, 0, 0)
    )
