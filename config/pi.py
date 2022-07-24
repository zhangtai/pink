from IT8951.display import AutoEPDDisplay
from IT8951 import constants

from .base import *


def get_display(rotate: str):
    return AutoEPDDisplay(
        vcom=-1.42, rotate=rotate, mirror=True, spi_hz=24_000_000
    )

constants = constants

