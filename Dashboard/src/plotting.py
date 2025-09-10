# -----------------------------------------------------------------------------
# plotting.py
# -----------------------------------------------------------------------------
# Function for plotting fractal points using matplotlib.
# 
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

def plot_fractal(points, N, K, point_size=0.5, origin="corner"):
    """Plot fractal using scatter plot."""
    x_vals, y_vals = zip(*points) if points else ([], [])
    fig, ax = plt.subplots(figsize=(8, 8))
    scatter = ax.scatter(
        x_vals, y_vals,
        s=point_size, marker="o",
        color='black'
    )
    ax.set_title(f"Fractal for N = {N}, K = {K}, origin={origin}")
    ax.set_aspect("equal")

    return fig

