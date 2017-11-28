function [clusters, clusters_idx, centroids] = kmeans_nd(input_data, num_clust, max_iters, metric, image, image_fname, gif)
% KMEANS_ND  Perform K-means clustering on data with 2-3 Features or RGB
% images.
%   Inputs:
%   input_data	: input data (2-D array or image or 3-D image)
%   num_clust	: (int) k number of clusters to divide data into
%   max_iters	: (int) maximum iterations to loop for
%   metric		: (string) Distance metric Available(‘L1’, ‘L2’, ‘Cosine’)
%   image		: (bool) Set if input data is an image
%   image_fname : (string) Saves output including this filename
%   gif         : (bool) Set if .gif file is desired to be created from images or plots
%
%   Outputs:
%   clusters     : (cell) array of input data values in each cluster
%   clusters_idx : (cell) array of input data indices in each cluster
%   centroids    : (cell) array of centroid values of each cluster               

    % Preprocess images to 2D array via (H,W,C) -> (H*W, C)
    if image
       img_dims = size(input_data);
       input_data = reshape(input_data, img_dims(1)*img_dims(2), img_dims(3));
       input_data = single(input_data);
    end

    % Initialize centroids as random points
    dims = size(input_data);
    num_points = dims(1);
    num_features = dims(end);
    rand_idx = randperm(num_points, num_clust);
    centroids = num2cell(input_data(rand_idx, :), numel(dims));
    
    % If dimensions are > 3 unable to plot data
    if num_features > 3
        warning('Plotting number of features not supported')
        close
    end
    
    % create plot colors which are repeatable(only necessary for plotting)
    rng('default');
    rng(5);
    colors = rand(num_clust, 3);
            
    % Assign initial clusters
    [centroids, clusters_idx, clusters] = batch_update(input_data, centroids, num_clust, metric);
    
    % Repeat for max iterations or until no change during update
    iter = 1; change = true;
    while iter <= max_iters && change==true
        
        % Recalculate centroids
        centroids = update_centroids(clusters, num_clust);
        
        % Update clusters
        [centroids, updated_clusters_idx, updated_clusters] = batch_update(input_data, centroids, num_clust, metric);
        
        % If no change then break
        if isequal(clusters_idx, updated_clusters_idx)
            change = false;
        end
        
        % Overwrite old clusters
        clusters = updated_clusters;
        clusters_idx = updated_clusters_idx;
        
        % Display as image or plot
        if image
            plot_kmeans_img(input_data, centroids, clusters, clusters_idx, img_dims, num_clust, iter, image_fname, gif, false)
        else
            plot_kmeans(centroids, clusters, num_clust, num_features, colors, iter, gif, false)
        end
        
        % Print current iteration to track progress
        fprintf('Iteration %u of %u\n', iter, max_iters);
        iter = iter + 1;
    end
    
    % Save final image or plot
    if image
        plot_kmeans_img(input_data, centroids, clusters, clusters_idx, img_dims, num_clust, iter, image_fname, false, true)
    else
        plot_kmeans(centroids, clusters, num_clust, num_features, colors, iter, false, true)
    end
        
    close all
    
    
    
%%%%%% Update clusters
    function [centroids, new_clusters_idx, new_clusters] = batch_update(data, centroids, num_clust, metric)
        % Preallocate arrays for efficiency
        % Note: This is necessary for images with many pixels
        new_clusters = cell(num_clust, 1);
        new_clusters_idx = repmat({false(size(data, 1), 1)}, num_clust, 1);
        
        centroids = cell2mat(centroids);
        
        % For every data point calculate the nearest centroid
        for i=1:size(data, 1)
            
            % Calculate distance between each point and each centroid         
            distances = distance_metric(repmat(data(i, :), num_clust, 1), centroids, metric);
            
            % Index centroid with minimum distance from current point
            % and concatenate point to corresponding cluster
            [~, min_idx] = min(distances);
            new_clusters_idx{min_idx}(i, :) = true;
        end
        
        % Remove all NaN values and get clusters from cluster idx
        for k=1:num_clust
            new_clusters{k} = data(new_clusters_idx{k}, :);
        end

        centroids = num2cell(centroids, 2);
        
        % Drop empty clusters and centroids
        [centroids, new_clusters, new_clusters_idx] = drop_empty(new_clusters, new_clusters_idx, centroids);
    end


%%%%%% Distance metric between centroid and current point
   function d = distance_metric(a, b, metric)
       if strcmp(metric, 'L1')
           d = sum(abs(a - b), 2);         
       elseif strcmp(metric, 'L2')
           d = sum((a-b).^2, 2);     
       % Cosine is currently not working correctly
       elseif strcmp(metric, 'Cosine')
           d = dot(a, b, 2) ./ dot(sqrt(sum(a.^2, 2)), sqrt(sum(b.^2, 2)), 2);          
       else
           error('Unknown distance metric');
       end
   end


