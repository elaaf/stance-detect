import numpy as np

from sklearn.cluster import MeanShift

# Local
from constants import *

def mean_shift_clustering(input_data, bandwidth=None):
    """Get the Mean Shift clustered labels of input_data.

    Args:
        input_data (dict): 
            Dictionary of (user:feature_vector) to be clusterd.
        bandwidth (int, optional): 
            RBF kernel bandwidth. Defaults to None.

    Returns:
        (dict): Dictionary of ( user:(feature_vector,label) ).
    """
    INFO.CLUSTERING_USED = " MeanShift"
    print("\n"+INFO.CLUSTERING_USED+"\n")
    
    model = MeanShift(bandwidth=bandwidth)
    
    # converting input_data to list of shape (n_samples, n_features)
    users = list(input_data.keys())
    data = np.array( list(input_data.values()) )
    
    model.fit(data)
    labels = list(model.labels_)
    
    data_label_zip = list(zip(data,labels))
    user_feature_label_dict = dict(zip( users, data_label_zip))
    return user_feature_label_dict