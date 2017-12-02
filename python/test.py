from imageio import imread
from sklearn.datasets import make_blobs
from kmeans import KMeans


max_iters = 50

#%% RGB image
file = '../files/images/peppers.jpg'

data = imread(file)
for i in [3, 7, 15]:
    k_means = KMeans(data, num_clust=i, max_iters=max_iters,
                     is_image=True)
    centroids, clusters = k_means.fit()

#%% RGB image
file = '../files/images/lena.jpg'

data = imread(file)
for i in [3, 7, 15]:
    k_means = KMeans(data, num_clust=i, max_iters=max_iters,
                     is_image=True)
    centroids, clusters = k_means.fit()

#%% Grayscale image
file = '../files/images/owl.jpg'

data = imread(file)
for i in [2, 3, 6]:
    k_means = KMeans(data, num_clust=i, max_iters=max_iters,
                     is_image=True)
    centroids, clusters = k_means.fit()
    
#%% Grayscale image
file = '../files/images/man.jpg'

data = imread(file)
for i in [2, 5, 8]:
    k_means = KMeans(data, num_clust=i, max_iters=max_iters,
                     is_image=True)
    centroids, clusters = k_means.fit()

#%% Grayscale image
file = '../files/images/security_camera.jpg'

data = imread(file)
for i in [2, 3, 4]:
    k_means = KMeans(data, num_clust=i, max_iters=max_iters,
                     is_image=True)
    centroids, clusters = k_means.fit()  
    
#%% RGB self-driving car image segmentation
file = '../files/images/traffic.jpg'

data = imread(file)
for i in [2, 4, 6]:
    k_means = KMeans(data, num_clust=i, max_iters=max_iters,
                     is_image=True, distinct_colors=True)
    centroids, clusters = k_means.fit()
        
#%% 3D data
data, _ = make_blobs(n_samples=500, centers=15, n_features=3)

for i in [2, 4, 6, 8]:
    k_means = KMeans(data, num_clust=i, max_iters=max_iters)
    centroids, clusters = k_means.fit()

#%% 2D data
data, _ = make_blobs(n_samples=500, centers=15, n_features=2)

for i in [2, 4, 6, 8]:
    k_means = KMeans(data, num_clust=i, max_iters=max_iters)
    centroids, clusters = k_means.fit()
