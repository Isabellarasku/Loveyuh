import cupid
import stddraw
from color import PINK
import math

stddraw.setXscale(-18, 218)
stddraw.setYscale(69, 300)
aditya = cupid.Cupid(100, 100, 0)
arrowSize = math.sin(math.radians(300))


def curve():
    for a in range(200):
        aditya.archback(-1)
        aditya.shootforward(1)


def _heart():
    stddraw.WHITE
    stddraw.setPenColor(PINK)
    stddraw.setPenRadius(6.9)
    aditya.archback(140)
    aditya.shootforward(112)
    curve()
    aditya.archback(120)
    curve()
    aditya.shootforward(112)
    stddraw.text(100, 200, "I love you")
    stddraw.show()


_heart()
