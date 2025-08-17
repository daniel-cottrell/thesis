# -----------------------------------------------------------------------------
# plotting.py
# -----------------------------------------------------------------------------
# Function for plotting fractal points using matplotlib.
# 
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt

def plot_fractal(points, N, K):
    """Plot fractal using scatter plot."""
    x_vals, y_vals = zip(*points)
    plt.figure(figsize=(8, 8))
    plt.scatter(x_vals, y_vals, s=0.5, color='black')
    plt.title(f"Fractal for N = {N}, K = {K}")
    plt.axis('equal')
    plt.show()

