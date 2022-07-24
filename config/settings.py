from dataclasses import dataclass

DISPLAY_LONG_SIDE = 1872
DISPLAY_SHORT_SIDE = 1404


@dataclass
class DisplayMode:
    mode: str
    size: tuple[int, int]
    paddings: tuple[int, int]

    def frame_points(self) -> list[tuple[int, int]]:
        return [
            self.paddings,
            (self.size[0] - self.paddings[0], self.paddings[1]),
            (self.size[0] - self.paddings[0], self.size[1] - self.paddings[1]),
            (self.paddings[0], self.size[1] - self.paddings[1]),
        ]


@dataclass
class DisplayModes:
    portait: DisplayMode
    landscape: DisplayMode


display = DisplayModes(
    portait=DisplayMode(
        mode="PORTAIT",
        size=(DISPLAY_SHORT_SIDE, DISPLAY_LONG_SIDE),
        paddings=(40, 60),
    ),
    landscape=DisplayMode(
        mode="LANDSCAPE",
        size=(DISPLAY_LONG_SIDE, DISPLAY_SHORT_SIDE),
        paddings=(60, 40),
    )
)
