# manimgl的库manimlib中的TransformMatchingShapes函数存在bug
# 连续两次配对会无法识别
# 出现字符重叠且部分字符不变的问题
# manim正常运行

from manim import *
from os import system


class TransformMatchingShapesExample(Scene):
    def construct(self):
        # src = Text("the morse code")
        src = Text("kahdfjhakdhfkadfasf")
        # tar = Text("here come dots")
        tar = Text("nvkaiiwhqirasvnkafk")
        self.play(Write(src))
        self.wait(0.5)
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(src, tar, **kw))
        self.wait()
        self.play(TransformMatchingShapes(tar, src, **kw))
        self.wait()


if __name__ == "__main__":
    system(f"manim {__file__} TransformMatchingShapesExample")
