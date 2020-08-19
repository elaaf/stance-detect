import sys
sys.path.append("...")

from csv import DictReader
from tqdm import tqdm

# Internal
from constants import *

from utils import sorted_count, str2list



# Filter Dataset for top users with tweets>min_tweets
def filter_users(users_list, num_top_users, min_tweets):
    """Returns filtered dataset for users top users with tweets
       greater than or equal to min_tweets.

    Args:
    
        users_list (list)    : List of users to filter.
        num_top_users (int)      : Number of top users to cluster
        min_tweets (int)     : Min number of tweets to consider a user 
                               "active/engaged"
    
    Returns:
        users_to_keep (list) : list of users to keep.
    """
    # Get sorted user counts
    users_to_keep = sorted_count(users_list)

    # Selecting with greater than or equal to min_tweets
    users_to_keep = [ k for k,v in tqdm(users_to_keep, desc="filtering rows", leave=LEAVE_BAR) if v>= min_tweets ]
    
    # Selecting top num_top_users
    users_to_keep = users_to_keep[:num_top_users]

    return users_to_keep



# Get twitter dataset: uses Pythons native csv DictReader
def load_dataset(dataset_path="", features=[], num_top_users=None, min_tweets=0, random_sample_size=0, rows_to_read=None, user_col="user_id", str2list_cols=[]):
    """Returns the csv twitter dataset, number of outputs same as features with order maintained.
    
    Args:
        dataset_path (str)      : Path to the dataset csv file
        features (list)         : List of feature/columns names to return,
                                  if empty, returns all columns.
        num_top_users (int)         : number of top users to return.
        min_tweets (int)        : Criteria to filter users, with tweets>=min_tweets.
        random_sample_size (int): Number of random samples to select from the dataset
                                  must be less than the total dataset size.
        user_col (string)       : users column name. MUST BE SPECIFIED FOR FILTERING.
        str2list_cols (list)    : list of column names that have lists but read as strings.
                                  converted back to lists using str2list.
                                  
    Returns:
        dataset (list)          : list of csv rows as dictionaries
    """
    INFO.LOAD_PARAMS_USED = f" #rows {rows_to_read} num_top_users {num_top_users} min_tweets {min_tweets}"
    
    if not dataset_path:
        raise ValueError("Arguement dataset_path not defined !")

    dataset = []
    with open(dataset_path, encoding="utf8") as csv_file:  
        csv_file = DictReader(csv_file)

        for i,row in enumerate(tqdm(csv_file, desc="reading rows", leave=LEAVE_BAR),1):
            if features:
                out = tuple( [row[feat] for feat in features] )
                dataset.append( out )
            else:
                dataset.append( row )
            
            if i==rows_to_read:
                break
    
    # Select random samples from the list
    if random_sample_size:
        try:
            dataset = sample(dataset, random_sample_size)
        except:
            raise ValueError(f"random_sample_size larger than dataset size: {len(output)} or negative !")
    
    # Filtering Top users with tweets>=min_tweets
    index_of_user_col = features.index( user_col )
    users_list = [ row[index_of_user_col] for row in dataset ]

    # filtering users
    users_to_keep = filter_users(users_list, num_top_users, min_tweets)

    # filtering rest of data, based on users_to_keep
    str2list_indices = [features.index(col) for col in str2list_cols]
    filtered_dataset = [ tuple([x if i not in str2list_indices else str2list(x) for i,x in enumerate(row)])
                         for row in tqdm(dataset, desc="filtering data", leave=LEAVE_BAR) if row[index_of_user_col] in users_to_keep]

    return zip(* filtered_dataset )