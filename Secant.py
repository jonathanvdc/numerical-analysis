from Polynomial import *

def secant(poly, x0, x1, n):
    x_prev = x0
    x_cur = x1

    y_prev = poly.get(x_prev)
    y_cur = poly.get(x_cur)

    for i in range(n):
        dx = x_cur - x_prev
        dy = y_cur - y_prev

        if dx == 0:
            return i + 1, x_cur

        dfx = dy / dx

        (x_prev, x_cur) = (x_cur, x_cur - y_cur / dfx)

        # Update y values
        (y_prev, y_cur) = (y_cur, poly.get(x_cur))

    return n, x_cur

print(secant(Polynomial([1, 4, 0, -10]), 0.0, 1.0, 20))
