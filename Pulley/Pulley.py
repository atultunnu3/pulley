from manim import *
import typing
from manim.typing import Point2D, Point3D, Vector3D


class Rope_End_Anim(Animation):
    def __init__(self, 
                    rope:Line,
                    start:Point3D,
                    end:Point3D,
                    
                    radius:float, 
                    not_r:bool=True,
                    v_space:float=0,
                    **kwargs) -> None:
        super().__init__(rope,  **kwargs)
        self.mobject=rope
        self.start=start
        self.end=end
        self.not_r=not_r
        self.radius=radius
        self.ver_space=v_space

    def interpolate_mobject(self, alpha: float) -> None:
        alpha=rush_into(alpha)
        self.mobject.put_start_and_end_on(self.start,[
            self.start[0],
            self.end[1]+(self.start[1]-self.end[1]-self.radius)*alpha 
            if self.not_r 
            else self.end[1]-(self.ver_space-self.radius)*alpha,
            0])




class Pulley():
    def __init__(
            self,
            position=[0,3,0],
            size=0.35,#ZOOM
            init_v=1,
            pulley_acc=0,
            v_space=17,
            e_masses=(1,1)
            ) -> None:
        #rotation
        if e_masses[0]>=e_masses[1]:
            l_rope_ln=size*(1+v_space)
            r_rope_ln=size
            clockw=-1
        else:
            l_rope_ln=size
            r_rope_ln=size*(1+v_space)
            clockw=1
        # level 0
        c=Circle(radius=size,color=WHITE)
        # circ = DashedVMobject(Circle(radius=1, color=WHITE), num_dashes=20)  #TO DO
        d=Dot([0.6*size,0,0],DEFAULT_DOT_RADIUS*size)
        cd=Group(c,d).shift(position)

        # c_rotate=Rotate(cd,PI*2*init_v*clockw,rate_func=rush_into)
        c_rotate=Rotate(cd,v_space/size*init_v*clockw,rate_func=rush_into)
        
        # rope
        l_rope_start=c.point_at_angle(PI)
        r_rope_start=c.point_at_angle(0)
        l_rope_end=[
            l_rope_start[0],
            l_rope_start[1]-l_rope_ln,
            0
            ]
        r_rope_end=[
            r_rope_start[0],
            r_rope_start[1]-r_rope_ln,
            0
            ]
        l_rope=Line(l_rope_start,l_rope_end)
        print(l_rope_start,l_rope_end)
        r_rope=Line(r_rope_start,r_rope_end)

        l_rope_anim=Rope_End_Anim(l_rope,l_rope_start,l_rope_end,size,True)
        r_rope_anim=Rope_End_Anim(r_rope,r_rope_start,r_rope_end,size,False,l_rope_ln)

        #lbox
        sq_length=size
        l_squ=Square(side_length=size).move_to([l_rope_end]).shift([0,-size/2,0])
        always_redraw(lambda:l_squ.next_to(l_rope, DOWN, buff=0))
        r_squ=Square(side_length=size).move_to([r_rope_end]).shift([0,-size/2,0])
        always_redraw(lambda:r_squ.next_to(r_rope, DOWN, buff=0))
 
        

        d= {"mob":(cd,r_rope,l_squ,r_squ),"anim":(c_rotate,r_rope_anim,l_rope_anim)}
        self.d=d
    def ret_dic(self):
        return self.d
