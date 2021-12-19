import Sphere


class World:
    def __init__(self, spheres: list[Sphere], lights: list[Sphere]):
        self.spheres = spheres
        self.lights = lights
