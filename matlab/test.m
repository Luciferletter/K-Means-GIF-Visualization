%% RGB image
close all; clearvars; clc;
img_name = './files/images/peppers.png';
input_data = imread(img_name);
figure
imshow(img_name)
[clusters, clusters_idx, centroids] = kmeans_nd(input_data, 10, 25, 'L2', true, img_name, true);


%% RGB image
close all; clearvars; clc;
img_name = './files/images/lena.tif';
input_data = imread(img_name);
figure
imshow(img_name)
[clusters, clusters_idx, centroids] = kmeans_nd(input_data, 10, 25, 'L2', true, img_name, true);


%% Grayscale image
close all; clearvars; clc;
img_name = './files/images/lena_gray.jpg';
input_data = imread(img_name);
figure
imshow(img_name)
[clusters, clusters_idx, centroids] = kmeans_nd(input_data, 10, 25, 'L2', true, img_name, true);


%% 3D data
clearvars; clc;
input_data = [2, 10, 8;
              2, 5, 7;
              8, 4, 1;
              5, 8, 11;
              7, 5, 3;
              6, 4, 9;
              1, 2, 0];

[clusters, clusters_idx, centroids] = kmeans_nd(input_data, 3, 25, 'L2', false, 'None', true);


%% 2D data
close all; clearvars; clc; 
input_data = [2, 10;
              2, 5;
              8, 4;
              5, 8;
              7, 5;
              6, 4;
              1, 2];  

[clusters, clusters_idx, centroids] = kmeans_nd(input_data, 3, 25, 'L2', false, 'None', true);