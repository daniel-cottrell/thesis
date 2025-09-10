# -----------------------------------------------------------------------------
# intersection.py
# -----------------------------------------------------------------------------
# Implements an equality check between sets of points, using a tolerance value.
# 
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.
# -----------------------------------------------------------------------------

def intersect_points(points1, points2, tol=1):
    """Find approximate intersection of two sets of points."""
    set1 = { (round(x, tol), round(y, tol)) for x, y in points1 }
    set2 = { (round(x, tol), round(y, tol)) for x, y in points2 }
    
    return list(set1 & set2)

def difference_points(points1, points2, tol=1):
    """Find approximate difference of two sets of points by rounding."""
    set1 = { (round(x, tol), round(y, tol)) for x, y in points1 }
    set2 = { (round(x, tol), round(y, tol)) for x, y in points2 }
    diff = set1 - set2
    
    return list(diff)

