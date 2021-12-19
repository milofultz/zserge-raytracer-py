import math
from Vec import Vec


class Sphere:
    def __init__(self, center: Vec, color: float, radius: float):
        self.center = center
        self.radius = radius
        self.color = color  # 0 = black, 1 = white

    def intersect(self, origin: Vec, direction: Vec) -> float:
        p = origin - self.center
        a = direction % direction
        b = 2 * (p % direction)
        c = (p % p) - (self.radius * self.radius)
        d = b * b - 4 * a * c
        if d < 0:
            return float('nan')
        sqd = math.sqrt(d)
        distance = (-b - sqd) / (2 * a)
        if distance > .1:
            return distance
        distance = (-b + sqd) / (2 * a)
        if distance > .1:
            return distance
        return float('nan')
