# 3D interactive plots using plotly

from plotly import graph_objects as go

from utils import unique_filename
from constants import INFO


def scatter_plot_3d(input_data,marker_size=6 ,title="", plot_save_path=""):
    """Generate and open an interactive 3D scatter plot as html.

    Args:
        input_data (dict): Dictionary of (user: feature_vector).
        marker_size (int, optional): Point size in plot. Defaults to 6.
        title (str, optional): Title of the plot. Defaults to "".
        plot_save_path (str, optional): Save path for plot html file. Defaults to "".
    
    TODO:
        Add marker labels.
    """
    
    # Get data to plot from input_data dict
    feature_vectors, labels = zip(*list(input_data.values()))
    x,y,z = zip(* [tuple(x) for x in feature_vectors] )
    
    trace = [go.Scatter3d(x=x, y=y, z=z, mode='markers', 
                          marker=dict(size=marker_size,
                                      color=labels,
                                      colorscale='Viridis',
                                      opacity=0.8)
                          )]
    fig = go.Figure(data=trace)

    title += INFO.LOAD_PARAMS_USED+INFO.DIM_RED_USED+INFO.CLUSTERING_USED
    fig.update_layout(title=title,
                      xaxis_title="",
                      yaxis_title="",
                      legend_title="")
    
    if plot_save_path:
        extra_info = INFO.LOAD_PARAMS_USED+INFO.DIM_RED_USED+INFO.CLUSTERING_USED
        plot_save_path = unique_filename (plot_save_path, extra_info) 
        fig.write_html(plot_save_path)
        
    fig.show()
    
    return