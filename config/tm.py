from dataclasses import dataclass

from escpos.printer import Escpos, Network
from PIL import Image, ImageFont

from .base import FONT_PATH

# printer.codepage = 'gb2312'

PAPER_WIDTH = 512
PAPER_MAX_HEIGHT = 1662


@dataclass
class Printer(object):
    device: Escpos
    image: Image
    font: ImageFont


printer = Printer(
    Network("192.168.3.4"),
    Image.new(mode="L", size=(PAPER_WIDTH, PAPER_MAX_HEIGHT), color=255),
    ImageFont.truetype(FONT_PATH, 24),
)

# F: 24, W: 36
# F: 22, W: 36
# F: 20, W: 40
