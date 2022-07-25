from dataclasses import dataclass
import itertools
from textwrap import TextWrapper

from escpos.printer import Escpos, Network
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


class Device(object):
    printer: Escpos = Network("192.168.3.4")
    image: Image = Image.new(mode="L", size=(PAPER_WIDTH, PAPER_MAX_HEIGHT), color=255)
    font: ImageFont = ImageFont.truetype(FONT_PATH, 24)
    image_draw: ImageDraw

    text_list: list[str] = []

    def __init__(self) -> None:
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

    def image_to_device(self) -> None:
        self.printer.image(self.image)

    def cut(self) -> None:
        self.printer.cut()


# F: 24, W: 36
# F: 22, W: 36
# F: 20, W: 40
