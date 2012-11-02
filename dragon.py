#!/usr/bin/python

import sdxf
from math import sqrt, sin, cos, pi

iterations = 11

def move(pos,angle,distance):
    nx = pos[0] + sin(angle)*distance
    ny = pos[1] + cos(angle)*distance
    return (nx,ny)

def flipElement(c):
    if (c == 'L'): return 'R'
    else: return 'L'

def generateTurns(iterations):
    if (iterations == 0):
        return ['R']
    else:
        i = generateTurns(iterations-1)
        j = i + ['R']
        i.reverse()
        j = j + map(flipElement,i)
        return j

turns = generateTurns(iterations)
direction = -pi/4
distance = 1.0
cutoff = 0.78
location = (0,0)
left = pi/2

def doTurn(direction,whichway,amount):
    if whichway == 'L':
        direction = direction + amount
    else:
        direction = direction - amount
    return direction

d=sdxf.Drawing()
d.layers.append(sdxf.Layer(name='DRAGON'))
for turn in turns:
    nl = move(location,direction,distance*cutoff)
    d.append(sdxf.Line(points=[location,nl],layer='DRAGON'))
    location = nl
    direction = doTurn(direction,turn,pi/4)

    nl = move(location,direction,distance*(1.0-cutoff))
    d.append(sdxf.Line(points=[location,nl],layer='DRAGON'))
    location = nl
    direction = doTurn(direction,turn,pi/4)

d.saveas("dragon.dxf")
