import trimesh
import numpy as np
import io

def load_obj_mesh(uploaded_file):
    mesh = trimesh.load(uploaded_file)
    # Extract vertices and faces as numpy arrays
    vertices = np.array(mesh.vertices)
    faces = np.array(mesh.faces)

    return vertices, faces
