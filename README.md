# MATLAB PYthon Combine-Code

## 1. 准备工作
在MATLAB的官方网站，有关于如何为Python安装MATLAB API的[指导教程](http://cn.mathworks.com/help/matlab/matlab_external/get-started-with-matlab-engine-for-python.html)

## 2. 相关代码
### 2.1 Python当中的
	import matlab.engine
	eng = matlab.engine.start_matlab()
	res = eng.GetRowColOfImage('test_img.jpg')
	print res
### 2.2 对应的MATLAB当中的
	function res = GetRowColOfImage(filename)
	    % filename = 'test_img.jpg';
	    test_mat = imread(filename);
	    row = size(test_mat,1);
	    col = size(test_mat,2);	    
	    res = [row, col];
	end
### 2.3 代码解释
两部分的程序文件需要放在同一个路径下。输入输出参数似乎不用作特殊处理。