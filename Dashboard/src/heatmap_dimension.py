# -----------------------------------------------------------------------------
# heatmap_dimension.py
# -----------------------------------------------------------------------------
# Generates a heatmap comparing computed and theoretical fractal dimensions
# over ranges of Farey order N and Katz parameter K.
#
# Author: Daniel Cottrell
# Part of the Farey fractal project.
# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from src import fractal_corner, metrics

def theoretical_dimension(N, K):
    """Analytical approximation of fractal dimension from thesis."""
    return 2 - np.log(1 / K) / np.log(N)

def compute_heatmap(N_values, K_values, origin="Corner"):
    """
    Computes fractal dimensions for all combinations of N and K.
    Returns two matrices: computed and theoretical dimensions.
    """
    D_computed = np.zeros((len(K_values), len(N_values)))
    D_theoretical = np.zeros((len(K_values), len(N_values)))

    for i, K in enumerate(K_values):
        for j, N in enumerate(N_values):
            # Generate fractal points
            if origin.lower() == "corner":
                points = fractal_corner.generate_fractal_points(N, K)
            else:
                raise NotImplementedError("Centre-origin heatmap not yet implemented")

            # Compute fractal dimension numerically
            D_computed[i, j] = metrics.fractal_dimension(points)
            # Compute theoretical dimension from approximation
            D_theoretical[i, j] = theoretical_dimension(N, K)

    return D_computed, D_theoretical


def plot_heatmap(N_values, K_values, D_matrix, title, cmap="viridis"):
    """Utility to plot a single heatmap with labeled axes."""
    fig, ax = plt.subplots(figsize=(8, 6))
    c = ax.imshow(D_matrix, origin="lower", aspect="auto",
                  extent=[N_values[0], N_values[-1], K_values[0], K_values[-1]],
                  cmap=cmap)
    fig.colorbar(c, ax=ax, label="Fractal Dimension (D)")
    ax.set_xlabel("Farey Order (N)")
    ax.set_ylabel("Katz Criterion (K)")
    ax.set_title(title)
    return fig


def generate_dimension_heatmaps(N_min=50, N_max=500, N_step=50,
                                K_min=0.1, K_max=1.0, K_step=0.1,
                                origin="Corner"):
    """
    Generate both the computed and theoretical dimension heatmaps,
    plus an error map showing their absolute difference.
    """
    N_values = np.arange(N_min, N_max + 1, N_step)
    K_values = np.arange(K_min, K_max + 1e-9, K_step)

    D_computed, D_theoretical = compute_heatmap(N_values, K_values, origin=origin)
    D_error = np.abs(D_computed - D_theoretical)

    fig1 = plot_heatmap(N_values, K_values, D_computed,
                        "Computed Fractal Dimension (Box-Counting)")
    fig2 = plot_heatmap(N_values, K_values, D_theoretical,
                        "Theoretical Approximation of Fractal Dimension")
    fig3 = plot_heatmap(N_values, K_values, D_error,
                        "Absolute Error |D_computed − D_theoretical|", cmap="plasma")

    return fig1, fig2, fig3
