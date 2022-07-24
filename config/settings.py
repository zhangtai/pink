from dataclasses import dataclass
from typing import Optional

from PIL import Image, ImageFont

DISPLAY_LONG_SIDE = 1872
DISPLAY_SHORT_SIDE = 1404
FONT_PATH = 'fonts/JetBrainsMonoRegularNerdFontCompleteMono.ttf'
HEAD_FONT_SIZE = 40
BODY_FONT_SIZE = 32
HEAD_FONT = ImageFont.truetype(FONT_PATH, HEAD_FONT_SIZE)
BODY_FONT = ImageFont.truetype(FONT_PATH, BODY_FONT_SIZE)


@dataclass
class DisplayMode:
    mode: str
    rotate: Optional[str]
    size: tuple[int, int]
    paddings: tuple[int, int]

    def frame_points(self) -> list[tuple[int, int]]:
        return [
            self.paddings,
            (self.size[0] - self.paddings[0], self.paddings[1]),
            (self.size[0] - self.paddings[0], self.size[1] - self.paddings[1]),
            (self.paddings[0], self.size[1] - self.paddings[1]),
        ]

    def image(self) -> Image:
        return Image.new(mode="L", size=self.size, color=256)


@dataclass
class DisplayModes:
    portrait: DisplayMode
    landscape: DisplayMode


display = DisplayModes(
    portrait=DisplayMode(
        mode="PORTRAIT",
        rotate="CCW",
        size=(DISPLAY_SHORT_SIDE, DISPLAY_LONG_SIDE),
        paddings=(40, 40),
    ),
    landscape=DisplayMode(
        mode="LANDSCAPE",
        rotate=None,
        size=(DISPLAY_LONG_SIDE, DISPLAY_SHORT_SIDE),
        paddings=(40, 30),
    )
)
