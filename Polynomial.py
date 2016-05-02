
class Polynomial:
    def __init__(this, coefficients):
        this.c = coefficients

    def get(this, x):
        y = 0
        for z in this.c:
            y *= x
            y += z
        return y

    __call__ = get

    def derive(this):
        length = len(this.c)
        derivPoly = [this.c[i] * (length - i - 1) for i in range(0, length - 1)]
        return Polynomial(derivPoly)

    def __eq__(this, other):
        return this.c == other.c

    def __ne__(this, other):
        return this.c != other.c

# Unit tests
poly = Polynomial([1, 1, 4])
assert(poly.get(1) == 1 + 1 + 4)
assert(poly.get(2) == 4 + 2 + 4)
assert(poly.derive() == Polynomial([2, 1]))
assert(Polynomial([1, 1, 2, 4]).derive() == Polynomial([3, 2, 2]))
assert(Polynomial([1, 4, 0, -10]).derive() == Polynomial([3, 8, 0]))
