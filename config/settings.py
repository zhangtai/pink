from dataclasses import dataclass

DISPLAY_LONG_SIDE = 1872
DISPLAY_SHORT_SIDE = 1404


@dataclass
class DisplayMode:
    mode: str
    display_size: tuple[int, int]
    paddings: tuple[int, int]

    def frame_points(self) -> list[tuple[int, int]]:
        return [
            self.paddings,
            (self.display_size[0] - self.paddings[0], self.paddings[1]),
            (self.display_size[0] - self.paddings[0], self.display_size[1] - self.paddings[1]),
            (self.paddings[0], self.display_size[1] - self.paddings[1]),
        ]


@dataclass
class DisplayModes:
    portait: DisplayMode
    landscape: DisplayMode


display = DisplayModes(
    portait=DisplayMode(
        mode="PORTAIT",
        display_size=(DISPLAY_SHORT_SIDE, DISPLAY_LONG_SIDE),
        paddings=(40, 60),
    ),
    landscape=DisplayMode(
        mode="LANDSCAPE",
        display_size=(DISPLAY_LONG_SIDE, DISPLAY_SHORT_SIDE),
        paddings=(60, 40),
    )
)
