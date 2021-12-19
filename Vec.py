import math


class Vec:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, n: float) -> 'Vec':
        return Vec(self.x * n, self.y * n, self.z * n)

    # Dot product
    def __mod__(self, other: 'Vec'):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self) -> float:
        return math.sqrt(self % self)

    # Divide the vector by its length and get a vector with the same “direction”
    #   but the length of 1, known as a unit vector
    def unit(self) -> 'Vec':
        return Vec(self.x, self.y, self.z) * (1 / self.length())

pass
