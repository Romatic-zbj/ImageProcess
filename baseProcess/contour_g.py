from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *
im=Image.open('test.PNG').convert('L')
im=array(im)
imx=zeros(im.shape)
filters.sobel(im,1,imx)
imy=zeros(im.shape)
filters.sobel(im,0,imy)
magnitude=sqrt(imx**2+imy**2)
print(magnitude.shape)
im2=Image.fromarray(magnitude)
im2.show()