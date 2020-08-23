import cv2 as cv
import numpy as np

image = cv.imread("C:/Users/Shoum/Desktop/face.jpg")

window="image"
width = int(image.shape[1] * 20 / 100)
height = int(image.shape[0] * 20 / 100)
dim = (width, height)
resized = cv.resize(image, dim, interpolation = cv.INTER_AREA)
#cv.imshow(window,resized)
#cv.imwrite("Resized.jpg",resized)


#Greyscale

grey = np.mean(resized,axis=2)
#cv.imwrite("grey.jpg",grey)


#Transpose Image

transpose = resized.transpose(1,0,2)
#cv.imwrite("Transpose_left.jpg",transpose)


#Transpose_right
transpose_right = np.fliplr(transpose)
#cv.imwrite("Transpose_right.jpg",transpose_right)


#Flip
b = resized
flip = np.zeros(resized.shape)
for i in range(resized.shape[1]):
    flip[:,i,:] = b[:,b.shape[1]-i-1,:]
    
    
cv.imwrite("flip.jpg",flip)
cv.waitKey(0)
cv.destroyAllWindows()



#tint
tinted = resized
resized[:,:,0]=0
cv.imwrite("Tint.jpg",tinted)


cv.waitKey(0)
cv.destroyAllWindows()


