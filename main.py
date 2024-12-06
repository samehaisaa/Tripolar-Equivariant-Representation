import streamlit as st
import plotly.graph_objects as go
from mesh_processing.mesh_loader import load_obj_mesh
from mesh_processing.geodesic_distances import compute_sum_of_distances
from camera_animation import update_camera_animation
import time
from mesh_processing.geodesic_distances import compute_diff_of_distances

import random

from mesh_processing.visualization import plot_bipolar_contours
random_progress = random.randint(0, 15)

camera = {
    'eye': {'x': 0, 'y': 0, 'z': 2.4},  # Position of the camera
    'up': {'x': 1, 'y': 0, 'z': 0},   # Which direction is 'up'
    'center': {'x': 0, 'y': 0, 'z': 0} # The focus point of the camera
}


def visualize_mesh(vertices, faces, sum_distances,diff_distances, seeds, target_distances_sum,target_distances_diff,tolerance):
    fig = plot_bipolar_contours(vertices, faces, sum_distances,diff_distances, seeds, target_distances_sum,target_distances_diff, tolerance)

    return fig

# Streamlit app starts here
st.title("Représentation tripolaire équivariante")



# Allow the user to upload an OBJ file
mesh_file = "./F0001_AN01WH_F3Dsur.obj"
with st.expander("Paramètres des contours",expanded=True):
    target_distances_sum_input = st.text_input(
        "Distances cibles (somme, e.g., 200,275,250,300)", "200,225,250,275,250,300,320"
    )
    target_distances_sum = list(map(int, target_distances_sum_input.split(",")))

    target_distances_diff_input = st.text_input(
        "Distances cibles (différence, e.g., 20,30,45,70,90,110,130,140,160)", "20,30,45,70,90,110,130,140,160"
    )
    target_distances_diff = list(map(int, target_distances_diff_input.split(",")))

    tolerance = st.slider("Tolérance pour les contours", min_value=0.0, max_value=1.0, value=0.85,step=0.01)
loading_message = st.empty()
random_progress = random.randint(0, 15)

loading_message.text("Chargement et traitement du maillage...")

# Proceed only if a file is uploaded
if mesh_file is not None:
    progress_bar = st.progress(random_progress)  # Initialize progress bar
    with st.empty():
        # Simulate processing time (if needed)
        
        loading_message.text("Chargement du maillage ...")  # Update message
        vertices, faces = load_obj_mesh(mesh_file)
	
        progress_bar.progress(25+random_progress)  # Update progress to 20%
        loading_message.text("Extraction des lignes de niveau ...")  # Update message


        seeds = [13714, 22526, 22229]  # Replace with your desired indices
        # Compute sum of distances (geodesic calculation)
        sum_distances = compute_sum_of_distances(vertices, faces, *seeds)
        progress_bar.progress(65+random_progress)
        loading_message.text("Génération des contours ...")

        diff_distances = compute_diff_of_distances(vertices, faces, *seeds)
        # Visualize the 3D mesh with geodesic contours

        fig = visualize_mesh(vertices, faces, sum_distances, diff_distances, seeds, target_distances_sum, target_distances_diff, tolerance)

        fig.update_layout(
            scene_camera=camera,
            scene=dict(
                xaxis=dict(visible=True),
                yaxis=dict(visible=True),
                zaxis=dict(visible=True)
            ),
            dragmode='orbit',
            scene_dragmode="turntable"
        )
        progress_bar.progress(70+random_progress)

        progress_bar.progress(100)
        loading_message.text("Traitement terminé ! Affichage des résultats...")  # Update progress to 100% 
        progress_bar.empty()     
        loading_message.empty()




    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig)
