import streamlit as st
import plotly.graph_objects as go
from mesh_processing.mesh_loader import load_obj_mesh
from mesh_processing.geodesic_distances import compute_sum_of_distances
from mesh_processing.visualization import plot_bipolar_contours

# Function to visualize the mesh with geodesic distances
def visualize_mesh(vertices, faces, sum_distances, seeds, target_distances):
    fig = plot_bipolar_contours(vertices, faces, sum_distances, seeds, target_distances, tolerance=0.85)
    return fig

# Streamlit app starts here
st.title("3D Mesh Visualization with Geodesic Distances")

# Set file path (this can be dynamically replaced with an uploaded file)
filepath = './F0001_AN01WH_F3Dsur.obj'  # Replace with your path or allow user to upload
mesh_file = filepath  # You can replace this with Streamlit file uploader logic if needed

if mesh_file is not None:
    # Load the mesh from the file
    vertices, faces = load_obj_mesh(mesh_file)

    # Allow user input for seed points (indices of the mesh vertices)
    seed_input = st.text_input("Enter seed points (comma-separated, e.g., 13714,22526,22229)", "13714,22526,22229")
    seeds = list(map(int, seed_input.split(",")))

    # Compute sum of geodesic distances from seed points
    sum_distances = compute_sum_of_distances(vertices, faces, *seeds)

    # Define target distances for the bipolar contours
    target_distances = [200, 250, 300, 400, 450, 500, 550, 600]

    # Visualize the mesh with the computed geodesic contours
    fig = visualize_mesh(vertices, faces, sum_distances, seeds, target_distances)
    
    # Display the Plotly figure in the Streamlit app
    st.plotly_chart(fig)
