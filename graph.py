import pyglet
from pyglet import shapes

window = pyglet.window.Window(960, 540)
batch = pyglet.graphics.Batch()

line = shapes.Line(0, 0, 100, 100, width=12,
                   color=(255, 255, 255), batch=batch)


@window.event
def on_draw():
    print("efewfw")
    window.clear()
    batch.draw()


pyglet.app.run()
