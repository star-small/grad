import math

import pyglet
from pyglet import shapes


class Vector:
    origin = [0, 0]
    color = (0, 0, 255)

    def __init__(self, val: list):
        self.val = val

    def set_color(self, color):
        self.color = color

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

    def copy(self):
        return Vector(self.val)


class Axis:
    def __init__(self, window, batch):
        self.batch = batch
        self.window = window

    def draw_axis(self, size):
        self.center = (size[0]/2, size[1]/2)

        self.x_axis = shapes.Line(0, self.center[1], size[0], self.center[1],
                                  color=(255, 255, 255), batch=self.batch)
        self.y_axis = shapes.Line(self.center[0], 0, self.center[0], size[1],
                                  color=(255, 255, 255), batch=self.batch)

        # @self.window.event
        # def on_draw():
        self.window.clear()
        self.batch.draw()

    def get_center(self):
        return self.center


v3 = Vector([-20, 100])


class Plot:

    def __init__(self):
        self.size = [600, 600]
        self.window = pyglet.window.Window(self.size[0], self.size[1])
        self.batch = pyglet.graphics.Batch()
        axis = Axis(self.window, self.batch)
        axis.draw_axis(self.size)
        self.center = axis.get_center()

    def plot(self, vector):
        self.display = shapes.Line(self.center[0]+vector.origin[0], self.center[1]+vector.origin[1], self.center[0] +
                                   vector.val[0]+vector.origin[0], self.center[1]+vector.val[1]+vector.origin[1], width=3, color=vector.color, batch=self.batch)
        self.display.draw()
        # self.display.delete()

    # def put_vector(self):
    #     self.vec = shapes.Line(self.center[0]+self.origin[0], self.center[1]+self.origin[1], self.center[0] + 100, self.center[1]+100, width=3,
    #                            color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), batch=self.batch)

    def show(self):
        pyglet.app.run()
        print('rwf')

        pyglet.app.exit()
