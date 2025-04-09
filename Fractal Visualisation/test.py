# Beginning code for fractal visualisations.
# By Daniel Cottrell

import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# Generate the Farey sequence of order N
def farey_sequence(N):
    # Start with the first two fractions: 0/1 and 1/1
    sequence = [Fraction(0, 1), Fraction(1, 1)]
    a1, b1 = 0, 1
    a2, b2 = 1, 1
    
    
    # Generate the Farey sequence
    while b2 <= N:
        a3 = a1 + a2
        b3 = b1 + b2
        if b3 > N:
            break
        sequence.append(Fraction(a3, b3))
        
        # Move to the next mediant
        if b1 + b2 > N:
            break
        if a3/b3 < 1:
            a1, b1 = a3, b3
        else:
            a2, b2 = a3, b3

    return sequence

# Map Farey fractions (a/b) to grid coordinates (b, a)
def farey_to_grid(sequence):
    grid_points = []
    for frac in sequence:
        a = frac.numerator
        b = frac.denominator
        grid_points.append((b, a))
    return grid_points

# Flip and mirror points to cover the entire grid
def generate_full_plane(grid_points, N):
    full_points = []
    for (b, a) in grid_points:
        full_points.append((b, a))  # First octant
        full_points.append((b, -a))  # Reflect along horizontal axis
        full_points.append((-b, a))  # Reflect along vertical axis
        full_points.append((-b, -a))  # Reflect along both axes

    # Ensure the points are within bounds of the grid
    full_points = [(b % N, a % N) for b, a in full_points]

    return full_points

# Sort points by their Euclidean distance (L2 norm)
def sort_points_by_distance(points):
    return sorted(points, key=lambda x: np.sqrt(x[0]**2 + x[1]**2))

# Apply the Katz criterion to select points
def apply_katz_criterion(points, N, K=0.1):
    # Compute Katz criterion based on max absolute values of coordinates
    max_a = max(abs(a) for _, a in points)
    max_b = max(abs(b) for b, _ in points)
    
    # Katz criterion to decide the number of points to select
    threshold = max(max_a, max_b) * K
    selected_points = [pt for pt in points if np.sqrt(pt[0]**2 + pt[1]**2) <= threshold]

    return selected_points

# Map points to periodic lines modulo N
def map_to_periodic_lines(points, N):
    periodic_points = []
    for b, a in points:
        for i in range(N):
            periodic_points.append(((b * i) % N, (a * i) % N))
    return periodic_points

# Plot the fractal
def plot_fractal(N, K=0.1):
    # Generate Farey sequence
    farey_seq = farey_sequence(N)
    
    # Map the fractions to grid coordinates
    grid_points = farey_to_grid(farey_seq)
    
    # Generate the full plane by mirroring and flipping
    full_points = generate_full_plane(grid_points, N)
    
    # Sort points by distance from origin
    sorted_points = sort_points_by_distance(full_points)
    
    # Apply Katz criterion to determine number of points to keep
    selected_points = apply_katz_criterion(sorted_points, N, K)
    
    # Map points to periodic lines
    periodic_points = map_to_periodic_lines(selected_points, N)
    
    # Extract x and y coordinates for plotting
    x_vals, y_vals = zip(*periodic_points)
    
    # Plot the points
    plt.figure(figsize=(8, 8))
    plt.scatter(x_vals, y_vals, s=0.5, color='black')
    plt.title(f"Fractal for N = {N}, K = {K}")
    plt.axis('equal')

    plt.show()


N = 257

plot_fractal(N, K=0.01)
plot_fractal(N, K=0.1)
plot_fractal(N, K=0.2)
plot_fractal(N, K=0.3)
plot_fractal(N, K=0.4)
plot_fractal(N, K=0.5)
