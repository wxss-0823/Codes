from manimlib import *
from os import system


class R_IExample(Scene):
    def construct(self):
        # a = Tex("\\lim_{n \\to \\infty}", "\\sum_{i=0}^{n}", "f(\\frac{i} {n})", "\\frac{1} {n}")
        # b = Tex("\\int_{0}^{1}", "f(x)", "{\\rm d}x")
        kwa = {
            "isolate": [
                "\\lim_{n \\to \\infty} \\sum_{i=0}^{n}",
                "f(",
                "\\frac{i} {n}",
                ")",
                "\\frac{1} {n}"
            ],
            "tex_to_color_map": {
                "\\lim_{n \\to \\infty} \\sum_{i=0}^{n}": YELLOW,
                "\\frac{i} {n}":  MAROON_A,
                "\\frac{1} {n}": BLUE
            }
        }
        kwb = {
            "isolate": [
                "\\int_{0}^{1}",
                "f(x)",
                "dx"
            ],
            "tex_to_color_map": {
                "\\int_{0}^{1}": YELLOW,
                "x": MAROON_A,
                "dx": BLUE
            }
        }
        lines = VGroup(
            Tex(
                "\\lim_{n \\to \\infty} \\sum_{i=0}^{n}"
                "f("
                "\\frac{i} {n}"
                ")"
                "\\frac{1} {n}",
                **kwa
            ).scale(2),

            Tex(
                "\\int_{0}^{1}"
                "f(x)"
                "dx",
                **kwb
            ).scale(2)
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        '''
        explicit_formula = Tex(
            "\\lim_{n \\to \\infty} \\sum_{i=0}^{n}"
            "f("
            "\\frac{i} {n}"
            ")"
            "\\frac{1} {n}",
            **kwa
        ).scale(2)
        expanded_formula = Tex(
            "\\int_{0}^{1}"
            "f(x)"
            "dx",
            **kwb
        ).scale(2)
        '''
        self.play(Write(lines[0]))
        self.wait()
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=0,
                key_map={
                    "\\lim_{n \\to \\infty} \\sum_{i=0}^{n}": "\\int_{0}^{1}",
                    # "f(\\frac{i}{n})": "f(x)",
                    # "\\frac{1}{n}": "dx",
                    "\\frac{i} {n}": "x",
                    "\\frac{1} {n}": "dx"
                },
                run_time=3
            )
        )
        self.wait()


if __name__ == '__main__':
    system(f'manim {__file__} R_IExample')