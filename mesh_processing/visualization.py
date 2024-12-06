import plotly.graph_objs as go
import numpy as np

def plot_bipolar_contours(vertices, faces, sum_distances,diff_distances, seeds, target_distances_sum,target_distances_diff, tolerance):
    """Plots the mesh and contours."""
    x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
    mesh3d = go.Mesh3d(
        x=x, y=y, z=z,
        i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
        intensity=sum_distances,
        colorscale='Viridis',
        showscale=False,
        opacity=0.8,showlegend=False
    )
    seed_markers = [
        go.Scatter3d(
            x=[vertices[seed][0]], y=[vertices[seed][1]], z=[vertices[seed][2]],
            mode='markers',
            marker=dict(size=6, color='blue', symbol='circle'),
            name=f"Seed Point {i+1}",showlegend=False
        )
        for i, seed in enumerate(seeds)
    ]

    contours = []
    for target in target_distances_sum:
        selected = np.where(np.isclose(sum_distances, target, atol=tolerance))[0]
        selected_vertices = vertices[selected]
        contours.append(go.Scatter3d(
            x=selected_vertices[:, 0], y=selected_vertices[:, 1], z=selected_vertices[:, 2],
            mode='markers',
            marker=dict(size=1.3, color='red', symbol='circle'),
            name=f"Contour at {target}",showlegend=False
        ))

    contours2 = []
    for target in target_distances_diff:
        selected = np.where(np.isclose(diff_distances, target, atol=tolerance))[0]
        selected_vertices = vertices[selected]
        contours2.append(go.Scatter3d(
            x=selected_vertices[:, 0], y=selected_vertices[:, 1], z=selected_vertices[:, 2],
            mode='markers',
            marker=dict(size=1.7, color='black', symbol='circle'),
            name=f"Contour at {target}",showlegend=False
        ))

    layout = go.Layout(
        title="Superposition des lignes de niveau de la différence (en noir) et de la somme (en rouge)",
        scene=dict(xaxis=dict(title='X'), yaxis=dict(title='Y'), zaxis=dict(title='Z')),
        width=800, height=600
    )
    fig = go.Figure(data=[mesh3d] + seed_markers + contours+contours2, layout=layout)
    return fig
