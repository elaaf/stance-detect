# Unsupervised User Stance Detection on Twitter.

A python implementation of the paper "Unsupervised User Stance Detection on Twitter" by Darwish et al. [arxiv](https://arxiv.org/abs/1904.02000).
This unofficial repo simply consolidates the code used in the paper for detecting the stance of prolific Twitter users with respect to controversial topics.

## Approach

Given a Twitter dataset containing Tweets regarding a divisive/controversial topic

- Construct Feature Vectors for each user. (Hashtags, Retweeted Accounts, Unique Tweets)


- Apply Dimensionality Reduction. (t-SNE, UMAP)


- Cluster low-dim data (Mean-Shift, DBSCAN)


The low dimensional clusters can be visualized to see nicely separated user clusters, which then can be assigned "Stance" labels based on their orignal descriptors/features.



## Requirements
To be added.




## How To Run This Code

Clone this repo.
```
git clone https://github.com/elaaf/stance-detect.git
```


Place your Twitter Dataset CSV in ./datasets/ folder.
Set parameters in stance_detect.py
For Standard Twitter API Dataset CSV, simply run.

```
python stance_detect/stance_detect.py
```


#### API USAGE

Data Loading
```python
from data_loading.load_data import load_dataset

load_dataset(dataset_path="./datasets/twitter_dataset.csv",
             features=["user_id", "username", "tweet", "mentions", "hashtags"], 
             num_top_users=1000,
             min_tweets=0,
             random_sample_size=0, 
             rows_to_read=None, 
             user_col="user_id", 
             str2list_cols=["mentions", "hashtags"])
```


Feature Extraction
```python
from feature_extraction.feat_extract import FeatureExtraction

FEATURES_TO_USE = ["T","R","H"]

ft_extract = FeatureExtraction()
user_feature_dict = ft_extract.get_user_feature_vectors(
                                FEATURES_TO_USE,
                                users_list,
                                tweets_list, 
                                mentions_list, 
                                hashtags_list,
                                feature_size=None,
                                relative_freq=True)
```

Dimensionality Reduction
```python
from dimensionality_reduction.umap import get_umap_embedding

low_dim_user_feature_dict = get_umap_embedding(
                                user_feature_dict,
                                n_neighbors=20,
                                n_components=3,
                                min_distance=0.1,
                                distance_metric="correlation")
```


Clustering
```python
from clustering.mean_shift import mean_shift_clustering

user_feature_label_dict = mean_shift_clustering( low_dim_user_feature_dict )

```

Interactive Scatter Plot
```python
from graph_plots.plot_3d import scatter_plot_3d

scatter_plot_3d(user_feature_label_dict, 
                title="Twitter Users Scatter Plot",
                plot_save_path="./stance_detect/results/3d_scatter_plot.html")
```

## 3D Scatter Plot

[![3D Scatter Plot](/images/3d_scatter_plot.png "3D Scatter Plot, Click to view Interactive !")](https://elaaf.github.io/stance-detect/3d_scatter_plot.html)



## References
Darwish, K., Stefanov, P., Aupetit, M., & Nakov, P. (2020). Unsupervised User Stance Detection on Twitter. Proceedings of the International AAAI Conference on Web and Social Media, 14(1), 141-152. Retrieved from https://www.aaai.org/ojs/index.php/ICWSM/article/view/7286


# UNDER PROGRESS !