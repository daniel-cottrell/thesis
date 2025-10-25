# -----------------------------------------------------------------------------
# metrics.py
# -----------------------------------------------------------------------------
# Mathematical metrics for Farey-based fractals:
#   - Box-counting fractal dimension
#   - Hausdorff distance between two fractals
#
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.
# -----------------------------------------------------------------------------

import numpy as np
from scipy.spatial.distance import cdist
from math import log2

# Fractal Dimension
def fractal_dimension(points, box_sizes=None):
    """Estimates the fractal dimension using box-counting."""
    if not points:
        return 0.0
    
    pts = np.array(points)
    N = max(pts.max(), abs(pts.min()))

    if box_sizes is None:
        box_sizes = [2 ** k for k in range(1, int(log2(N)) + 1)]

    counts = []
    for size in box_sizes:
        # Place points into grid of "boxes"
        grid = np.floor(pts / size).astype(int)
        unique_boxes = {tuple(g) for g in grid}
        counts.append(len(unique_boxes))

    logsizes = -np.log(box_sizes)
    logcounts = np.log(counts)

    # Linear regression slope
    coeffs = np.polyfit(logsizes, logcounts, 1)
    return coeffs[0]


# Hausdorff Distance
def fractal_distance(points1, points2):
    """Computes the distance between two fractals."""

    if not points1 or not points2:
        return float("inf")
    
    A = np.array(points1)
    B = np.array(points2)

    d_AB = np.max(np.min(cdist(A, B), axis=1))
    d_BA = np.max(np.min(cdist(B, A), axis=1))
    return max(d_AB, d_BA)
    




