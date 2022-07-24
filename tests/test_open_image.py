from PIL import ImageDraw

from config import settings
from core.draw import draw_cross, draw_text_box


def test_frame_can_map_to_display():
    display = settings.display.portrait
    img = display.image()
    draw = ImageDraw.Draw(img)
    for point in display.frame_points():
        draw_cross(draw, point)
    img.show()


def test_draw_multiline_text():
    display_portrait = settings.display.portrait
    img_portrait = display_portrait.image()
    draw_portrait = ImageDraw.Draw(img_portrait)
    display_landscape = settings.display.landscape
    img_landscape = display_landscape.image()
    draw_landscape = ImageDraw.Draw(img_landscape)
    text = """Today, we are excited to announce the general availability of LocalStack 1.0. This major release is a significant milestone towards our vision to propel developer productivity - by allowing dev teams to quickly and conveniently develop & test their cloud applications locally and across the CI/CD pipeline.

LocalStack 1.0 is available with our Docker image, shipped for both our Community and Pro users, as well as all users of our newly introduced Team tier. LocalStack’s core emulation platform provides emulated cloud APIs, currently primarily focused on AWS cloud. It is presently being used by a large and active open source community with over 100K active users worldwide. With various features for individual productivity and team collaboration, we provide a comprehensive ecosystem of local AWS services, integrations and tools to make cloud development a breeze.

With LocalStack 1.0, we mark the first milestone of LocalStack’s mission to become the go-to platform for local cloud development. We have spent the last year significantly re-shaping the codebase to make it easier to introduce and extend AWS services, improving parity with AWS. We have also introduced mechanisms to monitor parity, adding new Pro features and introducing a completely new Team tier focused on cross team collaboration. This blog looks at what’s new in LocalStack and what it means for our community and users."""
    draw_text_box(draw_portrait, text, display_portrait)
    draw_text_box(draw_landscape, text, display_landscape)
    img_portrait.show()
    img_landscape.show()
