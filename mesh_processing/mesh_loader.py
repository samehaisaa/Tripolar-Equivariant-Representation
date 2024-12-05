import trimesh
import numpy as np

def load_obj_mesh(filepath):
    """Loads a .obj file and extracts vertices and faces."""
    mesh = trimesh.load(filepath)
    vertices = np.array(mesh.vertices)
    faces = np.array(mesh.faces)
    return vertices, faces
