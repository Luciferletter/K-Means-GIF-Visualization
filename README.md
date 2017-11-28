# K-Means-GIF-Visualization
Tool for Visualizing K-Means Clustering of Color/Grayscale Images or 2D/3D Data

The kmeans_nd.m function performs K-means clustering on data with an arbitrary number of features.  The function provides support for 
plotting data with 2-3 features only. Support for k-means clustering on image data is also included by setting the ‘image’ argument to true 
and the ‘image_fname’ argument to the desired filename. The ability to save the clustered plots or images at each iteration into a .gif 
file is also included by setting the ‘gif’ argument to true. L1, L2, and Cosine distance similarity metrics are supported as well via the 
‘metric’ argument. The outputs are the clusters, the cluster indices and the centroids of each cluster.
  
# Examples

|      Original     |    3 Clusters    |
|:-----------------:|:----------------:|
| ![][pep original] | ![][pep 3 clust] |

|    5 Clusters    |    10 Clusters    |
|:----------------:|:-----------------:|
| ![][pep 5 clust] | ![][pep 10 clust] |










[pep original]: https://github.com/IsaacCorley/K-means-Clustering-GIF-Visualization-Tool/raw/master/files/peppers/peppers.png
[pep 3 clust]: https://github.com/IsaacCorley/K-means-Clustering-GIF-Visualization-Tool/raw/master/files/peppers/peppers_3_clust_.gif
[pep 5 clust]: https://github.com/IsaacCorley/K-means-Clustering-GIF-Visualization-Tool/raw/master/files/peppers/peppers_5_clust_.gif
[pep 10 clust]: https://github.com/IsaacCorley/K-means-Clustering-GIF-Visualization-Tool/raw/master/files/peppers/peppers_10_clust_.gif
