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
    x_vals, y_vals = zip(*points) if points else ([], [])
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(x_vals, y_vals, s=0.5, color='black')
    ax.set_title(f"Fractal for N = {N}, K = {K}")
    ax.axis('equal')
    return fig

