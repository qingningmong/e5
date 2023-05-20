#!/usr/bin/env python
#encoding:utf-8
#
# [SNIPPET_NAME: tClock]
# [SNIPPET_CATEGORIES: PyTurtle]
# [SNIPPET_DESCRIPTION: Use turtle to draw a clock.]
# [SNIPPET_DOCS: http://docs.python.org/library/turtle.html]
# [SNIPPET_AUTHOR: Grant Bowman <grantbow@ubuntu.com>]
# [SNIPPET_LICENSE: PSF]
# Code authorship from http://python.org/download/releases/2.6.4/
 
"""       turtle-example-suite:
             tdemo_clock.py
Enhanced clock-program, showing date
and time
  ------------------------------------
   Press STOP to exit the program!
  ------------------------------------
"""
from turtle import *
from datetime import datetime
 
mode("logo") # 向上（北），正角度为顺时针
 
thisday = 0
thisecond = 0
 
second_hand = Turtle()
minute_hand = Turtle()
hour_hand = Turtle()
writer = Turtle()
writer.getscreen().bgcolor('gray90')
writer.color("gray20", "gray20")
 
def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()
'''
laenge 指针长度
width 指针宽度
spitze 箭头边长
'''
def hand(laenge, spitze, width):
    lt(90)
    fd(width)
    rt(90)
    fd(laenge*1.15)
    rt(90)
    fd(width * 2)
    rt(90)
    fd(laenge*1.15)
    rt(90)
    fd(width)
    rt(90)
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)
 
def make_hand_shape(name, laenge, spitze, width):
    reset()
    jump(-laenge*0.15) # 指针靠近表盘中心的末端，但不与圆心重合
    begin_poly()
    hand(laenge, spitze, width)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)
 
 
def clockface(radius):
    reset()
    # 外圆周
    pensize(2)
    colors = ['green3', 'green2', 'gray98']
    # 从外向内fill
    for i in range(3):
        jump(radius+7+(2-i)*4,90)
        fillcolor(colors[i])
        begin_fill()
        circle(radius+7+(2-i)*4, steps=1000)
        end_fill()
        jump(-radius-7-(2-i)*4,90)
 
    # 刻度
    pensize(7)
    color("gray60", "gray60")
    # 经验值
    params = [-35, -40, -40, -25, -15, -5, 0, -5, -15, -25, -40, -40] #距离
    angles = [0, -15, -25, -40, -35, -30, 0, 30, 35, 40, 25, 15] # 角度
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(-15)
            # 下面三行写表盘数字
            jump(params[i/5], angles[i/5])
            write(12 if i/5==0 else i/5, align="center", font=("Courier", 20, "bold"))
            jump(params[i/5], 180+angles[i/5])
            jump(-radius+15)
        else:
            dot(3)
            jump(-radius)
        rt(6)
 
 
def setup():
    global second_hand, minute_hand, hour_hand, writer
    # 自定义形状
    make_hand_shape("hour_hand", 90, 25, 5)
    make_hand_shape("minute_hand",  130, 25, 3)
    make_hand_shape("second_hand", 140, 10, 1)
 
    # 画表盘
    clockface(160)
 
    hour_hand.shape("hour_hand")
    hour_hand.color("gray30", "gray12")
 
    minute_hand.shape("minute_hand")
    minute_hand.color("gray40", "blue")
 
    second_hand.shape("second_hand")
    second_hand.color("red4", "red4")
 
    for hand in hour_hand, minute_hand, second_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 1)
        hand.speed(1)
    ht()
 
    writer.ht()
    writer.pu()
    writer.bk(85)
    
def wochentag(t):
    wochentag = ["星期一", "星期二", "星期三","星期四", "星期五", "星期六", "星期日"]
    return wochentag[t.weekday()]
 
def get_mmdd(z):
    m = z.month
    t = z.day
    return "%d月%d日" % (m, t)
 
def get_yyyy(z):
    j = z.year
    return "%d" % (j)
 
def write_date(t):
    global thisday
    x = t.day
    if thisday != x:
        thisday = x
        writer.clear()
        writer.home()
        writer.forward(65)
        writer.write(wochentag(t),
                 align="center", font=("Courier", 16, "bold"))
        writer.back(150)
        writer.write(get_mmdd(t),
                 align="center", font=("Courier", 16, "normal"))
        writer.back(15)
        writer.write(get_yyyy(t),
                 align="center", font=("Courier", 10, "normal"))
        writer.forward(100)
 
def tick():
    global thisecond
    t = datetime.today()
    if thisecond != t.second:
        thisecond = t.second
        #print t
        sekunde = t.second + t.microsecond * 0.000001
        minute = t.minute + sekunde / 60.0
        stunde = t.hour + minute / 60.0
        tracer(False)
        write_date(t)
        tracer(True)
        hour_hand.setheading(30 * stunde)
        minute_hand.setheading(6 * minute)
        second_hand.setheading(6 * sekunde)
    ontimer(tick, 10)
 
def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"
 
if __name__ == "__main__":
    msg = main()
    print msg
    mainloop()