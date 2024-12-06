# camera_animation.py
import plotly.graph_objects as go

def update_camera_animation(fig):
    # Define your camera animation frames (or final camera settings)
    frames = [
        {
            "name": "frame1",
            "data": [],
            "layout": {
                "scene": {
                    "camera": {
                        "eye": {"x": 0, "y": 0, "z": 2.4},  # Initial camera position
                        "up": {"x": 0, "y": 0, "z": 1},
                        "center": {"x": 0, "y": 0, "z": 0}
                    }
                }
            }
        },
        {
            "name": "frame2",
            "data": [],
            "layout": {
                "scene": {
                    "camera": {
                        "eye": {"x": 0, "y": 0, "z": 2.4},  # Same eye position
                        "up": {"x": 0.5, "y": 0, "z": 0.5},  # Transition of the 'up' direction
                        "center": {"x": 0, "y": 0, "z": 0}
                    }
                }
            }
        },
        {
            "name": "frame3",
            "data": [],
            "layout": {
                "scene": {
                    "camera": {
                        "eye": {"x": 0, "y": 0, "z": 2.4},
                        "up": {"x": 1, "y": 0, "z": 0},  # Final 'up' direction
                        "center": {"x": 0, "y": 0, "z": 0}
                    }
                }
            }
        }
    ]

    # Update the layout of the figure to add the camera animation frames and buttons
    fig.update_layout(
        updatemenus=[
            {
                "buttons": [
                    {
                        "args": [
                            None,
                            {
                                "frame": {"duration": 10000, "redraw": True},
                                "fromcurrent": True,
                                "mode": "immediate",
                                "transition": {"duration": 500, "easing": "cubic-in-out"}
                            }
                        ],
                        "label": "Start Camera Animation",
                        "method": "animate"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }
        ]
    )
    return fig
