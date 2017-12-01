# K-Means-GIF-Visualization
Tool for Visualizing K-means Clustering of Color/Grayscale Images or 2D/3D Data

------------------
### K-means
K-means is an unsupervised learning algorithm with an objective of partitioning n observations into k clusters. Observations are grouped into clusters based on the minimum Euclidean (L2) distance from an observation to a cluster centroid, or average of all observations in a cluster; hence the name k-means. Centroids are initially selected at random from the dataset, clusters are formed, and then centroids are iteratively updated by averaging the new observations in each cluster and clustering new observations. This process is typically repeated until the clusters have reached a state of convergence (centroids are equal to previous iteration centroids) or for some number of iterations specified by the user.

Pseudocode is similar to below:

```python
initialize centroids randomly
assign observations to nearest centroid cluster

for iterations
  centroids = average of new cluster observations
  assign observations to nearest centroid cluster
  
  if centroids unchanged
    break

```

K-means can also be extended for clustering of pixel color values of images by treating RGB images as 2-dimensional arrays with 3 features or a grayscale images with 1 feature.

### Python Class Arguments
- __data:__ Input data (numpy array)
- __num_clust:__ Number of k-clusters to partition dataset into
- __max_iters:__ Number of iterations to loop for (Note convergence being reached will end clustering)
- __is_image:__ Set True if input data is an image
- __random_image_color:__ Set True if desired for image cluster pixels to be distinct

------------------
### Unsupervised Clustering Applications
- __[Image Segmentation](https://www.youtube.com/watch?v=yR7k19YBqiw):__
- __Image Compression/Quantization:__
- __[Netflix Recommendations](https://qz.com/939195/netflix-nflx-divides-its-93-million-users-around-the-world-not-by-geography-but-into-1300-taste-communities/):__
- __Anomaly Detection:__
- __Search Engine Results:__

------------------
## Examples

|      Original     |    3 Clusters    |
|:-----------------:|:----------------:|
| ![][pep original] | ![][pep 3 clust] |

|    5 Clusters    |    15 Clusters    |
|:----------------:|:-----------------:|
| ![][pep 5 clust] | ![][pep 15 clust] |

------------------

|      Original     |    3 Clusters    |
|:-----------------:|:----------------:|
| ![][lena original] | ![][lena 3 clust] |

|    5 Clusters    |    15 Clusters    |
|:----------------:|:-----------------:|
| ![][lena 5 clust] | ![][lena 15 clust] |

------------------

|      Original     |    2 Clusters    |
|:-----------------:|:----------------:|
| ![][lena gray original] | ![][lena gray 2 clust] |

|    4 Clusters    |    8 Clusters    |
|:----------------:|:-----------------:|
| ![][lena gray 4 clust] | ![][lena gray 8 clust] |

------------------

|      2 Clusters     |    4 Clusters    |
|:-----------------:|:----------------:|
| ![][blob3d 2 clust] | ![][blob3d 4 clust] |

|    6 Clusters    |    8 Clusters    |
|:----------------:|:-----------------:|
| ![][blob3d 6 clust] | ![][blob3d 8 clust] |

------------------

|      2 Clusters     |    4 Clusters    |
|:-----------------:|:----------------:|
| ![][blob2d 2 clust] | ![][blob2d 4 clust] |

|    6 Clusters    |    8 Clusters    |
|:----------------:|:-----------------:|
| ![][blob2d 6 clust] | ![][blob2d 8 clust] |

[pep original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/peppers.jpg
[pep 3 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/peppers/k-means_3_clusters.gif
[pep 5 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/peppers/k-means_5_clusters.gif
[pep 15 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/peppers/k-means_15_clusters.gif

[lena original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/lena.jpg
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
