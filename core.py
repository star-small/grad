import math

import pyglet
from pyglet import shapes
import random


class Vector:
    origin = [0, 0]

    def __init__(self, val: list):
        self.val = val
        vectors.add_vector(self)

    def set_origin(self, origin):
        self.origin = origin

    def __add__(self, Vec2):
        return Vector([self.val[i] + Vec2.val[i] for i in range(len(Vec2.val))])

    def __mul__(self, number: int):
        return Vector([number*i for i in self.val])

    def __div__(self, number: int):
        return Vector([number/i for i in self.val])

    def dot_product(self, vec):
        return sum([vec.val[i]*self.val[i] for i in range(len(vec.val))])

    def get_length(self):
        return math.sqrt(sum([i*i for i in self.val]))

    def get_cos(self, vec):
        return (self.dot_product(vec))/(vec.get_length() * self.get_length())

    def __repr__(self):
        return f"Vector: {self.val}"


class Vectors:
    def __init__(self):
        self.value = []

    def add_vector(self, vector):
        self.value.append(vector)


class Plot:
    def __init__(self, size=(600, 600)):
        self.window = pyglet.window.Window(size[0], size[1])
        self.center = (size[0]/2, size[1]/2)
        self.batch = pyglet.graphics.Batch()

        self.x_axis = shapes.Line(0, self.center[1], size[0], self.center[1],
                                  color=(255, 255, 255), batch=self.batch)
        self.y_axis = shapes.Line(self.center[0], 0, self.center[0], size[1],
                                  color=(255, 255, 255), batch=self.batch)
        self.shape_list = []
        for vector in vectors.value:
            print(vector.val)
            temp = shapes.Line(self.center[0], self.center[1], self.center[0] + vector.val[0], self.center[1]+vector.val[1], width=3, color=(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.shape_list.append(temp)

        @self.window.event
        def on_draw():
            self.window.clear()
            self.batch.draw()
            print(self.shape_list)
            for i in self.shape_list:
                print(i)
                i.draw()

    def put_vector(self):
        self.vec = shapes.Line(self.center[0], self.center[1], self.center[0] + 100, self.center[1]+100, width=3,
                               color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), batch=self.batch)

    def show(self):
        pyglet.app.run()


vectors = Vectors()
