import pyglet
from pyglet import shapes

window = pyglet.window.Window(width=800, height=600)
rectangle = pyglet.shapes.Rectangle(
    x=50, y=50, width=100, height=50, color=(255, 0, 0))

# Устанавливаем функцию обновления для обновления экрана


def update(dt):
    # Двигаем прямоугольник вправо
    rectangle.x += 5

# Устанавливаем функцию отрисовки


@window.event
def on_draw():
    window.clear()
    rectangle.draw()


# Устанавливаем функцию обновления через каждый кадр
pyglet.clock.schedule_interval(update, 1)

# Запускаем цикл обработки событий
pyglet.app.run()
