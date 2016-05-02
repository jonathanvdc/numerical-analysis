from Polynomial import *

def newton(poly, x0, n):
    x = x0
    deriv = poly.derive()

    for i in range(n):
        fx = poly(x)
        dfx = deriv(x)

        x = x - fx / dfx

    return n, x

print(newton(Polynomial([1, 4, 0, -10]), 1.5, 20))
