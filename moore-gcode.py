#!/usr/bin/python
from itertools import chain
from math import sin,cos,pi
import sys

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

seq=L_sys(axiom,5)

direction = 0.0
theta = (pi/2)
location = (0.0,0.0)
side = 3.125
bit = 0.125

def move(pos,angle,distance):
    nx = pos[0] + sin(angle)*distance
    ny = pos[1] + cos(angle)*distance
    return (nx,ny)

xmin = 0
xmax = 0
distance = 1.0

for e in seq:
    if e == 'F':
        nl = move(location, direction, distance)
        location = nl
        if location[0] < xmin:
            xmin = location[0]
        if location[0] > xmax:
            xmax = location[0]
    elif e == '+':
        direction = direction + theta
    elif e == '-':
        direction = direction - theta

d = xmax-xmin
distance = 3.128/d
direction = 0.0
theta = (pi/2)
location = (0.0,0.0)

print "distance",distance
millFeed = 10
travelFeed = 10

def gmove(x,y,z):
    global millFeed
    f = millFeed
    return "G1 X{0} Y{1} Z{2} F{3}\n".format(x,y,z,f)

if __name__ == '__main__':
    fname = 'moore.gcode'
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    f = open(fname,'w')
    f.write("G0 X0 Y0 Z0.5 F{0}\n".format(travelFeed))
    for e in seq:
        if e == 'F':
            nl = move(location, direction, distance)
            print location
            f.write(gmove(location[0],location[1],-0.005))
            location = nl
        elif e == '+':
            direction = direction + theta
        elif e == '-':
            direction = direction - theta
    f.write("G0 X{0} Y{1} Z0.5 F{1}\n".format(location[0],location[1],travelFeed))
    f.close()
