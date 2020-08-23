# UMAP Dimensionality Reduction

import numpy as np

from umap import UMAP

# Locals
from constants import *


def get_umap_embedding(input_data, n_neighbors=15, n_components=3, min_distance=0.1, distance_metric='correlation'):
    """Get the low dimensional UMAP embedding of input_data (num_samples, num_features).

    Args:
        input_data (dict): 
            Dictionary of (user: feature_vector).
        n_neighbors (int, optional): 
            UMAP parameter. Defaults to 15.
        n_components (int, optional): 
            Lower Dimension components.
        min_distance (float, optional): 
            UMAP parameter. Defaults to 0.1.
        distance_metric (str, optional): 
            UMAP parameter. Defaults to 'correlation'.

    Returns:
        (dict) : Dictionary of (user: low_dim_feature_vector).
    """
    INFO.DIM_RED_USED = f" UMAP(n_neigh {n_neighbors}, min_dist {min_distance})"
    print("\n"+INFO.DIM_RED_USED+"\n")
    
    
    dim_reducer = UMAP(n_neighbors=n_neighbors,
                       n_components=n_components,
                       min_dist=min_distance,
                       metric=distance_metric)
    
    # reshape data into list of shape (num_samples, num_features)
    users = list(input_data.keys())
    data = np.array( list(input_data.values()) )
    
    low_dim_data = dim_reducer.fit_transform(data)

    low_dim_user_data = dict(zip( users, list(low_dim_data) ))
    return low_dim_user_data