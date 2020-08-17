import sys
sys.path.append("..")

import numpy as np

from tqdm import tqdm

# Local Imports
from constants import *

from utils import sorted_count, get_tweet_counts

# For "n" users with "min_tweets" in dataset, we find
# Hashtags
# Retweeted Accounts
# Unique Tweets


class FeatureExtraction():
    def __init__(self):
        # Dictionary to lookup function for each input ["T","R","H"] 
        self.functions_dict = {
            "T": self.tweets,
            "R": self.mentions,
            "H": self.hashtags}
        return

    def get_user_feature_vectors(self, features_to_use, users_list, *feature_vectors_to_use, feature_size=None, relative_freq=True):
        """Returns a dictionary containing, (user:feature_vector), where
        feature_vector are concatenated features provided in features_to_use.

        Args:
            features_to_use (list)          : list of features to use e.g. ["T","R","H"]  
                                              T : tweets feature vectors
                                              R : mentions OR retweets feature vectors
                                              H : hashtags feature vector
                                              Feature vectors will be concatenated in order. 
            users_list (list)               : list of users
            feature_vectors_to_use (*args)  : positional arguments as list of feature_vectors in 
                                              same order as features_to_use ["T","R","H"].
            feature_size (int)              : Length of the hashtags feature vector
                                              (Equivalent to selecting top popular hashtags)
                                              If None - uses all hashtags in the dataset.
            relative_freq (bool)            : Whether to compute feature vector with relative
                                              count i.e. divide by total count.
                                              
        Returns:
            user_feature_vectors_dict (dict): Dictionary of (user:feature_vector)
        """
        features_dict = {}
        for i,feature in enumerate(features_to_use):
            try:
                current_feature_vectors_to_use = feature_vectors_to_use[i]
            except:
                raise ValueError("Different num of features_to_use and num of positional arguments *feature_vectors_to_use ")  

            try:
                features_dict[feature] = self.functions_dict[feature](
                                            users_list,
                                            current_feature_vectors_to_use,
                                            feature_size=feature_size,
                                            relative_freq=relative_freq
                                            )
            except:
                raise ValueError(f'Invalid feature {feature} ! Options: ["T","R","H"] !')        

        # Concatenating user feature vectors
        user_feature_vectors_dict = {}
        for user in tqdm(set(users_list), desc="concat user_features", leave=LEAVE_BAR):
            user_feature_vectors_dict[user] = np.concatenate( [features_dict[f][user] for f in features_to_use] )

        return user_feature_vectors_dict


    def hashtags(self, users_list, hashtags_list, feature_size=None, relative_freq=True):
        """Returns a list of dictionary, with hashtag features for each user.
        
        Args:
            users_list (list)           : List of all users in the dataset (Non-Unique).
            hashtags_list (list)        : List of list of all hashtags shared.
            feature_size (int)          : Length of the hashtags feature vector
                                          (Equivalent to selecting top popular hashtags)
                                          If None - uses all hashtags in the dataset.
            relative_freq (bool)        : Whether to compute feature vector with relative
                                          count i.e. divide by total count.
                                          
        Returns:
            hashtag_features (dict)     : Dictionary, with user_col as key and
                                           hashtag feature vector as value.
        """
        # get the counts of each hashtag shared
        # Collapse the list of lists: hashtags_list
        hashtag_counts = sorted_count([h for l in hashtags_list for h in l if h])

        # fitler against feature_size, Default is None=Selects all.
        hashtag_counts = hashtag_counts[:feature_size]
        hashtag_vector = tuple([h for h,_ in hashtag_counts])

        # zip users,hastags
        users_hashtags_zip = list(zip(users_list, hashtags_list))

        # findng hashtag feature for each user
        hashtag_features = {}
        for user in tqdm(set(users_list), desc="hashtag_features", leave=LEAVE_BAR):
            user_hashtags = [h for u,hts in users_hashtags_zip for h in hts if u==user]
            hashtag_features[user] = np.array( [ user_hashtags.count(h) for h in hashtag_vector ] )
            if relative_freq and np.sum(hashtag_features[user])>0:
                hashtag_features[user] = hashtag_features[user]/np.sum(hashtag_features[user])
        
        return hashtag_features
    

    def mentions(self, users_list, mentions_list, feature_size=None, relative_freq=True):
        """Returns a list of dictionary, with mentions features for each user.
        
        Args:
            users_list (list)           : List of all users in the dataset (Non-Unique).
            mentions_list (list)        : List of list of all mentions shared.
            feature_size (int)          : Length of the mentions feature vector
                                          (Equivalent to selecting top popular mentions)
                                          If None - uses all mentions in the dataset.
            relative_freq (bool)        : Whether to compute feature vector with relative
                                          count i.e. divide by total count.
                                          
        Returns:
            mention_features (dict)     : Dictionary, with user_col as key and
                                           mention feature vector as value.
        """
        # Collapsing mentions of users into a single list
        all_mentions = [x for m in mentions_list for x in m if x]
        mention_counts = sorted_count(all_mentions)

        mentions_vector = [m for m,_ in mention_counts]

        # zip users, mentions
        users_mentions_zip = list(zip(users_list, mentions_list))
        # findng mention feature vector for each user
        mention_features = {}
        for user in tqdm(set(users_list), desc="mention_features", leave=LEAVE_BAR):
            user_mentions = [m for u,mns in users_mentions_zip for m in mns if u==user]
            mention_features[user] = np.array( [ user_mentions.count(m) for m in mentions_vector ] )
            if relative_freq and np.sum(mention_features[user])!=0:
                mention_features[user] = mention_features[user]/np.sum(mention_features[user])
        
        return mention_features


    def tweets(self, users_list, tweets_list, feature_size=None, relative_freq=True):
        """Returns a list of dictionary, with tweets features for each user.
        
        Args:
            users_list (list)           : List of all users in the dataset (Non-Unique).
            tweets_list (list)          : List of list of all tweets shared.
            feature_size (int)          : Length of the tweets feature vector
                                          (Equivalent to selecting top popular tweets)
                                          If None - uses all tweets in the dataset.
            relative_freq (bool)        : Whether to compute feature vector with relative
                                          count i.e. divide by total count.
                                          
        Returns:
            tweet_features (dict)       : Dictionary, with user_col as key and
                                           tweet feature vector as value.
        """
        # Get tweet counts, sorted by count in descending order
        tweet_counts = get_tweet_counts(tweets_list, fuzzy_matching=False)

        # Tweet Vector
        tweets_vector = [tweet for tweet,_ in tweet_counts]

        # zip users, tweets
        users_tweets_zip = list(zip(users_list, tweets_list))

        # findng tweet feature vector for each user
        tweet_features = {}
        for user in tqdm(set(users_list), desc="tweet_features", leave=LEAVE_BAR):
            user_tweets = [ tweet for u,tweet in users_tweets_zip if u==user ]

            tweet_features[user] = np.array( [ user_tweets.count(tweet) for tweet in tweets_vector ] )
            if relative_freq and np.sum(tweet_features[user])!=0:
                tweet_features[user] = tweet_features[user]/np.sum(tweet_features[user])
        
        return tweet_features