# -----------------------------------------------------------------------------
# farey.py
# -----------------------------------------------------------------------------
# Function for generating Farey sequences of order N.
#
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.

from fractions import Fraction

def farey_sequence(N):
    """Generates a Farey sequence of order N."""
    sequence = [Fraction(0, 1), Fraction(1, 1)]
    a1, b1 = 0, 1
    a2, b2 = 1, 1

    while b2 <= N:
        a3, b3 = a1 + a2, b1 + b2
        if b3 > N:
            break
        sequence.append(Fraction(a3, b3))

        if b1 + b2 > N:
            break
        if a3 / b3 < 1:
            a1, b1 = a3, b3
        else:
            a2, b2 = a3, b3

    return sequence

