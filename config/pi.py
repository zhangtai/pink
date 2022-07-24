from IT8951.display import AutoEPDDisplay
from IT8951.constants.DisplayModes import GC16

from .base import *


def get_display(rotate: str):
    return AutoEPDDisplay(
        vcom=-1.42, rotate=rotate, mirror=True, spi_hz=24_000_000
    )
