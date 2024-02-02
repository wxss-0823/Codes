from manimlib import *
import numpy as np


class FuncExample(Scene):
    def construct(self):
        # 初始化坐标轴并标注数字
        axes = Axes(
            (-6, 6),
            (-2, 3),
            y_axis_config={
                "include_tip": True,
            },
            x_axis_config={
                "include_tip": True,
            }
        )
        axes.add_coordinate_labels()

        text1 = Tex("f(x)=\\frac{2sin(x)}{x}")
        text2 = Tex("x")
        text3 = Tex("f(x)=\\frac{sin(2x)}{x}")
        text4 = Tex("f(x)=\\frac{sin(x)}{2x}")
        text5 = Tex("f(x)=\\frac{sin(x)}{4x}")

        # 生成坐标轴以及图例
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        text1.next_to(axes, UP)
        text2.next_to(axes, RIGHT)
        text3.next_to(axes, UP)
        text4.next_to(axes, UP)
        text5.next_to(axes, UP)
        text = VGroup(
            text1,
            text2
        )
        self.play(Write(text))

        # 返回图像
        fx1 = axes.get_graph(
            lambda x: 2 * np.sin(x) / x,
            color=BLUE,
        )
        fx2 = axes.get_graph(
            lambda x: np.sin(2 * x) / x,
            color=BLUE,
        )
        fx3 = axes.get_graph(
            lambda x: np.sin(4 * x) / x / 2,
            color=BLUE,
        )
        fx4 = axes.get_graph(
            lambda x: np.sin(8 * x) / x / 4,
            color=BLUE,
        )

        # 为图像设置标签    有初值即为可选参数，**kwargs 定义关键字参数，输入键值对
        fx1_label = axes.get_graph_label(fx1, "f(x_1)", 3, buff=LARGE_BUFF)
        fx2_label = axes.get_graph_label(fx2, "f(x_2)", buff=LARGE_BUFF)
        fx3_label = axes.get_graph_label(fx3, "f(x_3)", buff=LARGE_BUFF)
        fx4_label = axes.get_graph_label(fx4, "f(x_4)", buff=LARGE_BUFF)

        # 播放时域的图像
        self.play(
            ShowCreation(fx1),
            FadeIn(fx1_label, UP),
        )

        # 你可以使用Axes.input_to_graph_point（缩写Axes.i2gp）来找到图像上的一个点
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(np.pi, fx1))

        # 我们可以从轴上画线，以便更好地标记给定点的坐标在这里
        # always_redraw命令意味着在每一个新帧上重新绘制线来保证线始终跟随着点移动
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        # 读取点的坐标
        F, x_num, M, y_num, B = label = VGroup(
            Text("("),
            DecimalNumber(
                0,
                num_decimal_places=2,
            ),
            Text(","),
            DecimalNumber(
                0,
                num_decimal_places=2,
            ),
            Text(")")
        ).scale(0.4)

        # 始终更新点的坐标
        label.arrange(RIGHT)
        f_always(x_num.set_value, dot.get_x)
        f_always(y_num.set_value, dot.get_y)
        always(label.next_to, dot, UL, buff=0.2)

        # 生成点及点的坐标
        self.add(label)
        self.play(FadeIn(dot, scale=0.5))
        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )

        # ValueTracker存储一个数值，可以帮助我们制作可变参数的动画
        # 通常使用updater或者f_always让其它mobject根据其中的数值来更新
        x_tracker = ValueTracker(PI)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), fx1)
        )
        self.play(
            x_tracker.animate.set_value(0.00001),
            run_time=3
        )
        self.play(
            x_tracker.animate.set_value(-PI),
            run_time=3
        )

        # 去除点及点的坐标
        self.play(
            FadeOut(dot),
            FadeOut(label),
            FadeOut(h_line),
            FadeOut(v_line)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(fx1, fx2),
            FadeTransform(fx1_label, fx2_label),
            FadeTransform(text1, text3)
        )
        self.wait()
        self.play(
            ReplacementTransform(fx2, fx3),
            FadeTransform(fx2_label, fx3_label),
            FadeTransform(text3, text4)
        )
        self.wait()
        self.play(
            ReplacementTransform(fx3, fx4),
            FadeTransform(fx3_label, fx4_label),
            FadeTransform(text4, text5)
        )
        self.wait()
        self.play(
            ReplacementTransform(fx4, fx1),
            FadeTransform(fx4_label, fx1_label),
            FadeTransform(text5, text1)
        )
        self.wait()
