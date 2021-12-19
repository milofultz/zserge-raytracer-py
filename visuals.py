import math

from Vec import Vec
from World import World


def trace(world: World, origin: Vec, direction: Vec):
    index = -1
    distance = float('nan')

    for i in range(len(world.spheres)):
        # Loop over every sphere, find nearest non-NAN intersection
        d = world.spheres[i].intersect(origin, direction)
        if not math.isnan(d) and (index < 0 or d < distance):
            distance = d
            index = i

    if index < 0:
        return 0

    p = origin + direction * distance
    n = (p - world.spheres[index].center).unit()
    c = world.spheres[index].color * 0.1
    for light in world.lights:
        l = (light.center - p).unit()
        shadow = 0
        for sphere in world.spheres:
            if not math.isnan(sphere.intersect(p, l)):
                shadow = 1
        if not shadow:
            return world.spheres[index].color

    return c


def render(world: World, width: int, height: int):
    for y in range(height):
        for x in range(width):
            direction = Vec(x - width / 2, height / 2 - y, -height).unit()
            # c would be the color of the pixel
            c = trace(world, Vec(0, 1, 5), direction)
            # find the suitable ASCII symbol "density" from 0 to 10
            pixel = list(" .:-=+*#%@$")[int(c * 10)]
            print(pixel, end='')
        print()
