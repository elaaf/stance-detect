import sys
sys.path.append("..")

import numpy as np

from tqdm import tqdm
from utils import sorted_count

# For "n" users with "min_tweets" in dataset, we find
# Hashtags
# Retweeted Accounts
# Unique Tweets


class FeatureExtraction():
    def __init__(self):
        return


    def hashtags(self, users_list, hashtags_list, feature_size=None, relative_freq=True):
        """Returns a list of dictionary, with hashtag features for each user.
        Arguments:
            users_list (list)           : List of all users in the dataset (Non-Unique).
            hashtags_list (list)        : List of list of all hashtags shared.
            feature_size (int)          : Length of the hashtags feature vector
                                          (Equivalent to selecting top popular hashtags)
                                          If None - uses all hashtags in the dataset.
            relative_freq (bool)        : Whether to compute feature vector with relative
                                          count i.e. divide by total count.
        Returns:
            hashtag_features (list)     : list of dictionaries, with user_col as key and
                                           hashtag feature vector as value.
        """
        # get the counts of each hashtag shared
        # Collapse the list of lists: hashtags_list
        hashtag_counts = sorted_count([h for l in hashtags_list for h in l])

        # fitler against feature_size, Default is None=Selects all.
        hashtag_counts = hashtag_counts[:feature_size]
        hashtag_vector = [h for h,_ in hashtag_counts]

        # zip users,hastags
        users_hashtags = zip(users_list, hashtags_list)

        # findng hashtag feature for each user
        hashtag_features = {}
        for user in tqdm(set(users_list), desc="hashtag_features", leave=True):
            user_hashtags = [h for u,h in users_hashtags if u==user]
            hashtag_features[user] = np.array( [ user_hashtags.count(h) for h in hashtag_vector ] )
        
        return hashtag_features
    

    def mentions(self, users_list, mentions_list, feature_size=None, relative_freq=True):
        """Returns a list of dictionary, with mentions features for each user.
        Arguments:
            users_list (list)           : List of all users in the dataset (Non-Unique).
            mentions_list (list)        : List of list of all mentions shared.
            feature_size (int)          : Length of the mentions feature vector
                                          (Equivalent to selecting top popular mentions)
                                          If None - uses all mentions in the dataset.
            relative_freq (bool)        : Whether to compute feature vector with relative
                                          count i.e. divide by total count.
        Returns:
            hashtag_features (list)     : list of dictionaries, with user_col as key and
                                           mention feature vector as value.
        """
        
        return


    def unique_tweets(self):
        return
    
