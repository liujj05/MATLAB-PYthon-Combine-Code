# coding: utf-8
# 2017-12-06
# 达到快速开发的目的，希望能够实现Python与MATLAB的混合编程
import matlab.engine
eng = matlab.engine.start_matlab()

# OK
# tf = eng.isprime(37)
# print tf

# No OK
res = eng.GetRowColOfImage('test_img.jpg')
print res

# OK
# ret = eng.triarea(1.0, 5.0)
# print ret

# OK
# eng.ImageScript(nargout=0)

