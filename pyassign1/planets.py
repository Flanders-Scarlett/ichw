#!/usr/bin/env python3
"""planets.py: The approximate orbits of the planets in the solar system
__author__ = "Fu Yixuan"
__pkuid__  = "1800011720"
__email__  = "FuYixuan@pku.edu.cn"
"""
import turtle
import math


def orbit(p,o,r,t):   #轨道函数
    x=r*math.cos(math.radians(o))
    y=r*t*math.sin(math.radians(o))
    p.goto(x,y)          

def main():
    colors=['red',  'blue', 'green', 'orange',
            'purple',  'gray', 'brown', 'sea green']

    a=turtle.Turtle()
    b=turtle.Turtle()
    c=turtle.Turtle()
    d=turtle.Turtle()
    e=turtle.Turtle()
    f=turtle.Turtle()
    g=turtle.Turtle()

    a.up()
    a.fd(16)
    a.down()
    a.pensize(40)
    a.shape('circle')
    a.color('yellow')    #太阳的位置

    b.up()
    b.shape('circle')
    b.fd(40)
    b.pen(fillcolor=colors[1], pencolor=colors[1], pensize=2)
    b.down()
    
    c.up()
    c.shape('circle')
    c.fd(80)
    c.pen(fillcolor=colors[2], pencolor=colors[2], pensize=2)
    c.down()
    
    d.up()
    d.shape('circle')
    d.pen(fillcolor=colors[3], pencolor=colors[3], pensize=2)
    d.fd(120)
    d.down()
    
    e.up()
    e.shape('circle')
    e.fd(160)
    e.pen(fillcolor=colors[4], pencolor=colors[4], pensize=2)
    e.down()
    
    f.up()
    f.shape('circle')
    f.fd(200)
    f.pen(fillcolor=colors[5], pencolor=colors[5], pensize=2)
    f.down()
    
    g.up()
    g.shape('circle')
    g.pen(fillcolor=colors[6], pencolor=colors[6], pensize=2)
    g.fd(240)
    g.down()

    for o in range(1,36001):                
        orbit(b,10*o,40,0.83)
        orbit(c,8*o,80,0.87)
        orbit(d,6*o,120,0.79)
        orbit(e,4*o,160,0.75) 
        orbit(f,2*o,200,0.93)
        orbit(g,o,240,1)
        
if __name__ == '__main__':
    main()        

