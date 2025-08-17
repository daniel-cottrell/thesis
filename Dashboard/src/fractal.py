# -----------------------------------------------------------------------------
# fractal.py
# -----------------------------------------------------------------------------
# Main fractal generation pipeline:
# - Build Farey sequence
# - Map fractions to grid
# - Generate full plane
# - Apply Katz criterion
# - Map points to periodic lines
# 
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.
# -----------------------------------------------------------------------------

from src import farey, transforms, criteria, plotting

def map_to_periodic_lines(points, N):
    """Map points to periodic lines modulo N."""
    periodic_points = []
    for b, a in points:
        for i in range(N):
            periodic_points.append(((b * i) % N, (a * i) % N))
    
    return periodic_points

def generate_fractal_points(N, K):
    """Full pipeline to generate fractal points."""
    farey_seq = farey.farey_sequence(N)
    grid_points = transforms.farey_to_grid(farey_seq)
    full_points = transforms.generate_full_plane(grid_points, N)
    sorted_points = transforms.sort_points_by_distance(full_points)
    selected_points = criteria.apply_katz_criterion(sorted_points, K)

    return map_to_periodic_lines(selected_points, N)

