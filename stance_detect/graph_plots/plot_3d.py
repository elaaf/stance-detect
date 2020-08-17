# 3D interactive plots using plotly

from plotly import graph_objects as go


def scatter_plot_3d(input_data, plot_save_path=""):
    # Get data to plot from input_data dict
    feature_vectors, labels = zip(*list(input_data.values()))
    x,y,z = zip(* [tuple(x) for x in feature_vectors] )
    
    trace = [go.Scatter3d(x=x, y=y, z=z, mode='markers', 
                          marker=dict(size=8,
                                      color=labels,
                                      colorscale='Viridis',
                                      opacity=0.8)
                          )]
    fig = go.Figure(data=trace)
    if plot_save_path:
        fig.write_html(plot_save_path)
    fig.show()
    
    return