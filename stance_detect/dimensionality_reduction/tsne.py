# t-SNE Dimensionality Reduction

import numpy as np
from sklearn.manifold import TSNE

# Local Imports
from constants import INFO


def get_tsne_embedding(input_data, n_components=3, perplexity=30, early_exaggeration=12, learning_rate=200, max_iters=1000, metric="euclidean", verbose=0):
    """Get low dimensional t-SNE embedding.

    Args:
        input_data (dict): 
            Dictionary of (user: feature_vector)
        n_components (int, optional): 
            Number of low dimensions to reduce to. Defaults to 3.
        perplexity (int, optional): 
            Balance focus between local and gloabl
            data features. Defaults to 30.
        early_exaggeration (int, optional): 
            Specifies space between natural clusters 
            in the embedding space. Defaults to 12.
        learning_rate (int, optional): 
            Higher values clumps data into a ball.
            Defaults to 200.
        max_iters (int, optional): 
            Max iterations to run for. Defaults to 1000.
        metric (str, optional): 
            Distance metric. Defaults to "euclidean".
        verbose (int, optional): 
            Define verbose level. Defaults to 0.

    Returns:
        (dict): Dictionary of (user: low_dim_featuer_vector)
    """
    dim_reducer = TSNE(n_components=n_components, 
                       perplexity=perplexity, 
                       early_exaggeration=early_exaggeration, 
                       learning_rate=learning_rate, 
                       n_iter=max_iters,
                       metric=metric,
                       verbose=verbose)
    
    # reshape data into list of shape (num_samples, num_features)
    users = list(input_data.keys())
    data = np.array( list(input_data.values()) )
    
    low_dim_data = dim_reducer.fit_transform(data)

    low_dim_user_data = dict(zip( users, list(low_dim_data) ))
    
    return low_dim_user_data