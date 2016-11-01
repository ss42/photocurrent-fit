

# Implementation of what was in the handout on 2x2 matrix inversion is needed.

# The reason is that Newton's method in two dimensions involves inverting a
# 2x2 Hessian.


def invert_2x2(a, b, c, d):
    # DUMMY IMPLEMENTATION
    ax = d
    bx = -b
    cx = -c
    dx = a
    divide = 1/(a*d - b*c)

    return divide * d, divide * (-b), divide * (-c), divide * a
