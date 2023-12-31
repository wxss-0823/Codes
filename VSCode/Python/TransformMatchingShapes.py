from manimlib import *


class TransformMatchingShapesExample(Scene):
    def construct(self):
        source = Text("the asldfj code", height=1)
        target = Text("here come asdfj", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": 0}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()
