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

|    5 Clusters    |    15 Clusters    |
|:----------------:|:-----------------:|
| ![][pep 5 clust] | ![][pep 15 clust] |


|      Original     |    3 Clusters    |
|:-----------------:|:----------------:|
| ![][lena original] | ![][lena 3 clust] |

|    5 Clusters    |    15 Clusters    |
|:----------------:|:-----------------:|
| ![][lena 5 clust] | ![][lena 15 clust] |


|      Original     |    2 Clusters    |
|:-----------------:|:----------------:|
| ![][lena gray original] | ![][lena gray 2 clust] |

|    4 Clusters    |    8 Clusters    |
|:----------------:|:-----------------:|
| ![][lena gray 4 clust] | ![][lena gray 8 clust] |


|      2 Clusters     |    4 Clusters    |
|:-----------------:|:----------------:|
| ![][blob2d 2 clust] | ![][blob2d 4 clust] |

|    6 Clusters    |    8 Clusters    |
|:----------------:|:-----------------:|
| ![][blob2d 6 clust] | ![][blob2d 8 clust] |


|      2 Clusters     |    4 Clusters    |
|:-----------------:|:----------------:|
| ![][blob3d 2 clust] | ![][blob3d 4 clust] |

|    6 Clusters    |    8 Clusters    |
|:----------------:|:-----------------:|
| ![][blob3d 6 clust] | ![][blob3d 8 clust] |

[pep original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/peppers.jpg
[pep 3 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/peppers/k-means_3_clusters.gif
[pep 5 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/peppers/k-means_5_clusters.gif
[pep 15 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/peppers/k-means_15_clusters.gif

[lena original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/lena.tif
[lena 3 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/lena/k-means_3_clusters.gif
[lena 5 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/lena/k-means_5_clusters.gif
[lena 15 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/lena/k-means_15_clusters.gif

[lena gray original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/lena_gray.jpg
[lena gray 2 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/lena_gray/k-means_2_clusters.gif
[lena gray 4 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/lena_gray/k-means_4_clusters.gif
[lena gray 8 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/lena_gray/k-means_8_clusters.gif

[blob2d 2 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob2D/k-means_2_clusters.gif
[blob2d 4 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob2D/k-means_4_clusters.gif
[blob2d 6 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob2D/k-means_6_clusters.gif
[blob2d 8 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob2D/k-means_8_clusters.gif

[blob3d 2 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob3D/k-means_2_clusters.gif
[blob3d 4 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob3D/k-means_4_clusters.gif
[blob3d 6 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob3D/k-means_6_clusters.gif
[blob3d 8 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob3D/k-means_8_clusters.gif
