function res = GetRowColOfImage(filename)

    % filename = 'test_img.jpg';
    test_mat = imread(filename);
    row = size(test_mat,1);
    col = size(test_mat,2);
    
    res = [row, col];
end
