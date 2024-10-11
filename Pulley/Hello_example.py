from manim import *
from Pulley import Pulley
class Pulley_Scene(Scene):
    def construct(self):
        dic=Pulley().ret_dic()
        self.add(*dic['mob'])
        self.play(*dic['anim'])