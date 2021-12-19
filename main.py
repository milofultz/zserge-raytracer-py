from Vec import Vec
from Sphere import Sphere
from World import World
import visuals


world = World(
    [   # Spheres
        Sphere(Vec(0, -1000, 0), 0.001, 1000),  # large dark plane, the ground
        Sphere(Vec(-2, 1, -2), 1, 1),  # white sphere on the left
        Sphere(Vec(0, 1, 0), 0.5, 1),  # grey sphere in the center
        Sphere(Vec(2, 1, -1), 0.1, 1)  # dark sphere on the right
    ],
    [   # Three directional lights of various brightness
        Sphere(Vec(0, 100, 0), .4, 0),
        Sphere(Vec(100, 100, 200), .5, 0),
        Sphere(Vec(-100, 300, 100), .1, 0)
    ]
)


visuals.render(world, 120, 80)
