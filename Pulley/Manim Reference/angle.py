from manim import *

class RightArcAngleExample(Scene):
    def construct(self):
        line1 = Line( LEFT, RIGHT )
        line2 = Line( DOWN, UP )
        rightarcangles = [
            Angle(line1, line2, dot=True),
            Angle(line1, line2, radius=0.4, quadrant=(1,-1), dot=True, other_angle=True),
            Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8, dot=True, dot_color=YELLOW, dot_radius=0.04, other_angle=True),
            Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED, dot=True, dot_color=GREEN, dot_radius=0.08),
        ]
        plots = VGroup()
        for angle in rightarcangles:
            plot=VGroup(line1.copy(),line2.copy(), angle)
            plots.add(plot)
        plots.arrange(buff=1.5)
        self.add(plots)

# class AngleExample(Scene):
#     def construct(self):
#         line1 = Line( LEFT + (1/3) * UP, RIGHT + (1/3) * DOWN )
#         line2 = Line( DOWN + (1/3) * RIGHT, UP + (1/3) * LEFT )
#         angles = [
#             Angle(line1, line2),
#             Angle(line1, line2, radius=0.4, quadrant=(1,-1), other_angle=True),
#             Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8, other_angle=True),
#             Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED),
#             Angle(line1, line2, other_angle=True),
#             Angle(line1, line2, radius=0.4, quadrant=(1,-1)),
#             Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8),
#             Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED, other_angle=True),
#         ]
#         plots = VGroup()
#         for angle in angles:
#             plot=VGroup(line1.copy(),line2.copy(), angle)
#             plots.add(VGroup(plot,SurroundingRectangle(plot, buff=0.3)))
#         plots.arrange_in_grid(rows=2,buff=1)
#         self.add(plots)