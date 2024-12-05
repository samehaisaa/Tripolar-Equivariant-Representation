# tests/test_mesh_loader.py
from src.mesh_loader import load_obj_mesh
import os

def test_load_obj_mesh():
    filepath = './data/sample.obj'
    assert os.path.exists(filepath), "Sample .obj file does not exist"
    vertices, faces = load_obj_mesh(filepath)
    assert vertices.shape[1] == 3, "Vertices should have 3 coordinates"
    assert faces.shape[1] == 3, "Faces should have 3 indices"
