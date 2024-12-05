import streamlit as st
import plotly.graph_objects as go
from mesh_processing.mesh_loader import load_obj_mesh
from mesh_processing.geodesic_distances import compute_sum_of_distances
from mesh_processing.visualization import plot_bipolar_contours

def visualize_mesh(vertices, faces, sum_distances, seeds, target_distances):
    fig = plot_bipolar_contours(vertices, faces, sum_distances, seeds, target_distances, tolerance=0.85)
    return fig

# Streamlit app starts here
st.title("Représentation Tripolaire Equivariante")

# Allow the user to upload an OBJ file
mesh_file = st.file_uploader("Télécharger votre maillage", type="obj")

# Proceed only if a file is uploaded
if mesh_file is not None:
    # Load the mesh from the uploaded file
    vertices, faces = load_obj_mesh(mesh_file)

    # Input seed points (indices of the mesh vertices)
    seed_input = st.text_input("Les indices des points de référence (e.g., 13714,22526,22229)", "13714,22526,22229")
    seeds = list(map(int, seed_input.split(",")))

    # Compute sum of distances (geodesic calculation)
    sum_distances = compute_sum_of_distances(vertices, faces, *seeds)

    target_distances_input = st.text_input("Les distances cibles pour les contours bipolaires (e.g., 200,250,300)", "200,250,300,400,450")
    target_distances = list(map(int, target_distances_input.split(",")))

    # Visualize the 3D mesh with geodesic contours
    fig = visualize_mesh(vertices, faces, sum_distances, seeds, target_distances)

    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig)
