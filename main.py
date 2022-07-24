from PIL import ImageDraw

from config import pi as settings
from core.draw import draw_text_box


if __name__ == "__main__":
    mode = settings.modes.landscape
    display = settings.get_display(mode.rotate)
    text = """The initial approach was to create tiny spheres which were half white and half black, and which, depending on the electric charge, would rotate such that the white side or the black side would be visible on the display. Albert and Comiskey were told this approach was impossible by most experienced chemists and materials scientists and they had trouble creating these perfectly half-white, half-black spheres; during his experiments, Albert accidentally created some all-white spheres.[1]

Comiskey experimented with charging and encapsulating those all-white particles in microcapsules mixed in with a dark dye. The result was a system of microcapsules that could be applied to a surface and could then be charged independently to create black and white images.[1] A first patent was filed by MIT for the microencapsulated electrophoretic display in October 1996.[6]

The scientific paper was featured on the cover of Nature, something extremely unusual for work done by undergraduates. The advantage of the microencapsulated electrophoretic display and its potential for satisfying the practical requirements of electronic paper were summarized in the abstract of the Nature paper:

    It has for many years been an ambition of researchers in display media to create a flexible low-cost system that is the electronic analogue of paper ... viewing characteristic[s] result in an "ink on paper" look. But such displays have to date suffered from short lifetimes and difficulty in manufacture. Here we report the synthesis of an electrophoretic ink based on the microencapsulation of an electrophoretic dispersion. The use of a microencapsulated electrophoretic medium solves the lifetime issues and permits the fabrication of a bistable electronic display solely by means of printing. This system may satisfy the practical requirements of electronic paper.[7]"""
    draw = ImageDraw.Draw(display.frame_buf)
    display.clear()
    draw_text_box(mode, draw, text)
    display.draw_partial(settings.constants.DisplayModes.GC16)

