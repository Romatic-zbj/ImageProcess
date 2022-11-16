import PIL
from pylab import *
from PIL import Image
from scipy.ndimage import filters
from numpy import *
testPicture=Image.open('test.png')
#testPicture.show()
im=array(testPicture)
print(im.shape)
im3=Image.fromarray(im)

# im3.show()
im2=ones(im.shape)*255
# im2=zeros(im.shape)
for i in range(3):
    im2[:,:,i]=filters.gaussian_filter(im[:,:,i],3)
    print(im2)
im2=uint8(im2)
im4=im/im2
# print(im2)
# im2=Image.fromarray(im2)
# im2.show()
im4=Image.fromarray(im4)
# print(im2)
im4.save('test3.PNG')


