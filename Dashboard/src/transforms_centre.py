# -----------------------------------------------------------------------------
# transforms_centre.py
# -----------------------------------------------------------------------------
# Maps Farey fractions to grid coordinates, generating mirroed points, and 
# sorting points by Euclidean distance.
# 
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.
# -----------------------------------------------------------------------------

import numpy as np

def farey_to_grid(sequence):
    """Map Farey fractions (a/b) to coordinates (b, a)."""
    return [(frac.denominator, frac.numerator) for frac in sequence]

def generate_full_plane(grid_points, N):
    """Reflect and mirror points across axes to cover all quadrants."""
    full_points = []
    center = N // 2  # middle of the square

    for (b, a) in grid_points:
        # generate reflections
        variants = [(b, a), (b, -a), (-b, a), (-b, -a)]
        for x, y in variants:
            # shift so origin maps to the middle of the square
            new_x = (x + center) % N
            new_y = (y + center) % N
            full_points.append((new_x, new_y))

    return full_points

def sort_points_by_distance(points):
    """Sort points by Euclidean distance from origin."""
    return sorted(points, key=lambda x: np.sqrt(x[0]**2 + x[1]**2))

