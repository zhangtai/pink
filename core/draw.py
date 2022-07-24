from PIL import ImageDraw


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
