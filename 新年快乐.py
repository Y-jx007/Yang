from manimlib.imports import *

class 新年快乐(ThreeDScene):

    def construct(self):

        bar_1=Prism(dimensions=[1,0.1,0.1])#创建第一个“2”的各笔画
        bar_1.move_to([-3,1,0])
        bar_2=Prism(dimensions=[0.1,1,0.1])
        bar_2.move_to([-2.5,0.5,0])
        bar_3=Prism(dimensions=[1,0.1,0.1])
        bar_3.move_to([-3,0,0])
        bar_4=bar_2.copy().move_to([-3.5,-0.5,0])
        bar_5=bar_1.copy().move_to([-3,-1,0])
        
        first_letter=VGroup(bar_1,bar_2,bar_3,bar_4,bar_5)#包装成一个整体
        
        third_letter=first_letter.copy().move_to([1,0,0])#复制出第二个“2”
        
        letter_two=VGroup(first_letter,third_letter)#两个二包装成一个整体
        
        l=letter_two.copy().set_color(GOLD).scale(2)#为后面变形做准备
        z=letter_two.copy()
        n=VGroup(z[0][2],z[1][2])
        
        self.play(ShowCreation(letter_two))#两个“2”产生的动画
        
        self.play(ApplyMethod(z.move_to,[1,0,0]))#两个“2”复制出四个“2”
        
        for i in n:
            self.play(Rotate(i,angle=PI/2,axis=OUT))#“2”变形为“0”
        m=n.copy()
        zeros=VGroup(m,z)
        self.play(ApplyMethod(m.shift,[-0.5,0.5,0]))
        self.play(ApplyMethod(n.shift,[0.5,-0.5,0]))
        
        zeros=VGroup(m,z)
        zeros_1=VGroup(m[0].copy(),z[0][0:5].copy()).scale(2).move_to([-1,0,0]).set_color(GOLD)#大“0”
        
        self.play(ApplyMethod(letter_two.scale,2))#动画效果
        self.play(Rotate(letter_two),angle=PI,axis=[1,0,1])
        k=letter_two.copy().rotate(angle=PI,axis=[1,0,1])
        self.play(ApplyMethod(k.move_to,[6,0,0]))
        self.play(ApplyMethod(k.set_color,GOLD))
        self.play(ReplacementTransform(letter_two,l))
        self.play(ReplacementTransform(zeros,zeros_1))
        self.wait(2)
        
        
        
        
