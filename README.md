# Unsupervised User Stance Detection on Twitter.

A python implementation of the paper "Unsupervised User Stance Detection on Twitter" by Darwish et al. [arxiv](https://arxiv.org/abs/1904.02000).
This unofficial repo simply consolidates the code used in the paper for detecting the stance of prolific Twitter users with respect to controversial topics.

## Basic Approach

Given a Twitter dataset containing Tweets regarding a divisive/controversial topic

- Construct Feature Vectors for each user. (Hashtags, Retweeted Accounts, Unique Tweets)


- Apply Dimensionality Reduction. (t-SNE, UMAP)


- Cluster low-dim data (Mean-Shift, DBSCAN)


The low dimensional clusters can be visualized to see nicely separated user clusters, which then can be assigned "Stance" labels based on their orignal descriptors/features.


## How To Run This Code



## Usage




## References
Darwish, K., Stefanov, P., Aupetit, M., & Nakov, P. (2020). Unsupervised User Stance Detection on Twitter. Proceedings of the International AAAI Conference on Web and Social Media, 14(1), 141-152. Retrieved from https://www.aaai.org/ojs/index.php/ICWSM/article/view/7286


# UNDER PROGRESS !
