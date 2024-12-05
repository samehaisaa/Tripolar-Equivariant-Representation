from mesh_processing.mesh_loader import load_obj_mesh
from mesh_processing.geodesic_distances import compute_sum_of_distances
from mesh_processing.visualization import plot_bipolar_contours

filepath = './F0001_AN01WH_F3Dsur.obj'  # Replace with your path
vertices, faces = load_obj_mesh(filepath)

seeds = [13714, 22526, 22229]
sum_distances = compute_sum_of_distances(vertices, faces, *seeds)

target_distances = [200, 250, 300, 400, 450, 500, 550, 600]
plot_bipolar_contours(vertices, faces, sum_distances, seeds, target_distances, tolerance=0.7)
