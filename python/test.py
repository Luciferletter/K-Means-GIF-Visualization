from kmeans import KMeans
from imageio import imread
from sklearn.datasets import make_blobs


#%% RGB image
file = './files/images/peppers.jpg'

data = imread(file)
for i in [3, 5, 10, 15]:
    k_means = KMeans(data, num_clust=i, max_iters=25, is_image=True)
    centroids, clusters = k_means.fit()

#%% RGB image
file = './files/images/lena.jpg'

data = imread(file)
for i in [3, 5, 10, 15]:
    k_means = KMeans(data, num_clust=i, max_iters=25, is_image=True)
    centroids, clusters = k_means.fit()

#%% Grayscale image
file = './files/images/lena_gray.jpg'

data = imread(file)
for i in [2, 4, 6, 8]:
    k_means = KMeans(data, num_clust=i, max_iters=25, is_image=True)
    centroids, clusters = k_means.fit()

#%% 3D data
data, _ = make_blobs(n_samples=500, centers=15, n_features=3)

for i in [2, 4, 6, 8]:
    k_means = KMeans(data, num_clust=i, max_iters=25, is_image=False)
    centroids, clusters = k_means.fit()

#%% 2D data
data, _ = make_blobs(n_samples=500, centers=15, n_features=2)

for i in [2, 4, 6, 8]:
    k_means = KMeans(data, num_clust=i, max_iters=25, is_image=False)
    centroids, clusters = k_means.fit()
