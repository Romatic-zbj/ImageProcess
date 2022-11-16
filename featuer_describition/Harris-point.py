#if there exists edges in more than one direction around the pixel,we think this pixel is Point of Interest
#corner point
#Harris matrix:M=W*M1,W is Gauss filter, M1 is delta(I)delta(I)'
from scipy.ndimage import filters
from PIL import Image
from pylab import *
from numpy import *
def compute_harris_response(im,sigma=3):
    imx=zeros(im.shape)
    filters.gaussian_filter(im,(sigma,sigma),(0,1),imx)
    imy=zeros(im.shape)
    filters.gaussian_filter(im,(sigma,sigma),(0,1),imy)
    Wxx=filters.gaussian_filter(imx*imx,sigma)
    Wxy=filters.gaussian_filter(imx*imy,sigma)
    Wyy=filters.gaussian_filter(imy*imy,sigma)
    Wdet=Wxx*Wyy-2*Wxy
    Wtra=Wxx+Wyy
    return Wdet/Wtra
def get_harris_points(hassim,min_dist=10,threshold=0.1):
    corner_threshold=hassim.max()*threshold
    hassim_t=(hassim>corner_threshold*1)
    #get the coordinates of Candidate point
    coords=array(hassim_t.nonzero()).T
    candidate_values=[hassim[c[0],c[1]] for c in coords]
    index=argsort(candidate_values)

    allowed_location=zeros(hassim.shape)
    allowed_location[min_dist:-min_dist,min_dist:-min_dist]=1
    filtered_coords=[]
    for i in index:
        if allowed_location[coords[i,0],coords[i,1]]==1:
            filtered_coords.append(coords[i])
            allowed_location[(coords[i,0]-min_dist):(coords[i,0]+min_dist),
            (coords[i,1]-min_dist):(coords[i,1]+min_dist)]=0
    return filtered_coords
def plot_harris_points(image,filtered_coords):
    figure()
    gray()
    imshow(image)
    plot([p[1] for p in filtered_coords],[p[0] for p in filtered_coords],'*')
    axis('off')
    show()
if __name__ == "__main__":
    im=array(Image.open('test.PNG').convert('L'))
    harrism=compute_harris_response(im)
    filtered_coords=get_harris_points(harrism,6)
    plot_harris_points(im,filtered_coords)

