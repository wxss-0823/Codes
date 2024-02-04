from manim import *
from os import system


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


if __name__ == "__main__":
    system(f"manim {__file__} CreateCircle")
