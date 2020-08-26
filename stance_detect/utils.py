# Imports
import os 

from tqdm import tqdm
from random import sample

from constants import *

## HELPER FUNCTIONS

def get_tweet_counts(list_of_tweets, fuzzy_matching=False, fuzzy_matching_threshold=0.7):
    """Returns a list containing tuple((tweet): count), sorted by count in descending order.
    The first element (tweet) is a tuple, and may aggregate multiple tweets
    as one, based on the tweet_similarity function.
    
    Args:
        list_of_tweets (list): 
            list of strings, where each string is a tweet.
        fuzzy_matching (bool): 
            To find similar tweets using fuzzy string matching.
                                          Default: False.
        fuzzy_matching_threshold (int): 
            Similarity threshold for fuzzy string matching over 
            which to consider two tweets similar. Defaults to 0.7.
    
    Returns:
        (list): list of ((tweet/s), count).
    
    TODO:
        Add fuzzy string matching for tweets.
    """
    if not fuzzy_matching:
        unique_tweets = set(list_of_tweets)
        tweet_counts = [(tweet,list_of_tweets.count(tweet)) 
                        for tweet in tqdm(unique_tweets, desc="finding couts", leave=LEAVE_BAR)]
        tweet_counts =  sorted(tweet_counts, key=lambda item: item[1], reverse=True)

    if fuzzy_matching:
        pass
        # TO BE IMPLEMENTED

    return tweet_counts


# Function to return 

# List to Sorted counts dict
def sorted_count(array, reverse=True):
    """Returns a list containing tuple (value, count) of each unqiue value
       in the list, in desceding order.
    """
    sorted_count_list = [ (x,array.count(x)) for x in tqdm(set(array), desc="finding counts", leave=LEAVE_BAR) ]
    sorted_count_list =  sorted(sorted_count_list, key=lambda item: item[1], reverse=reverse)
    return sorted_count_list


# String to List
def str2list(string):
    """Returns list contained in a string.
    
    Args:
        string (str): A string containing a list.
    
    Returns:
        (list): inferred list from the string.
    """
    # Removing brackets "[" "]" from the string
    string = string[1:-1]

    # Splitting at ","
    output = string.split(",")

    # Removing trailing, leading space and residue ' ' characters
    output = [ string.strip()[1:-1] for string in output ]

    return output


# Get a unique file name
def unique_filename(save_path, extra_info):
    """Generate a new unique enumerated file name, 
       based on existing files.

    Args:
        save_path (str): 
            file path. Makes directory if does not exist.
        extra_info (str): 
            Text to append before file extension.

    Returns:
        (str): An enumerated file path.
    """
    # Check if path exists, otherwise make directory
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
    
    filename, extension = os.path.splitext(save_path)
    filename, extension = str(filename), str(extension)

    filename += extra_info
    save_path = filename+extension
    
    counter = 1
    while os.path.exists(save_path):
        save_path = filename+" ("+str(counter)+")"+extension
        counter += 1

    return save_path


