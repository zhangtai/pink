from datetime import date
from itertools import groupby

import dateutil.parser
import feedparser
from IT8951 import constants
from IT8951.display import AutoEPDDisplay
from PIL import Image, ImageDraw, ImageFont

display = AutoEPDDisplay(vcom=-1.42, rotate='CCW', mirror=True, spi_hz=24_000_000)

urls = [
    'https://www.voachinese.com/api/zm_yqe$$yi',
    'https://cn.nytimes.com/rss/',
]


def get_feeds_by_date(urls: list[str]):
    feeds = [feedparser.parse(url)['entries'] for url in urls]
    feed = [item for feed in feeds for item in feed]
    feed.sort(key=lambda x: dateutil.parser.parse(x['published']), reverse=True)

    groups = []
    uniquekeys = []
    for k, g in groupby(feed, lambda x: date.strftime(dateutil.parser.parse(x['published']), '%Y-%m-%d')):
        groups.append(list(g))
        uniquekeys.append(k)
    print()


def draw_feed(img: Image, articles, fontsize: int = 32) -> None:
    draw = ImageDraw.Draw(img)
    final_test = ""
    try:
        font = ImageFont.truetype(
            "/home/zhangtai/NotoSansSC/NotoSansSC-Regular.otf", fontsize
        )
    except OSError:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf", fontsize
        )
    for i in articles[:30]:
        final_test += i['title'] + '\n'
    draw.text((40, 60), final_test, font=font)


if __name__ == "__main__":
    articles = get_feeds_by_date(urls)
    display.clear()
    draw_feed(display.frame_buf, articles)
    display.draw_partial(constants.DisplayModes.GC16)
