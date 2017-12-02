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
- __distinct_colors:__ Set True if desired for image cluster pixels to be distinct

------------------
### Unsupervised Clustering Applications
- __[Image Segmentation](https://www.youtube.com/watch?v=yR7k19YBqiw):__
- __Image Compression/Quantization:__
- __[Netflix Recommendations](https://qz.com/939195/netflix-nflx-divides-its-93-million-users-around-the-world-not-by-geography-but-into-1300-taste-communities/):__
- __Anomaly Detection:__
- __Search Engine Results:__

------------------
## Examples
### Self-driving Car
|      Original     |    2 Clusters    |
|:-----------------:|:----------------:|
| ![][traffic original] | ![][traffic 2 clust] |

|    4 Clusters    |    6 Clusters    |
|:----------------:|:-----------------:|
| ![][traffic 4 clust] | ![][traffic 6 clust] |

------------------
### Security Camera
|      Original     |    2 Clusters    |
|:-----------------:|:----------------:|
| ![][sec cam original] | ![][sec cam 2 clust] |

|    3 Clusters    |    4 Clusters    |
|:----------------:|:-----------------:|
| ![][sec cam 3 clust] | ![][sec cam 4 clust] |

------------------
### Owl

|      Original     |    2 Clusters    |
|:-----------------:|:----------------:|
| ![][owl original] | ![][owl 2 clust] |

|    3 Clusters    |    6 Clusters    |
|:----------------:|:-----------------:|
| ![][owl 3 clust] | ![][owl 6 clust] |

------------------
### Man

|      Original     |    2 Clusters    |
|:-----------------:|:----------------:|
| ![][man original] | ![][man 2 clust] |

|    5 Clusters    |    8 Clusters    |
|:----------------:|:-----------------:|
| ![][man 5 clust] | ![][man 8 clust] |

------------------
### Peppers
|      Original     |    3 Clusters    |
|:-----------------:|:----------------:|
| ![][pep original] | ![][pep 3 clust] |

|    7 Clusters    |    15 Clusters    |
|:----------------:|:-----------------:|
| ![][pep 7 clust] | ![][pep 15 clust] |

------------------
### Lena

|      Original     |    3 Clusters    |
|:-----------------:|:----------------:|
| ![][lena original] | ![][lena 3 clust] |

|    7 Clusters    |    15 Clusters    |
|:----------------:|:-----------------:|
| ![][lena 7 clust] | ![][lena 15 clust] |

------------------
### 3D Blobs

|      2 Clusters     |    4 Clusters    |
|:-----------------:|:----------------:|
| ![][blob3d 2 clust] | ![][blob3d 4 clust] |

|    6 Clusters    |    8 Clusters    |
|:----------------:|:-----------------:|
| ![][blob3d 6 clust] | ![][blob3d 8 clust] |

------------------
### 2D Blobs

|      2 Clusters     |    4 Clusters    |
|:-----------------:|:----------------:|
| ![][blob2d 2 clust] | ![][blob2d 4 clust] |

|    6 Clusters    |    8 Clusters    |
|:----------------:|:-----------------:|
| ![][blob2d 6 clust] | ![][blob2d 8 clust] |

[pep original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/peppers.jpg
[pep 3 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/peppers/k-means_3_clusters.gif
[pep 7 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/peppers/k-means_7_clusters.gif
[pep 15 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/peppers/k-means_15_clusters.gif

[lena original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/lena.jpg
[lena 3 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/lena/k-means_3_clusters.gif
[lena 7 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/lena/k-means_7_clusters.gif
[lena 15 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/lena/k-means_15_clusters.gif

[man original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/man.jpg
[man 2 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/man/k-means_2_clusters.gif
[man 5 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/man/k-means_5_clusters.gif
[man 8 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/man/k-means_8_clusters.gif

[owl original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/owl.jpg
[owl 2 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/owl/k-means_2_clusters.gif
[owl 3 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/owl/k-means_3_clusters.gif
[owl 6 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/owl/k-means_6_clusters.gif

[sec cam original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/security_camera.jpg
[sec cam 2 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/security_camera/k-means_2_clusters.gif
[sec cam 3 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/security_camera/k-means_3_clusters.gif
[sec cam 4 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/security_camera/k-means_4_clusters.gif

[traffic original]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/images/traffic.jpg
[traffic 2 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/traffic/k-means_2_clusters.gif
[traffic 4 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/traffic/k-means_4_clusters.gif
[traffic 6 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/traffic/k-means_6_clusters.gif

[blob2d 2 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob2D/k-means_2_clusters.gif
[blob2d 4 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob2D/k-means_4_clusters.gif
[blob2d 6 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob2D/k-means_6_clusters.gif
[blob2d 8 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob2D/k-means_8_clusters.gif

[blob3d 2 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob3D/k-means_2_clusters.gif
[blob3d 4 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob3D/k-means_4_clusters.gif
[blob3d 6 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob3D/k-means_6_clusters.gif
[blob3d 8 clust]: https://github.com/IsaacCorley/K-means-GIF-Visualization/raw/master/files/gifs/blob3D/k-means_8_clusters.gif
