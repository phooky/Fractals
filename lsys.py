#!/usr/bin/python
from itertools import chain
import sdxf
from math import sin,cos,pi

class LSystem:
    def __init__(self, rules, axiom=""):
        self.rules = rules
        self.axiom = axiom
        self.state = axiom

    def reset(self):
        self.state = self.axiom

    def iterate(self, iterations = 1):
        def mapElement(char):
            if self.rules.has_key(char):
                return self.rules[char]
            else:
                return char
        for x in xrange(iterations):
            self.state = ''.join(map(mapElement,self.state))

moore = LSystem({ 'L' : "-RF+LFL+FR-",
                  'R' : "+LF-RFR-FL+" },
                "LFL+F+LFL")
hilbert = LSystem({ 'A' : "-BF+AFA+FB-",
                    'B' : "+AF-BFB-FA+" },
                  "A")
dragon = LSystem({ 'X' : 'X+YF+',
                   'Y' : '-FX-Y' },
                 'FX')

library = {
    "dragon" : dragon,
    "hilbert" : hilbert,
    "moore" : moore
}
