from config import tm as settings


def test_print_display():
    device = settings.Device()
    text = "26. 27. 28. 29. 30. 31. 01.\n[ ] ,<! Get\n     \n Breakfast"
    device.add_text(text)
    device.draw_text()
    device.crop()
    device.image_to_device()
    device.cut()
