from math import sqrt


class PizzabotCoordinate:
    def __init__(self, *argv):
        self.points = []
        for arg in argv:
            if isinstance(arg, int):
                self.points.append(arg)
            else:
                raise ValueError(
                    "ValueError exception thrown, non-int passed to PizzabotCoordinate",
                    argv,
                )

    def __len__(self):
        return len(self.points)

    def _check_len(self, other):
        if len(self) != len(other):
            raise TypeError(
                "TypeError exception thrown, PizzabotCoordinate points dimensions do not match",
                self.points,
                other.point,
            )

    def __abs__(self):
        sum_of_squares = 0
        for sp in self.points:
            sum_of_squares += sp * sp
        return sqrt(sum_of_squares)

    def __iadd__(self, other):
        added = []
        self._check_len(other)
        for sp, op in zip(self.points, other.points):
            added.append(sp + op)
        return PizzabotCoordinate(*added)

    def __sub__(self, other):
        delta = []
        self._check_len(other)
        for sp, op in zip(self.points, other.points):
            delta.append(sp - op)
        return PizzabotCoordinate(*delta)

    def __eq__(self, other):
        delta = []
        self._check_len(other)
        for sp, op in zip(self.points, other.points):
            if sp != op:
                return False
        return True
