from manimlib import *
from os import system


class TransformMatchingTexExample(Scene):
    def construct(self):
        a = Tex("A", "^2", "=", "B^2+C^2")
        b = Tex("A", "=", "\\sqrt{", "B^2+C^2", "}")
        # a = Tex("\\lim_{n \\to \\infty}", "\\sum_{i=0}^{n}", "f(\\frac{i} {n})", "\\frac{1} {n}")
        # b = Tex("\\int_{0}^{1}", "f(x)", "{\\rm d}x")
        self.add(a)
        self.wait()
        self.play(TransformMatchingTex(a, b, key_map={"^2": "\\sqrt{"}))
        self.wait()
