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
    if not points:
        return []

    pts = np.asarray(points, dtype=float)
    max_x = np.max(np.abs(pts[:, 0]))
    max_y = np.max(np.abs(pts[:, 1]))
    threshold = max(max_x, max_y) * K

    # Use squared distance to avoid sqrt
    sqd = pts[:, 0]**2 + pts[:, 1]**2
    mask = sqd <= threshold**2
    filtered = pts[mask]
    return [tuple(row) for row in filtered]

