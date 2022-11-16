from pylab import *
from PIL import Image
from scipy.ndimage import filters
from numpy import *
im=array(Image.open('out3.PNG').convert('L'))
figure()
# gray()#是否使用颜色空间
a=contour(im,origin='image')#轮廓
axis('equal')
axis('off')
show()