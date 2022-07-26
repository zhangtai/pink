from dataclasses import dataclass
import itertools
from textwrap import TextWrapper

from PIL import Image, ImageDraw, ImageFont

from .base import FONT_PATH

# printer.codepage = 'gb2312'

PAPER_WIDTH = 512
PAPER_MAX_HEIGHT = 1662


@dataclass
class FontSize:
    font_size: int
    display_width: int


def text_to_list(text: str, width: int = 36) -> list[str]:
    wrapper: TextWrapper = TextWrapper(width=width)
    mylist = [wrapper.wrap(i) for i in text.split('\n') if i != '']
    text_list = list(itertools.chain(*mylist))
    return text_list


class PrinterImage(object):
    def __init__(self) -> None:
        self.image: Image = Image.new(mode="L", size=(PAPER_WIDTH, PAPER_MAX_HEIGHT), color=255)
        self.font: ImageFont = ImageFont.truetype(FONT_PATH, 32)
        self.text_list: list[str] = []
        self.image_draw = ImageDraw.Draw(self.image)

    def add_text(self, text: str) -> None:
        self.text_list += text_to_list(text)

    def draw_text(self) -> None:
        self.image_draw.multiline_text(
            (0, 0),
            "\n".join(self.text_list),
            font=self.font,
            fill=10
        )

    def crop(self) -> None:
        self.image = self.image.crop((
            0,
            0,
            PAPER_WIDTH,
            self.image_draw.multiline_textbbox(
                (0, 0),
                "\n".join(self.text_list),
                font=self.font
            )[3]
        ))

# F: 24, W: 36
# F: 22, W: 36
# F: 20, W: 40
