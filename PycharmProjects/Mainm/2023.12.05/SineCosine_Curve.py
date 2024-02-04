from manimlib import *
from os import system


class SineCosine_Curve(Scene):
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()

        self.wait()

    def show_axis(self):
        x_start = np.array([-6, 2, 0])
        x_end = np.array([3, 2, 0])

        y_start = np.array([-4, -3, 0])
        y_end = np.array([-4, 3.5, 0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_xy_labels()

        self.orgin_point = np.array([-4, 2, 0])
        self.curve_start = np.array([-3, 2, 0])

    def add_xy_labels(self):
        x_labels = [
            Tex("\\pi"), Tex("2\\pi"),
            Tex("3\\pi"), Tex("4\\pi"),
        ]

        y_labels = [
            Tex("\\pi"), Tex("2\\pi"),
            Tex("3\\pi"), Tex("4\\pi"),
        ]

        for i in range(len(x_labels)):  # -2 -1 0 1
            x_labels[i].scale(0.6)
            x_labels[i].next_to(np.array([-2 + i, 2, 0]), DOWN)
            self.add(x_labels[i])

        for i in range(len(y_labels)):  # 1 0 -1 -2
            y_labels[i].scale(0.6)
            y_labels[i].rotate(-PI / 2)
            y_labels[i].next_to(np.array([-4, 1 - i, 0]), LEFT)
            self.add(y_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.orgin_point)

        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        orgin_point = self.orgin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(orgin_point, dot.get_center(), color=BLUE)

        ### sine
        def get_line_to_sine():
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x, y, 0]), color=YELLOW_A, stroke_width=2)

        self.sine_curve = VGroup()
        self.sine_curve.add(Line(self.curve_start, self.curve_start))

        def get_sine_curve():
            last_line = self.sine_curve[-1]
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            self.sine_curve.add(new_line)

            return self.sine_curve

        # cosine
        def get_line_to_cosine():
            x = dot.get_center()[0]
            y = self.curve_start[1] - self.t_offset * 2
            return Line(dot.get_center(), np.array([x, y, 0]), color=YELLOW_A, stroke_width=2)

        self.cosine_curve = VGroup()
        self.cosine_curve.add(Line(self.curve_start, self.curve_start))

        def get_cosine_curve():
            last_line = self.cosine_curve[-1]
            x = dot.get_center()[0]
            y = self.curve_start[1] - self.t_offset * 2
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            self.cosine_curve.add(new_line)

            return self.cosine_curve

        dot.add_updater(go_around_circle)  # move dot around the circle

        origin_to_circle_line = always_redraw(get_line_to_circle)  # from circle origin to dot

        dot_to_sine_line = always_redraw(get_line_to_sine)  # from dot to sine curve
        sine_curve_line = always_redraw(get_sine_curve)  # sine curve

        dot_to_cosine_line = always_redraw(get_line_to_cosine)  # from dot to cosine curve
        cosine_curve_line = always_redraw(get_cosine_curve)  # cosine curve

        self.add(dot, orbit)
        self.add(origin_to_circle_line,
                 dot_to_sine_line, sine_curve_line,
                 dot_to_cosine_line, cosine_curve_line,
                 )
        self.wait(8.5)

        dot.remove_updater(go_around_circle)


if __name__ == "__main__":
    system(f"manimgl {__file__} SineCosine_Curve -ow")