%%%%%% Update centroids via averaging cluster points by dimension
    function centroids = update_centroids(clusters, num_clust)
        centroids = cell(num_clust, 1);
        for i=1:size(clusters, 1)
            centroids{i} = mean(clusters{i}, 1);
        end
    end


%%%%%% Removes empty clusters and centroids
    function [centroids, clusters, clusters_idx] = drop_empty(clusters, clusters_idx, centroids)
        nan_idx = cellfun(@isempty, clusters);
        if ~isempty(nan_idx)
            centroids = centroids(~nan_idx);
            clusters = clusters(~nan_idx);
            clusters_idx = clusters_idx(~nan_idx);
        end
    end


%%%%%% Plot centroids and clusters
    function plot_kmeans(centroids, clusters, num_clust, num_features, colors, iter, gif, save_last)
        
        if iter==1
            figure
        end
        
        % Clear figure
        clf
        
        % Plot 2D scatter plot
        if num_features == 2
            % Create empty 2D scatter plot and hold
            scatter(NaN, NaN)
            set(gca, 'XTickLabel', [], 'YTickLabel', [], 'ZTickLabel', [])
            hold on
            
            for k=1:size(clusters, 1)
                scatter(clusters{k}(:, 1), clusters{k}(:, 2), 100, colors(k, :), '.')
                scatter(centroids{k}(1), centroids{k}(2), 50, colors(k, :), 'filled', ...
                        'MarkerEdgeColor', 'k', 'LineWidth', 1)                
            end
            
        % Plot 3D scatter plot
        elseif num_features == 3
            % Create empty 3D scatter plot and hold
            scatter3(NaN, NaN, NaN)
            set(gca, 'XTickLabel', [], 'YTickLabel', [], 'ZTickLabel', [])
            hold on
            
            for k=1:size(clusters, 1)
                scatter3(clusters{k}(:, 1), clusters{k}(:, 2), ...
                         clusters{k}(:, 3), 100, colors(k, :), '.')              
                scatter3(centroids{k}(1), centroids{k}(2), centroids{k}(3), ...
                         60, colors(k, :), 'filled', 'MarkerEdgeColor', 'k', ...
                         'LineWidth', 1)      
            end     
        end
            
            
        % Create gif if desired
        if gif
            % Setup figure in format for gif
            fname = strcat(num2str(num_features), {'_feat_'}, {'clust_'}, ...
                           num2str(num_clust), {'.gif'});
            frame = getframe;
            img = frame2im(frame);
            [imgind, cm] = rgb2ind(img, 256);
                       
            if iter==1
                % Creates initial gif
                imwrite(imgind, cm, fname{1}, 'gif', 'Loopcount', Inf);
            else
                % Add figure to gif
                imwrite(imgind, cm, fname{1}, 'gif', 'WriteMode', 'append');
            end
        end
        
        % If process ended, save finished clustered image
        if save_last
            fname = strcat(num2str(num_features), {'_feat_'}, num2str(num_clust),...
                           {'_clust_'}, {'iter_'}, num2str(iter), {'.png'}); 
            print(fname{1}, '-dpng');
        end
    end     


%%%%%% Plot kmeans image
    function plot_kmeans_img(img, centroids, clusters, clusters_idx, img_dims, num_clust, iter, image_fname, gif, save_last)
        
        % Create initial figure
        if iter==1
            figure
            hold on
        end
        
        % Reshape array to image
        for k=1:num_clust
            img(clusters_idx{k}, :) = repmat(uint8(centroids{k}), size(clusters{k}, 1), 1);
        end
        
        % Display image
        img = uint8(reshape(img, img_dims));
        imshow(img)
                
        % Create gif if desired
        if gif
            % Setup image in format for gif
            fname = strcat(image_fname(1:end-4), {'_'}, num2str(num_clust), ...
               {'_clust_'}, {'.gif'});
            [img, cm] = rgb2ind(img, 256);
            
            if iter==1
                % Creates initial gif
                imwrite(img, cm, fname{1},'gif', 'Loopcount',inf);
            else
                % Add figure to gif
                imwrite(img, cm, fname{1},'gif','WriteMode','append');
            end
        end
        
        % If process ended, save finished clustered image
        if save_last
            fname = strcat(image_fname(1:end-4), {'_'}, num2str(num_clust), ...
               {'_clust_'}, {'iter_'}, num2str(iter), {'.png'}); 
            imwrite(img, fname{1});
        end
    end     
end

