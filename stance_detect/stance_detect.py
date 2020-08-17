# Local Imports
from constants import *

from data_loading.load_data import load_dataset
from feature_extraction.feat_extract import FeatureExtraction
from dimensionality_reduction.umap import get_umap_embedding
from clustering.mean_shift import mean_shift_clustering
from graph_plots.plot_3d import scatter_plot_3d



if __name__ == "__main__":

    ##### DATA LOADING #####
    # Get dataset columns
    users_list, usernames_list, tweets_list, mentions_list, hashtags_list  =  load_dataset(
                        dataset_path="./datasets/twitter_covid.csv", 
                        features=["user_id", "username", "tweet", "mentions", "hashtags"], 
                        num_top_users=1000,
                        min_tweets=10,
                        random_sample_size=0, 
                        rows_to_read=None,
                        user_col="user_id", 
                        str2list_cols=["mentions", "hashtags"])


    ##### FEATURE EXTRACTION #####
    # Define features to use for Dim Reduction and Clustering
    # CONSISTENT WITH THE PAPER
    # T : tweets feature vectors
    # R : mentions OR retweets feature vectors
    # H : hashtags feature vector
    # Feature vectors will be concatenated in order
    FEATURES_TO_USE = ["T","R","H"]

    ft_extract = FeatureExtraction()
    user_feature_dict = ft_extract.get_user_feature_vectors(
                            FEATURES_TO_USE,
                            users_list,
                            tweets_list, 
                            mentions_list, 
                            hashtags_list,
                            feature_size=None,
                            relative_freq=True
                            )
    
    
    ##### DIMENSIONALITY REDUCTION #####
    low_dim_user_feature_dict = get_umap_embedding(
                                    user_feature_dict,
                                    n_neighbors=15,
                                    n_components=3,
                                    min_distance=0.1,
                                    distance_metric="correlation")
    
    
    
    ##### CLUSTERING #####
    user_feature_label_dict = mean_shift_clustering( low_dim_user_feature_dict )
    
    
    ##### PLOTTING #####
    scatter_plot_3d(user_feature_label_dict, 
                    plot_save_path="./stance_detect/results/3d_sactter_plot.html")