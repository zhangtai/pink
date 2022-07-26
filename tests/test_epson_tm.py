import calendar

from escpos.printer import Network
from PIL import Image, ImageDraw

from config.tm import PrinterImage


def test_calendar():
    printer = Network("192.168.3.4")
    pi = PrinterImage()

    img = Image.new(mode="L", size=(1664, 512), color=256)
    draw = ImageDraw.Draw(img)
    cal = calendar.Calendar(1)
    header = ""
    for day in cal.monthdatescalendar(2022, 7)[-1]:
        header += (" " + str(day))
    draw.text((20, 20), header, font=pi.font, fill=12)
    printer.image(img.rotate(90, expand=True))
    printer.cut()
