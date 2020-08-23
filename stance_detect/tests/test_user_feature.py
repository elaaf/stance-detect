# Verify users from all feature vectors are the same for a given subset of data read

import sys
sys.path.append("..")

import random
import unittest
from itertools import permutations

# Local Imports
from stance_detect.data_loading.load_data import read_dataset
from stance_detect.feature_extraction.feat_extract import FeatureExtraction


# Unit Test
class TestUsersInFeatureVectors(unittest.TestCase):
    def setUp(self):
        self.num_users = random.randint(100,1000)
        self.rows_to_read = random.randint(1000,10000)
        self.min_tweets = random.randint(1,20)

        dataset_path = "./datasets/twitter_covid.csv"
        features_to_get = ["user_id", "username", "tweet", "mentions", "hashtags"]
        users_list, usernames_list, tweets_list, mentions_list, hashtags_list  =  read_dataset(
                    dataset_path, features=features_to_get, num_users=self.num_users,
                    min_tweets=self.min_tweets, random_sample_size=0, rows_to_read=self.rows_to_read,
                    user_col="user_id", str2list_cols=["mentions", "hashtags"])
        
        ft_extract = FeatureExtraction()
        hashtag_features = ft_extract.hashtags(users_list, hashtags_list)
        mention_features = ft_extract.mentions(users_list, mentions_list)
        tweet_features = ft_extract.tweets(users_list, tweets_list)

        self.to_compare = [ hashtag_features, mention_features, tweet_features ]
    

    def test_users(self):
        to_compare = permutations(self.to_compare, 2)
        for item in to_compare:
            self.assertCountEqual(item[0], item[1])


if __name__ == "__main__":
    unittest.main()
