# -----------------------------------------------------------------------------
# criteria.py
# -----------------------------------------------------------------------------
# Implements filtering of points using the Katz criterion.
# 
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.
# -----------------------------------------------------------------------------

import numpy as np

def apply_katz_criterion(points, K):
    """Filter points using Katz criterion with threshold K."""
    max_a = max(abs(a) for _, a in points)
    max_b = max(abs(b) for b, _ in points)
    threshold = max(max_a, max_b) * K

    return [pt for pt in points if np.sqrt(pt[0]**2 + pt[1]**2) <= threshold]

