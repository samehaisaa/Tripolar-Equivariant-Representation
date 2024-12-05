import trimesh
import numpy as np
import io

def load_obj_mesh(uploaded_file):
    """Loads a .obj file from an uploaded file object and extracts vertices and faces."""
    # Read the uploaded file as a binary stream
    file_bytes = uploaded_file.read()

    # Use io.BytesIO to treat the binary data as a file object
    file_like = io.BytesIO(file_bytes)
    
    # Load the mesh from the file-like object
    mesh = trimesh.load(file_like, file_type='obj')
    # Extract vertices and faces as numpy arrays
    vertices = np.array(mesh.vertices)
    faces = np.array(mesh.faces)

    return vertices, faces
