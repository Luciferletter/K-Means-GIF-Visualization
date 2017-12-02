import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from imageio import mimwrite


class KMeans:
    def __init__(self, data, num_clust=3, max_iters=50,is_image=False,
                 distinct_colors=False):
        self.data = np.array(data)
        self.num_clust = num_clust
        self.max_iters = max_iters
        self.is_image = is_image
        
        
        self.distinct_colors = distinct_colors
        
        self.converged = False
        self.clusters_idx = None
        self.centroids = []
        self.plots = []

        # Flatten array if image (excluding channel dimension)
        if self.is_image:
            self.image_dims = self.data.shape

            if len(self.image_dims) == 2:
                self.data = np.reshape(self.data, (-1))
            else:
                self.data = np.reshape(self.data, (-1, self.image_dims[-1]))

        self.num_samples = self.data.shape[0]

        if len(self.data.shape) > 1:
            self.num_features = self.data.shape[-1]
        else:
            self.num_features = 1

        # Generate distinct colors if desired
        if self.is_image & self.distinct_colors:
            self.distinct_colors = self.__generate_colors()
        else:
            self.distinct_colors = False
            
        print('Number of Clusters:', self.num_clust)
        print('Number of Iterations:', self.max_iters)
        print('Number of Features:', self.num_features)


    def __initialize_centroids(self):
        # Randomly sample n samples from data where n = number of clusters
        rand_samples = np.random.randint(0, high=self.num_samples, size=self.num_clust)
        self.centroids = list(self.data[rand_samples])


    def __update_centroids(self):
        # New centroids are average of all data samples in the corresponding cluster
        new_centroids = self.centroids.copy()

        for cluster in range(len(self.centroids)):
            new_centroids[cluster] = np.mean(self.data[np.argwhere(self.clusters_idx == cluster)], axis=0)

        return new_centroids


    def __update_clusters(self):
        distances = np.zeros((self.num_samples, len(self.centroids)))

        # Compute distance between each sample and each centroid
        for cluster in range(len(self.centroids)):
            if self.num_features > 1:
                distances[:, cluster] = np.sqrt(np.sum((self.centroids[cluster] - self.data) ** 2, axis=-1))
            else:
                distances[:, cluster] = np.sqrt((self.centroids[cluster] - self.data) ** 2)

        # Points belong to the cluster with the nearest centroid
        # Or formally, the minimum Euclidean (L2) distance
        self.clusters_idx = np.argmin(distances, axis=-1)


    def __compare_centroids(self, new_centroids):
        # If centroids unchanged then clusters have converged
        if np.array_equal(self.centroids, new_centroids):
            self.converged = True
            print('Converged')


    def __plot_clusters(self):
        
        # Images
        if self.is_image:
            cluster_plot = self.data.copy()
            
            # Make cluster points equal to pixel value of corresponding centroid
            for cluster in range(len(self.centroids)):
                if self.distinct_colors:
                    cluster_plot[self.clusters_idx == cluster] = self.distinct_colors[cluster]
                else:
                    cluster_plot[self.clusters_idx == cluster] = self.centroids[cluster]
            
            # Reshape to original image dimensions
            cluster_plot = np.reshape(cluster_plot, self.image_dims)
            
            # Turn off graph ticks
            plt.tick_params(which='both', top='off', bottom='off',
                            left='off', right='off',
                            labelbottom='off', labeltop='off',
                            labelleft='off', labelright='off')
            
            # Plot grayscale
            if self.num_features == 1:
                plt.imshow(cluster_plot, cmap='gray')
                
            # Plot RGB
            else:
                plt.imshow(cluster_plot)
        
        # Non-images
        else:
            centroid_arr = np.squeeze(np.array(self.centroids))
            
            fig = plt.figure()
            
            # Plot 2D data
            if self.num_features == 2:

                plt.tick_params(which='both', top='off', bottom='off',
                                left='off', right='off',
                                labelbottom='off', labeltop='off',
                                labelleft='off', labelright='off')
            
                # Plot clusters
                plt.scatter(self.data[:, 0], self.data[:, 1], s=25,
                            c=self.clusters_idx, alpha=1.0, zorder=0)
                
                # Plot centroids
                plt.scatter(centroid_arr[:, 0], centroid_arr[:, 1], 
                            s=125, c=np.arange(0, centroid_arr.shape[0]),
                            marker='*', alpha=1.0, zorder=10, edgecolors='k')
                
                # Set plot limits
                plt.xlim(self.data[:, 0].min()-1, self.data[:, 0].max()+1)
                plt.ylim(self.data[:, 1].min()-1, self.data[:, 1].max()+1)
                
            # Plot 3D data
            elif self.num_features == 3:
                ax = Axes3D(fig)
                ax.tick_params(which='both', top='off', bottom='off',
                                left='off', right='off',
                                labelbottom='off', labeltop='off',
                                labelleft='off', labelright='off')
                
                # Plot clusters
                ax.scatter(self.data[:, 0], self.data[:, 1], self.data[:, 2], 
                            s=25, c=self.clusters_idx, alpha=0.6, depthshade=False)
                
                # Plot centroids
                ax.scatter(centroid_arr[:, 0], centroid_arr[:, 1], centroid_arr[:, 2],
                            s=125, c=np.arange(0, centroid_arr.shape[0]),
                            marker='*', alpha=1.0, depthshade=False, edgecolors='k')
                
                # Set plot limits
                ax.set_xlim3d(left=self.data[:, 0].min(), right=self.data[:, 0].max())
                ax.set_ylim3d(top=self.data[:, 1].min(), bottom=self.data[:, 1].max())
                ax.set_zlim3d(top=self.data[:, 2].min(), bottom=self.data[:, 2].max())
                
            # Convert plot to image array for .gif
            fig.canvas.draw()
            cluster_plot = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
            cluster_plot = cluster_plot.reshape(fig.canvas.get_width_height()[::-1] + (3,))
            plt.close(fig)
            
        # Append to plot list for conversion to .gif
        self.plots.append(cluster_plot)


    def __write_gif(self):
        output_file = 'k-means_%d_clusters.gif' % self.num_clust
        
        if self.is_image:
            mimwrite(output_file, self.plots, duration=0.5)
        else:
            mimwrite(output_file, self.plots, duration=1.0)


    def __generate_colors(self):
        # RGB colors
        if self.num_features == 3:
            colors = [
                        (0, 0, 0),       # black
                        (255, 255, 255), # white
                        (0, 0, 128),     # navy
                        (128, 0, 0),     # maroon
                        (145, 30, 180),  # purple
                        (70, 240, 240),  # cyan
                        (60, 180, 75),   # green
                        (128, 128, 0),   # olive
                        (128, 128, 128), # grey
                        (230, 25, 75),   # red
                        (170, 110, 40),  # brown
                        (255, 225, 25),  # yellow
                        (0, 130, 200),   # blue
                        (240, 50, 230),  # magenta
                        (255, 250, 200), # beige
                        (210, 245, 60),  # lime
                        (250, 190, 190), # pink
                        (0, 128, 128),   # teal
                        (230, 190, 255), # lavender
                        (170, 255, 195), # mint
                        (255, 215, 180), # coral
                    ]
            
            return colors[0:self.num_clust]
        # Grayscale colors
        else:
            return list(np.linspace(0, 255, self.num_clust))
        
        
    def fit(self):
        # Initialize centroids randomly
        self.__initialize_centroids()

        # Update clusters
        self.__update_clusters()

        # Plot initial clusters
        self.__plot_clusters()

        # Loop for max iterations or until convergence
        for iteration in range(self.max_iters - 1):

            # Calculate new centroids
            new_centroids = self.__update_centroids()

            # Check if previous and new centroids are the same
            # Break if convergence is reached
            self.__compare_centroids(new_centroids)

            if self.converged:
                break
            else:
                self.centroids = new_centroids.copy()

            # Update clusters using new centroids
            self.__update_clusters()

            # Plot new clusters
            self.__plot_clusters()

            # Print status update
            print('Iteration:', iteration+1)

        # Output gif file from list of plots/images
        self.__write_gif()

        return self.centroids, self.clusters_idx
