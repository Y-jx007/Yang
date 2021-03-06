from manimlib.imports import *
from numpy import *

class 足球(ThreeDScene):

    def construct(self):

        五边形列表=[]
        六边形列表=[]
        比例=sqrt(10-2*sqrt(5))/2
        for i in range(0,5):
            五边形列表.append([cos(2*PI/5*i)/比例,sin(2*PI/5*i)/比例,0])
        for i in range(0,6):
            六边形列表.append([cos(2*PI/6*i),sin(2*PI/6*i),0])

        五边形=Polygon(五边形列表[0],五边形列表[1],五边形列表[2],\
                    五边形列表[3],五边形列表[4]).set_color(YELLOW)
        六边形=Polygon(六边形列表[0],六边形列表[1],六边形列表[2],
                    六边形列表[3],六边形列表[4],六边形列表[5]).set_color(BLUE)
        六边形存=六边形.copy()

        self.play(DrawBorderThenFill(六边形))

        copy61=六边形.copy()
        copy62=六边形.copy()
        copy63=六边形.copy()
        
        self.play(copy61.shift,[3/2,sqrt(3)/2,0],copy62.shift,[-3/2,sqrt(3)/2,0],copy63.shift,[0,-sqrt(3),0])
        self.play(Rotate(copy61,arccos(sqrt(5)/3),[1,-sqrt(3),0],about_point=[1,0,0]),\
                  Rotate(copy62,arccos(sqrt(5)/3),[1,+sqrt(3),0],about_point=[-1/2,+sqrt(3)/2,0]),\
                  Rotate(copy63,-arccos(sqrt(5)/3),array([1,0,0]),about_point=[+1/2,-sqrt(3)/2,0]))

        copy51=五边形.copy().rotate(9*PI/30,about_point=ORIGIN)
        copy52=五边形.copy().rotate(29*PI/30,about_point=ORIGIN)
        copy53=五边形.copy().rotate(49*PI/30,about_point=ORIGIN)
        
        self.play(Write(copy51),\
                  Write(copy52),\
                  Write(copy53))
        
        tan54=(5+3*sqrt(5))*sqrt(10-2*sqrt(5))/20,
        distance=sqrt(3)/2-(5+3*sqrt(5))*sqrt(10-2*sqrt(5))/40
        
        self.play(copy51.shift,[0,distance,0],\
                  copy52.shift,[-distance*sqrt(3)/2,-distance/2,0],\
                  copy53.shift,[+distance*sqrt(3)/2,-distance/2,0])

        面角56=arccos(-(5+3*sqrt(5))*sqrt(3)*sqrt(10-2*sqrt(5))/60)
        
        self.play(Rotate(copy51,-面角56,array([1,0,0]),about_point=[1/2,sqrt(3)/2,0]),\
                  Rotate(copy52,面角56,[1,-sqrt(3),0],about_point=[-1,0,0]),\
                  Rotate(copy53,面角56,[1,sqrt(3),0],about_point=[1/2,-sqrt(3)/2,0]))
        self.wait(2)

        一部分=VGroup(六边形,copy61,copy62,copy63,copy51,copy52,copy53)

        self.play(一部分.scale,0.3,一部分.move_to,[6,-3,0])

        text1=TextMobject("上","次","我","们","做","了","个","十","二","面","体","的","视","频")
        for i in range(len(text1)):
            if i%2 == 1:
                text1[i].set_color(BLUE)
            else:
                text1[i].set_color(YELLOW)
        text2=TextMobject("但","是","它","不","是","通","用","的","方","法")
        for i in range(len(text2)):
            if i%2 == 0:
                text2[i].set_color(BLUE)
            else:
                text2[i].set_color(YELLOW)
        text3=TextMobject("我","们","知","道","一","共","有","五","种","正","多","面","体",",","十","三","种","半","正","多","面","体")
        for i in range(len(text3)):
            if i%2 == 1:
                text3[i].set_color(BLUE)
            else:
                text3[i].set_color(YELLOW)
        text4=TextMobject("这","个","可","以","参","看","up","木莫良于梓","的","<<","阿基米德多面体",">>")
        for i in range(len(text4)):
            if i%2 == 0:
                text4[i].set_color(BLUE)
            else:
                text4[i].set_color(YELLOW)
        text5=TextMobject("接","下","来","我","们","就","以","右","下","角","足","球","为","例")
        for i in range(len(text5)):
            if i%2 == 1:
                text5[i].set_color(BLUE)
            else:
                text5[i].set_color(YELLOW)
        text6=TextMobject("用","一","种","通","用","方","法","来","求","这","些","多","面","体","的","体","积")
        for i in range(len(text6)):
            if i%2 == 0:
                text6[i].set_color(BLUE)
            else:
                text6[i].set_color(YELLOW)
        text7=TextMobject("为","简","单","起","见","，","不","妨","设","其","边","长","为","1")
        for i in range(len(text7)):
            if i%2 == 1:
                text7[i].set_color(BLUE)
            else:
                text7[i].set_color(YELLOW)
        method=TextMobject("方法可以大致分为以下几步").scale(2).to_edge(UP)
        method1=TextMobject("1.求多边形面积").next_to(method,DOWN*2).set_color(BLUE)
        method2=TextMobject("2.求二面角").next_to(method1,DOWN*2).set_color(YELLOW)
        method3=TextMobject("3.求高").next_to(method2,DOWN*2).set_color(BLUE)
        method4=TextMobject("4.底面积乘高,各棱锥体积相加").next_to(method3,DOWN*2).set_color(YELLOW)
        methods=VGroup(method,method1,method2,method3,method4)
        self.play(FadeInFromLarge(text1))
        self.add_fixed_in_frame_mobjects(text1)
        self.wait(2.5)
        self.play(ReplacementTransform(text1,text2))
        self.add_fixed_in_frame_mobjects(text2)
        self.wait(2.5)
        self.play(ReplacementTransform(text2,text3))
        self.add_fixed_in_frame_mobjects(text3)
        self.wait(2.5)
        self.play(ReplacementTransform(text3,text4))
        self.add_fixed_in_frame_mobjects(text4)
        self.wait(2.5)
        self.play(ReplacementTransform(text4,text5))
        self.add_fixed_in_frame_mobjects(text5)
        self.wait(2.5)
        self.play(ReplacementTransform(text5,text6))
        self.add_fixed_in_frame_mobjects(text6)
        self.wait(2.5)
        self.play(ReplacementTransform(text6,text7))
        self.add_fixed_in_frame_mobjects(text7)
        self.wait(2.5)
        self.play(VFadeOut(text7,run_time=2))
        self.play(VFadeIn(methods,run_time=2))
        self.add_fixed_in_frame_mobjects(method)
        self.add_fixed_in_frame_mobjects(method1)
        self.add_fixed_in_frame_mobjects(method2)
        self.add_fixed_in_frame_mobjects(method3)
        self.add_fixed_in_frame_mobjects(method4)
        copy1=method1.copy()
        self.play(FadeIn(copy1))
        self.play(FadeOut(methods))
        self.wait()
        self.play(copy1.to_edge,UP)

        model5=五边形.copy().move_to([-3,0,0])
        model6=六边形存.copy().move_to([3,0,0])
        self.play(FadeIn(model5),FadeIn(model6))
        S5=TextMobject("S","5")
        S5[1].scale(0.7).shift(DOWN*0.2)
        S5.move_to([-3,2,0]).set_color(YELLOW)
        S6=TextMobject("S","6")
        S6[1].scale(0.7).shift(DOWN*0.2)
        S6.move_to([3,2,0]).set_color(BLUE)
        self.play(DrawBorderThenFill(S5),DrawBorderThenFill(S6))

        V5=model5.get_vertices()
        V6=model6.get_vertices()
        A5=Arc(arc_center=V5[0],radius=0.2,start_angle=7*PI/10,angle=3*PI/5,color=YELLOW)
        self.play(Write(A5))
        A6=Arc(arc_center=V6[0],radius=0.2,start_angle=2*PI/3,angle=2*PI/3,color=BLUE)
        self.play(Write(A6))
        a5=TexMobject("\\frac{3\\pi}{5}").next_to(A5).set_color(YELLOW).scale(0.6)
        a6=TexMobject("\\frac{2\\pi}{3}").next_to(A6).set_color(BLUE).scale(0.6)
        self.play(DrawBorderThenFill(a5),DrawBorderThenFill(a6))

        C5=model5.get_center()
        C6=model6.get_center()
        L51=Line(C5,V5[0]).set_color(YELLOW)
        L52=Line(C5,V5[4]).set_color(YELLOW)
        L61=Line(C6,V6[0]).set_color(BLUE)
        L62=Line(C6,V6[5]).set_color(BLUE)
        L5v=DashedLine(C5,0.5*array(V5[0])+0.5*array(V5[4])).set_color(YELLOW)
        L6v=DashedLine(C6,0.5*array(V6[0])+0.5*array(V6[5])).set_color(BLUE)

        self.play(Write(L51),Write(L52))
        self.play(Write(L5v))
        self.play(S5.shift,[-3,0,0])
        VS5=TexMobject("=5\\times\\frac{1}{2}\\times","1\\times\\frac{1}{2}\\times","\\tan(\\frac{3\\pi}{10})").set_color(YELLOW)
        VS5.next_to(S5)
        VS55=TexMobject("=\\frac{5\\tan(\\frac{3\\pi}{10})}{4}").next_to(S5)
        self.play(DrawBorderThenFill(VS5))
        self.wait(2)
        self.play(ReplacementTransform(VS5,VS55))
        self.wait()

        self.play(Write(L61),Write(L62))
        self.play(Write(L6v))
        self.play(S6.shift,[-3,0,0])
        VS6=TexMobject("=6\\times\\frac{1}{2}\\times","1\\times\\frac{1}{2}\\times","\\tan(\\frac{\\pi}{3})").set_color(BLUE)
        VS6.next_to(S6)
        VS66=TexMobject("=\\frac{3\\sqrt{3}}{2}").next_to(S6)
        self.play(DrawBorderThenFill(VS6))
        self.wait(2)
        self.play(ReplacementTransform(VS6,VS66))
        self.wait()

        s5=VGroup(S5,VS55)
        s6=VGroup(S6,VS66)
        self.play(s5.scale,0.5,s5.to_corner,UL)
        self.play(s6.scale,0.5,s6.next_to,s5,DOWN,s6.to_edge,LEFT)

        self.play(FadeOut(model5),FadeOut(L51),FadeOut(L52),FadeOut(L5v),\
                  FadeOut(model6),FadeOut(L61),FadeOut(L62),FadeOut(L6v),\
                  FadeOut(A5),FadeOut(a5),FadeOut(A6),FadeOut(a6))

        self.play(FadeIn(method2),FadeOut(copy1))
        self.play(method2.to_edge,UP)

        self.play(一部分.scale,10/3,一部分.move_to,[0,0,0])

        t5=TexMobject("5").move_to(copy51).set_color(YELLOW).scale(0.8)
        t61=TexMobject("6").move_to(copy61).set_color(BLUE).scale(0.8)
        t62=TexMobject("6").move_to(六边形).set_color(BLUE).scale(0.8)
        t=VGroup(t5,t61,t62)

        self.play(DrawBorderThenFill(t5),DrawBorderThenFill(t61),DrawBorderThenFill(t62))
        
        self.play(一部分.shift,[-2,0,0],t.shift,[-2,0,0])

        vt1=六边形.get_vertices()
        vt2=copy61.get_vertices()

        vg=[vt1[0],vt1[1],vt1[2],vt2[2]]
        p1=Line(vg[0],vg[2]).set_color(GREEN)
        p2=Line(vg[2],vg[3]).set_color(LIGHT_BROWN)
        p3=Line(vg[0],vg[3]).set_color(GREEN)
        self.play(Write(p1),Write(p3),Write(p2))

        dv1=array(vt1[2])/10+array(vt2[2])*9/10
        dv2=array(vt1[0])/10+array(vt2[2])*9/10
        dv3=array(vt1[0])*9/10+array(vt2[2])/10
        dv4=array(vt1[0])*9/10+array(vt1[2])/10
        arc1=ArcBetweenPoints(dv1,dv2)
        arc2=ArcBetweenPoints(dv3,dv4)

        self.play(Write(arc1),Write(arc2))

        A=TextMobject("A").next_to(arc1,UR).scale(0.8)
        B=TextMobject("B").next_to(arc2,DR).scale(0.8)

        self.play(DrawBorderThenFill(A),DrawBorderThenFill(B))

        te1=TextMobject("易求得").move_to([3,2.5,0])
        te2=TexMobject("\\text{棕}","=","\\frac{\\sqrt{5}+1}{2}")
        te2[0].set_color(LIGHT_BROWN)
        te2.scale(0.8).next_to(te1,DOWN)
        te3=TexMobject("\\text{绿}","=","\\sqrt{3}")
        te3[0].set_color(GREEN)
        te3.scale(0.8).next_to(te2,DOWN,aligned_edge=LEFT)
        self.play(DrawBorderThenFill(te1),DrawBorderThenFill(te2),DrawBorderThenFill(te3))

        
        self.wait(2)
        self.play(te2.scale,5/8,te2.next_to,s6,DOWN,te2.to_edge,LEFT)
        self.play(te3.scale,5/8,te3.next_to,te2,DOWN,te3.to_edge,LEFT)

        te11=TextMobject("余弦定理").move_to([3,2.5,0])
        te22=TexMobject("\\cos(A)","=","\\frac{\\text{棕}^2+\\text{绿}^2-\\text{绿}^2}{2\\times\\text{棕}\\times\\text{绿}}")
        te22[2][0].set_color(LIGHT_BROWN)
        te22[2][3].set_color(GREEN)
        te22[2][6].set_color(GREEN)
        te22[2][11].set_color(LIGHT_BROWN)
        te22[2][13].set_color(GREEN)
        te22.scale(0.8).next_to(te11,DOWN)
        te33=TexMobject("=\\frac{\\sqrt{15}+\\sqrt{3}}{12}")
        te33.scale(0.8).next_to(te22[1],DOWN*2.5,aligned_edge=LEFT)
        self.play(ReplacementTransform(te1,te11))
        self.play(Write(te22))
        self.play(Write(te33))
        te44=TexMobject("\\cos(B)","=","\\frac{\\text{绿}^2+\\text{绿}^2-\\text{棕}^2}{2\\times\\text{绿}\\times\\text{绿}}")
        te44[2][0].set_color(GREEN)
        te44[2][3].set_color(GREEN)
        te44[2][6].set_color(LIGHT_BROWN)
        te44[2][11].set_color(GREEN)
        te44[2][13].set_color(GREEN)
        te44.scale(0.8).next_to(te22,DOWN*5.5)
        te55=TexMobject("=\\frac{9-\\sqrt{5}}{12}")
        te55.scale(0.8).next_to(te44[1],DOWN*2.5,aligned_edge=LEFT)
        self.play(Write(te44))
        self.play(Write(te55))

        
        self.wait(4)
        self.play(FadeOutAndShift(te22[1::],RIGHT),FadeOutAndShift(te44[1::],RIGHT))
        self.play(te33.next_to,te22[0],te55.next_to,te44[0])

        vga=VGroup(te22[0],te33)
        vgb=VGroup(te44[0],te55)

        self.play(vga.scale,5/8,vga.next_to,te2,DOWN*3,vga.to_edge,LEFT,vgb.scale,5/8,vgb.next_to,vga,DOWN*5,vgb.to_edge,LEFT)
        self.play(FadeOutAndShift(te2,LEFT),FadeOutAndShift(te3,LEFT))
        self.play(vga.next_to,s6,DOWN*1.2,vga.to_edge,LEFT,vgb.next_to,vga,DOWN,vgb.to_edge,LEFT,vgb.shift,UP*1.2)

        te111=TextMobject("三面角余弦定理").move_to([3,2.5,0])
        te222=TexMobject("\\cos","(5,6",")","=","\\frac{\\cos(A)-\\cos(\\frac{\\pi}{5})\\cos(\\frac{\\pi}{6})}{\\sin(\\frac{\\pi}{5})\\sin(\\frac{\\pi}{6})}")
        te222[1][1].set_color(YELLOW)
        te222[1][3].set_color(BLUE)
        te222.scale(0.8).next_to(te111,DOWN).shift([1,0,0])
        te333=TexMobject("=-\\frac{\\csc(\\frac{\\pi}{5})}{12}")
        te333.scale(0.8).next_to(te222[3],DOWN*2.5,aligned_edge=LEFT)
        self.play(ReplacementTransform(te11,te111))
        self.play(Write(te222))
        self.play(Write(te333))
        te444=TexMobject("\\cos","(6,6",")","=","\\frac{\\cos(B)-\\cos(\\frac{\\pi}{6})\\cos(\\frac{\\pi}{6})}{\\sin(\\frac{\\pi}{6})\\sin(\\frac{\\pi}{6})}")
        te444[1][1].set_color(BLUE)
        te444[1][3].set_color(BLUE)
        te444.scale(0.8).next_to(te222,DOWN*5.5)
        te555=TexMobject("=-\\frac{\\sqrt{5}}{3}")
        te555.scale(0.8).next_to(te444[3],DOWN*2.5,aligned_edge=LEFT)
        self.play(Write(te444))
        self.play(Write(te555))

        
        self.wait(5)
        self.play(FadeOutAndShift(te222[3::],RIGHT),FadeOutAndShift(te444[3::],RIGHT))
        self.play(te333.next_to,te222[2],te555.next_to,te444[2])

        vgaa=VGroup(te222[0:3],te333)
        vgbb=VGroup(te444[0:3],te555)

        self.play(vgaa.scale,5/8,vgaa.next_to,vgb,DOWN*1.5,vgaa.to_edge,LEFT,vgbb.scale,5/8,vgbb.next_to,vgb,DOWN*5,vgbb.to_edge,LEFT)
        self.play(FadeOutAndShift(vga,LEFT),FadeOutAndShift(vgb,LEFT))
        self.play(vgaa.next_to,s6,DOWN*1.2,vgaa.to_edge,LEFT,vgbb.next_to,vgaa,DOWN,vgbb.to_edge,LEFT,vgbb.shift,UP*1.8)

        self.play(FadeOut(te111))
        self.play(FadeOut(A),FadeOut(B))
        self.play(FadeOut(arc1),FadeOut(arc2))
        self.play(FadeOut(p1),FadeOut(p2),FadeOut(p3))
        self.play(FadeOut(t5),FadeOut(t61),FadeOut(t62))
        self.play(一部分.move_to,ORIGIN)
        self.play(ReplacementTransform(method2,method3.to_edge(UP)))

        o1=六边形.get_center()
        o2=copy63.get_center()
        n2=copy53.get_vertices()
        o3=(array(n2[0])+array(n2[1])+array(n2[2])+array(n2[3])+array(n2[4]))/5
        o=array(o1)+array([0,0,(3*sqrt(3)+sqrt(15))/4])
        Line1=DashedLine(o,o1).set_color(BLUE)
        Line2=DashedLine(o,o2).set_color(BLUE)
        Line3=DashedLine(o,o3).set_color(YELLOW)

        tex1=TextMobject("由足球中心对多边形中心作高").scale(0.7).move_to([4,2.5,0])
        self.play(ShowCreation(tex1))
        y1=六边形.copy()
        y2=copy63.copy()
        y3=copy53.copy()
        y=VGroup(y1,y2,y3,Line1,Line2,Line3)
        self.play(FadeIn(y))
        self.play(FadeOut(一部分))

        self.play(Rotate(y,PI/2,axis=array([0,0,1]),about_point=o1))

        ver6=y1.get_vertices()
        mid=array(ver6[5])/2+array(ver6[4])/2

        self.play(y.shift,[-sqrt(3)/2,0,0])
        self.play(Rotate(y,arccos(sqrt(5)/3)/2,axis=array([0,1,0]),about_point=mid))       
        self.play(Rotate(y,-PI/3,axis=array([1,0,0]),about_point=ORIGIN))

        ve6=y1.get_vertices()
        mi=array(ve6[5])/2+array(ve6[4])/2
        o11=y1.get_center()
        o22=y2.get_center()
        oo=Line1.get_start()

        self.play(FadeOut(Line3),FadeOut(y3))
        Line61=DashedLine(o11,mi).set_color(PURPLE)
        Line62=DashedLine(o22,mi).set_color(PURPLE)
        Line63=DashedLine(oo,mi).set_color(GREY)
        self.play(DrawBorderThenFill(Line61),DrawBorderThenFill(Line62),DrawBorderThenFill(Line63))

        av1=array(mi)*6/7+array(oo)/7
        av2=array(mi)*2/3+array(o22)/3

        arc3=DashedVMobject(ArcBetweenPoints(av2,av1))
        self.play(DrawBorderThenFill(arc3))

        theta=TexMobject("\\theta")
        theta.scale(0.6).next_to(arc3,DR*0.4)
        self.play(Write(theta))

        tex2=TextMobject("易求得").scale(0.7).next_to(tex1,DOWN)
        tex3=TexMobject("\\text{紫}=\\frac{\\sqrt{3}}{2}")
        tex3[0][0].set_color(PURPLE)
        tex3.scale(0.7).next_to(tex2,DOWN)
        self.play(Write(tex2))
        self.play(Write(tex3))
        self.wait(2)
        self.play(tex3.scale,5/7,tex3.next_to,vgbb,DOWN,tex3.to_edge,LEFT)

        H5=TextMobject("H","5")
        H5[1].scale(0.7).shift(DOWN*0.2)
        H5.set_color(YELLOW)
        H5.next_to(Line3,LEFT)
        H6=TextMobject("H","6")
        H6[1].scale(0.7).shift(DOWN*0.2)
        H6.set_color(BLUE).scale(0.7)
        H6.next_to(Line3,RIGHT*1.5)
        self.play(Write(H6))
        
        H61=H6.copy()
        eqn1=TexMobject("=\\text{紫}\\times\\tan(\\theta)")
        eqn1[0][1].set_color(PURPLE)
        eqn1.scale(0.7).next_to(H61,RIGHT)
        vn1=VGroup(H61,eqn1).next_to(tex2,DOWN)
        self.play(Write(vn1))
        vgbb2=vgbb.copy().scale(7/5).next_to(vn1,DOWN)
        self.play(ReplacementTransform(vgbb.copy(),vgbb2))
        self.play(vgbb2[0].next_to,vgbb2[1][0][0],RIGHT,vgbb2[1][0][1::].next_to,vgbb2[1][0][0],LEFT)
        self.play(vgbb2.next_to,vn1,DOWN,aligned_edge=LEFT)

        theta2=TexMobject("\\cos(2\\theta)")
        theta2.scale(0.7).next_to(vgbb2[1][0][0])
        self.play(ReplacementTransform(vgbb2[0],theta2))

        text1=TexMobject("=\\frac{1-\\tan^2(\\theta)}{1+\\tan^2(\\theta)}")
        text1.scale(0.7).next_to(vgbb2[1][0][0],DOWN,aligned_edge=LEFT)
        self.play(Write(text1))

        vn2=VGroup(theta2,text1,vgbb2[1][0][0],vgbb2[1][0][1::])

        text2=TexMobject("\\tan(\\theta)=\\frac{3+\\sqrt{5}}{2}")
        text2.scale(0.7).next_to(vn1,DOWN,aligned_edge=LEFT)
        self.wait(2)
        self.play(ReplacementTransform(vn2,text2,run_time=3))

        self.play(ShowCreationThenDestructionAround(tex3,color=PURPLE),ShowCreationThenDestructionAround(eqn1[0][1],color=PURPLE))

        vn3=VGroup(vn1,text2)
        text4=TexMobject("=\\frac{3\\sqrt{3}+\\sqrt{15}}{4}")
        text4.scale(0.7)
        H62=H6.copy()
        text4.next_to(H62)
        vn4=VGroup(H62,text4)
        vn4.next_to(tex2,DOWN)
        self.wait(2)
        self.play(ReplacementTransform(vn3,vn4,run_time=3))

        self.play(vn4.scale,5/7,vn4.next_to,tex3,DOWN,vn4.to_edge,LEFT)
        vn5=VGroup(tex3,vn4)
        self.play(FadeOutAndShift(vgaa,LEFT),FadeOutAndShift(vgbb,LEFT))
        self.play(vn5.next_to,s6,DOWN,vn5.to_edge,LEFT)

        self.play(FadeOut(theta))
        self.play(FadeOut(arc3))
        self.play(FadeOut(Line61),FadeOut(Line62),FadeOut(Line63))
        self.play(FadeOut(H6))
        self.play(FadeIn(y3),FadeIn(Line3))

        self.play(Rotate(y,2.1*PI/3,axis=array([0,1,1]),about_point=y.get_center()))
        self.play(FadeOut(Line2),FadeOut(y2))

        vw=y3.get_vertices()
        mw=array(vw[0])/2+array(vw[1])/2
        r1=array(vw[0])/5+array(vw[1])/5+array(vw[2])/5+array(vw[3])/5+array(vw[4])/5
        r2=y1.get_center()
        r=Line3.get_start()
        Li1=DashedLine(mw,r1).set_color(ORANGE)
        Li2=DashedLine(mw,r2).set_color(PURPLE)
        Li3=DashedLine(mw,r).set_color(GREY)
        self.play(DrawBorderThenFill(Li1),DrawBorderThenFill(Li2),DrawBorderThenFill(Li3))

        H666=H6.copy().next_to(Line1,RIGHT*0.2)
        H555=H5.scale(0.7).copy().next_to(Line3,LEFT*0.5)
        self.play(DrawBorderThenFill(H555),DrawBorderThenFill(H666))

        tc=TexMobject("\\text{橙}=\\frac{\\tan(\\frac{3\\pi}{10})}{2}")
        tc[0][0].set_color(ORANGE)
        tc.scale(0.7).next_to(tex2,DOWN).shift([-1,0,0])
        self.play(Write(tc))
        self.wait(2)
        
        tc2=TexMobject("\\text{H}5=\\sqrt{{\\text{H}6}^2+\\text{紫}^2-\\text{橙}^2}")
        tc2[0][1].scale(0.7).shift(DOWN*0.2)
        tc2[0][0:2].set_color(YELLOW)
        tc2[0][6].scale(0.7).shift(DOWN*0.2)
        tc2[0][5:7].set_color(BLUE)
        tc2[0][9].set_color(PURPLE)
        tc2[0][12].set_color(ORANGE)
        tc2.scale(0.7).next_to(tc,DOWN,aligned_edge=LEFT)
        self.play(Write(tc2))
        self.wait(2)

        tc3=TexMobject("=\\frac{\\sqrt{54+18\\sqrt{5}-4\\tan^2(\\frac{3\\pi}{10})}}{4}")
        tc3.scale(0.7).next_to(tc2[0][2],DOWN,aligned_edge=LEFT)
        self.play(Write(tc3))
        self.wait(2)

        self.play(FadeOut(tc2[0][2::]))
        self.play(FadeOut(tc),FadeOut(tex3))
        self.play(tc3.shift,UP)
        vnv=VGroup(tc3,tc2[0][0:2])
        self.play(vnv.scale,5/7,vnv.next_to,s6,DOWN,vnv.to_edge,LEFT,vnv.shift,DOWN*0.1,vn4.shift,DOWN*0.4)

        self.play(FadeOut(tex1),FadeOut(tex2))
        self.play(FadeOut(Li1),FadeOut(Li2),FadeOut(Li3))
        self.play(FadeOut(H555),FadeOut(H666))

        z5=VGroup(Line3,y3)
        z6=VGroup(Line1,y1)

        self.play(z6.shift,[2,0,0])

        axis5=array(Line3.get_start())-array(Line3.get_end())
        axis6=array(Line3.get_start())-array(Line3.get_end())

        self.play(Rotate(z5,PI/11),Rotate(z6,-PI/7.5))
        self.play(Rotate(z5,-PI/20,axis=axis5,about_point=Line3.get_end()),ApplyMethod(z6.shift,-axis6*0.08))

        vv5=y3.get_vertices()
        vv6=y1.get_vertices()
        
        od5=Line3.get_start()
        od6=Line1.get_start()
        
        LL51=Line(od5,vv5[0]).set_color(YELLOW)
        LL52=Line(od5,vv5[1]).set_color(YELLOW)
        LL53=Line(od5,vv5[2]).set_color(YELLOW)
        LL54=Line(od5,vv5[3]).set_color(YELLOW)
        LL55=DashedLine(od5,vv5[4]).set_color(YELLOW)

        LL61=Line(od6,vv6[0]).set_color(BLUE)
        LL62=Line(od6,vv6[1]).set_color(BLUE)
        LL63=Line(od6,vv6[2]).set_color(BLUE)
        LL64=Line(od6,vv6[3]).set_color(BLUE)
        LL65=DashedLine(od6,vv6[4]).set_color(BLUE)
        LL66=Line(od6,vv6[5]).set_color(BLUE)

        self.play(DrawBorderThenFill(LL51),DrawBorderThenFill(LL52),DrawBorderThenFill(LL53),\
                  DrawBorderThenFill(LL54),DrawBorderThenFill(LL55),DrawBorderThenFill(LL61),\
                  DrawBorderThenFill(LL62),DrawBorderThenFill(LL63),DrawBorderThenFill(LL64),\
                  DrawBorderThenFill(LL65),DrawBorderThenFill(LL66))

        vLine=VGroup(LL51,LL52,LL53,LL54,LL55,LL61,LL62,LL63,LL64,LL65,LL66)

        self.play(ReplacementTransform(method3,method4.to_edge(UP)))

        Vt5=TextMobject("V5")
        Vt5[0][1].scale(0.7).shift(DOWN*0.2)
        Vt5.scale(0.8).set_color(YELLOW).next_to(z5,DOWN*3).shift([0,-0.1,0])
        Vt6=TextMobject("V6")
        Vt6[0][1].scale(0.7).shift(DOWN*0.2)
        Vt6.scale(0.8).set_color(BLUE).next_to(z6,DOWN*3)

        self.play(DrawBorderThenFill(Vt5),DrawBorderThenFill(Vt6))

        self.play(Vt5.shift,[-2,0,0])
        s55=s5[0][0:2].copy()
        s56=tc2[0][0:2].copy()
        equ5=TexMobject("=\\frac{1}{3}\\times")
        equ5.scale(0.8).next_to(Vt5)
        times5=TexMobject("\\times")
        times5.scale(0.8).next_to(equ5,RIGHT*3)
        self.play(Write(equ5))
        self.play(s55.scale,8/5,s55.next_to,equ5,s56.scale,8/5,s56.next_to,times5)
        self.play(Write(times5))

        self.play(Vt6.shift,[-1,0,0])
        s65=s6[0][0:2].copy()
        s66=H62.copy()
        equ6=TexMobject("=\\frac{1}{3}\\times")
        equ6.scale(0.8).next_to(Vt6)
        times6=TexMobject("\\times")
        times6.scale(0.8).next_to(equ6,RIGHT*3)
        self.play(Write(equ6))
        self.play(s65.scale,8/5,s65.next_to,equ6,s66.scale,8/5,s66.next_to,times6)
        self.play(Write(times6))

        wen1=TextMobject("用上个视频中的相似求出")
        wen1.scale(0.6).next_to(vn4,DOWN).shift([0.5,-0.5,0])
        wen2=TexMobject("\\cos(\\frac{\\pi}{5})=\\frac{\\sqrt{5}+1}{4}")
        wen2.scale(0.6).next_to(wen1,DOWN)
        wen3=TextMobject("经过些许计算")
        wen3.scale(0.6).next_to(wen2,DOWN)
        self.play(Write(wen1))
        self.wait()
        self.play(Write(wen2))
        self.wait()
        self.play(Write(wen3))
        self.wait()

        wen=VGroup(wen1,wen2,wen3)
        self.play(ShowCreationThenDestructionAround(wen))

        shu1=TexMobject("=\\frac{35+13\\sqrt{5}}{48}")
        shu2=TexMobject("=\\frac{9+3\\sqrt{5}}{8}")
        shu1.scale(0.8).next_to(Vt5)
        shu2.scale(0.8).next_to(Vt6)
        vvg5=VGroup(s55,s56,equ5,times5)
        vvg6=VGroup(s65,s66,equ6,times6)
        self.play(ReplacementTransform(vvg5,shu1),ReplacementTransform(vvg6,shu2))

        self.play(FadeOut(vLine),FadeOut(z5),FadeOut(z6))
        self.play(FadeOut(wen))
        self.play(FadeOut(vn4),FadeOut(vnv),FadeOut(s5),FadeOut(s6))

        bigv5=VGroup(Vt5,shu1)
        bigv6=VGroup(Vt6,shu2)

        self.play(bigv5.scale,5/8,bigv5.to_corner,UL)
        self.play(bigv6.scale,5/8,bigv6.next_to,bigv5,DOWN,bigv6.to_edge,LEFT)

        end1=TextMobject("设五边形有","X","个,","六边形有","Y","个")
        end1[1].set_color(YELLOW)
        end1[4].set_color(BLUE)
        end1.scale(0.8).move_to([0,2,0])
        end2=TextMobject("由于三个多边形共一个点")
        end2.scale(0.8).next_to(end1,DOWN)
        end3=TexMobject("\\text{故共有}\\frac{5\\text{X}+6\\text{Y}}{3}\\text{个点}")
        end3.scale(0.8).next_to(end2,DOWN)
        end3[0][4].set_color(YELLOW)
        end3[0][7].set_color(BLUE)
        end4=TextMobject("又两个多边形共一条棱")
        end4.scale(0.8).next_to(end3,DOWN)
        end5=TexMobject("\\text{故共有}\\frac{5\\text{X}+6\\text{Y}}{2}\\text{条棱}")
        end5.scale(0.8).next_to(end4,DOWN)
        end5[0][4].set_color(YELLOW)
        end5[0][7].set_color(BLUE)
        end=VGroup(end1,end2,end3,end4,end5)

        self.play(Write(end1))
        self.wait(2)
        self.play(Write(end2))
        self.wait(2)
        self.play(Write(end3))
        self.wait(2)
        self.play(Write(end4))
        self.wait(2)
        self.play(Write(end5))
        self.wait(2)

        en1=TexMobject("\\text{面}=\\text{X}+\\text{Y}")
        en1[0][2].set_color(YELLOW)
        en1[0][4].set_color(BLUE)
        en1.scale(0.5).to_edge(LEFT).shift(UP)
        en2=TexMobject("\\text{点}=\\frac{5\\text{X}+6\\text{Y}}{3}")
        en2[0][3].set_color(YELLOW)
        en2[0][6].set_color(BLUE)
        en2.scale(0.5).next_to(en1,DOWN*2,aligned_edge=LEFT).shift([0,-0.2,0])
        en3=TexMobject("\\text{棱}=\\frac{5\\text{X}+6\\text{Y}}{2}")
        en3[0][3].set_color(YELLOW)
        en3[0][6].set_color(BLUE)
        en3.scale(0.5).next_to(en2,DOWN*2,aligned_edge=LEFT)
        en=VGroup(en1,en2,en3)

        self.play(ReplacementTransform(end,en,run_time=3))

        e1=TextMobject("由多面体的欧拉公式")
        e1.scale(0.8).move_to([0,2,0])
        e2=TexMobject("\\text{面}+\\text{点}-\\text{棱}=2")
        e2.scale(0.8).next_to(e1,DOWN*2)

        
        self.play(Write(e1))
        self.play(Write(e2))

        groupv1=en1[0][2::].copy().scale(2)
        plus=TexMobject("+")
        groupv2=en2[0][2::].copy().scale(2)
        minus=TexMobject("-")
        groupv3=en3[0][2::].copy().scale(2)
        eq2=TexMobject("=2")
        
        plus.next_to(groupv1)
        groupv2.next_to(plus)
        minus.next_to(groupv2)
        groupv3.next_to(minus)
        eq2.next_to(groupv3)

        env=VGroup(groupv1,groupv2,groupv3,plus,minus,eq2)
        env.scale(0.8).next_to(e2,DOWN*2)

        self.play(ReplacementTransform(en1[0][2::].copy(),groupv1),\
                  ReplacementTransform(en2[0][2::].copy(),groupv2),\
                  ReplacementTransform(en3[0][2::].copy(),groupv3))

        self.play(DrawBorderThenFill(plus),DrawBorderThenFill(minus),DrawBorderThenFill(eq2))

        trans=TextMobject("X = 12")
        trans[0][0].set_color(YELLOW)
        trans.scale(0.8).next_to(e2,DOWN*2)

        self.play(ReplacementTransform(env,trans,run_time=2))

        self.play(FadeOutAndShift(e1,UP),FadeOutAndShift(e2,UP))

        self.play(trans.shift,UP*1.6)

        et1=TextMobject("由于每个顶点为两个六边形、一个五边形共有")
        et1[0][9:12].set_color(BLUE)
        et1[0][15:18].set_color(YELLOW)
        et1.scale(0.8).next_to(trans,DOWN*2)
        et2=TextMobject("故每个五边形邻接五个六边形")
        et2[0][3:6].set_color(YELLOW)
        et2[0][10::].set_color(BLUE)
        et2.scale(0.8).next_to(et1,DOWN*2)
        et3=TextMobject("每个六边形邻接三个五边形")
        et3[0][2:5].set_color(BLUE)
        et3[0][-3::].set_color(YELLOW)
        et3.scale(0.8).next_to(et2,DOWN*2)
        et4=TexMobject("\\text{即}\\text{Y}=\\frac{5}{3}\\text{X}")
        et4[0][1].set_color(BLUE)
        et4[0][-1].set_color(YELLOW)
        et4.scale(0.8).next_to(et3,DOWN*2)

        self.play(DrawBorderThenFill(et1))
        self.wait(2)
        self.play(DrawBorderThenFill(et2))
        self.wait(2)
        self.play(DrawBorderThenFill(et3))
        self.wait(2)
        self.play(Write(et4))
        self.wait(2)

        twenty=TextMobject("20")
        twenty.scale(0.8).next_to(et4[0][2])

        self.play(ReplacementTransform(et4[0][3::],twenty))

        self.play(FadeOut(et1),FadeOut(et2),FadeOut(et3),FadeOut(et4[0][0]))
        self.play(FadeOut(en1),FadeOut(en2),FadeOut(en3))
        self.play(trans.scale,5/8,trans.to_edge,LEFT,trans.shift,DOWN)
        kk=VGroup(et4[0][1:3],twenty)
        self.play(kk.scale,5/8,kk.next_to,trans,DOWN*2)

        eenn=TexMobject("\\text{V足球}=\\text{X}\\text{V}5+\\text{Y}\\text{V}6")
        eenn[0][1:3].scale(0.7).shift(LEFT*0.2+DOWN*0.2)
        eenn[0][6].scale(0.7).shift(DOWN*0.2)
        eenn[0][-1].scale(0.7).shift(DOWN*0.2)
        eenn[0][4:7].set_color(YELLOW)
        eenn[0][8::].set_color(BLUE)
        eenn.scale(0.8)

        transf=TexMobject("\\frac{125+43\\sqrt{5}}{4}")
        transf.scale(0.8).next_to(eenn[0][3])

        self.play(DrawBorderThenFill(eenn,run_time=2))
        self.wait(3)
        self.play(ReplacementTransform(eenn[0][4::],transf,run_time=2))

        self.play(FadeOut(trans),FadeOut(kk),FadeOut(bigv5),FadeOut(bigv6))
        self.play(FadeOut(method4))
        self.play(FadeOut(eenn[0][0:4]))
        self.play(transf.move_to,ORIGIN,transf.scale,2)
        self.play(transf.set_color,GOLD,run_time=2)
        self.play(VFadeOut(transf,run_time=2))
        self.wait(2)
                  


        
                  
        
        
        
        
        

        
        
        
        

        
        
        
        
        
        

        

        
       

        
        
        

        
        
        
        
        

        

        

        
        

        

        
            
