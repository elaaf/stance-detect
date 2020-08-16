# Local Imports
from utils import read_twitter_dataset, filter_dataset, str2list

from feature_extraction.feat_extract import FeatureExtraction



if __name__ == "__main__":
    # PRE PROCESSING
    # Get twitter dataset with specific features
    dataset_path = "./stance_detect/datasets/twitter_covid.csv"
    features_to_get = ["user_id", "username", "tweet", "mentions", "hashtags"]
    random_sample_size = 0
    dataset = read_twitter_dataset(dataset_path, features_to_get, random_sample_size, None)

    # Filter Dataset for top user, with atleast min tweets
    dataset = filter_dataset(dataset, num_users= 10, min_tweets=10)

    # FEATURE EXTRACTION
    user_col = "user_id"
    hashtags_col = "hashtags"
    ft_extract = FeatureExtraction()

    # GATHERING DATA FOR FEATURE EXTRACTION
    # list of all users in dataset
    users_list = [row[user_col] for row in dataset]
    # list of all hashtags in dataset
    hashtags_list = [ str2list(row[hashtags_col]) for row in dataset ]
    # 

    # Hashtags feat vector for each user
    hashtag_features = ft_extract.hashtags(users_list, hashtags_list)

    print(list(hashtag_features.items())[0])