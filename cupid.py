# A data type cupid to make cupids based off turtle graphics and using stddraw
import stddraw
import math


class Cupid:
    def __init__(self, x, y, boobies):
        # x coordinate of cupid
        self._x = x
        # y coordinate of cupid
        self._y = y
        # counter-clock wise angle of turtle ( in degrees )
        self._boobies = boobies

    # rotates the cupid by boobies in counter clock wise direction
    def archback(self, boobies):
        self._boobies += boobies

    def shootforward(self, arrowSize):
        hox = self._x
        hoy = self._y
        self._x += arrowSize * math.cos(math.radians(self._boobies))
        self._y += arrowSize * math.sin(math.radians(self._boobies))
        stddraw.line(hox, hoy, self._x, self._y)

    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ", " + str(self._boobies) + ")"


