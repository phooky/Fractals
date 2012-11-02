#!/usr/bin/python
from itertools import chain
import sdxf
from math import sin,cos,pi

axiom = list("LFL+F+LFL")

rules = { 'L' : list("-RF+LFL+FR-"),
          'R' : list("+LF-RFR-FL+") }

def L_repl(c):
    global rules
    if rules.has_key(c):
        return rules[c]
    return [c]

def L_iter(system):
    a = map(L_repl,system)
    return list(chain.from_iterable(a))

def L_sys(system,depth):
    l = axiom
    for i in range(depth):
        l = L_iter(l)
    return l

seq=L_sys(axiom,4)

direction = 0.0
theta = (pi/2)
distance = 1.5
location = (0.0,0.0)

def move(pos,angle,distance):
    nx = pos[0] + sin(angle)*distance
    ny = pos[1] + cos(angle)*distance
    return (nx,ny)

d=sdxf.Drawing()
d.layers.append(sdxf.Layer(name='MOORE'))
for e in seq:
    if e == 'F':
        nl = move(location, direction, distance)
        d.append(sdxf.Line(points=[location,nl],layer='MOORE'))
        location = nl
    elif e == '+':
        direction = direction + theta
    elif e == '-':
        direction = direction - theta

d.saveas("moore.dxf")
