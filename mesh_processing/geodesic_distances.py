import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from tqdm import tqdm

def compute_geodesic_distances(vertices, faces, seed_index):
    """Computes geodesic distances from a seed vertex."""
    rows, cols, data = [], [], []

    for face in tqdm(faces, desc="Building Graph"):
        for i in range(3):
            for j in range(i + 1, 3):
                vi, vj = face[i], face[j]
                dist = np.linalg.norm(vertices[vi] - vertices[vj])

                rows.extend([vi, vj])
                cols.extend([vj, vi])
                data.extend([dist, dist])

    num_vertices = len(vertices)
    graph = csr_matrix((data, (rows, cols)), shape=(num_vertices, num_vertices))
    distances, _ = dijkstra(csgraph=graph, directed=False, indices=seed_index, return_predecessors=True)
    return distances

def compute_sum_of_distances(vertices, faces, seed1, seed2, seed3):
    """Computes the sum of geodesic distances to multiple seeds."""
    dist1 = compute_geodesic_distances(vertices, faces, seed1)
    dist2 = compute_geodesic_distances(vertices, faces, seed2)
    dist3 = compute_geodesic_distances(vertices, faces, seed3)
    return dist1 + dist2 + dist3

def compute_diff_of_distances(vertices, faces, seed1, seed2, seed3):
    """Computes the sum of geodesic distances to multiple seeds."""
    dist1 = compute_geodesic_distances(vertices, faces, seed1)
    dist2 = compute_geodesic_distances(vertices, faces, seed2)
    dist3 = compute_geodesic_distances(vertices, faces, seed3)
    return np.abs((dist1 - ((dist2 + dist3) )))

