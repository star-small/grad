import random
from core import Vector
from core import Plot
v1 = Vector([random.randint(-250, 250), random.randint(-250, 250)])
v2 = Vector([-20, 100])
v3 = v1+v2
v3.set_color([255, 0, 0])


plt = Plot()

plt.plot(v1)


plt.plot(v2)
plt.plot(v3)


plt.show()
# how the aniation should work?
# v1 = Vector(...)
# v2 = Vector(...)
# plt = Plot()
# while True:
#   plot(v1)
#   plot(v2)
#   plt.show()
