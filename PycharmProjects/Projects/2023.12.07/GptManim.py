from manim import *


# 中文学术版Chat-gpt写的manim数学动画示例
class AnimationExample(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=1, color=BLUE)

        # Create a square
        square = Square(side_length=2, color=RED)

        # Place the square on the left side of the circle
        square.next_to(circle, LEFT)

        # Create an arrow pointing from the square to the circle
        arrow = Arrow(start=square.get_right(), end=circle.get_left(), color=YELLOW)

        # Create text objects
        text1 = Text("Square", color=WHITE).next_to(square, DOWN)
        text2 = Text("Circle", color=WHITE).next_to(circle, DOWN)

        # Add everything to the scene
        self.add(circle, square, arrow, text1, text2)

        # Move the square and circle to the right simultaneously
        self.play(square.animate.shift(RIGHT), circle.animate.shift(RIGHT))

        # Scale the square and circle simultaneously
        self.play(square.animate.scale(0.5), circle.animate.scale(0.5))

        # Rotate the square and circle around their centers simultaneously
        self.play(square.animate.rotate(PI/2), circle.animate.rotate(PI/2))

        # Move the square and circle back to their original positions simultaneously
        self.play(square.animate.shift(LEFT), circle.animate.shift(LEFT))

        # Fade out the square and circle simultaneously
        self.play(FadeOut(square), FadeOut(circle))

        # Remove the arrow and text objects
        self.remove(arrow, text1, text2)

        # Display a final message
        final_text = Text("Animation complete!", color=GREEN).scale(1.5)
        self.play(Write(final_text))
