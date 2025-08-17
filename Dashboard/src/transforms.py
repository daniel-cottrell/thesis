# -----------------------------------------------------------------------------
# transforms.py
# -----------------------------------------------------------------------------
# Maps Farey fractions to grid coordinates, generating mirroed points, and 
# sorting points by Euclidean distance.
# 
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.

import numpy as np

def farey_to_grid(sequence):
    """Map Farey fractions (a/b) to coordinates (b, a)."""
    return [(frac.denominator, frac.numerator) for frac in sequence]

def generate_full_plane(grid_points, N):
    """Reflect and mirror points across axes to cover all quadrants."""
    full_points = []
    
    for (b, a) in grid_points:
        full_points.extend([(b, a), (b, -a), (-b, a), (-b, -a)])

    return [(b % N, a % N) for b, a in full_points]

def sort_points_by_distance(points):
    """Sort points by Euclidean distance from origin."""
    return sorted(points, key=lambda x: np.sqrt(x[0]**2 + x[1]**2))


