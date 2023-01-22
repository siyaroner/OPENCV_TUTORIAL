import cv2 as cv
import numpy as np

img=cv.imread("data/photos/ayasofyacami.jpg")
cv.imshow("AyasofyaCami",img)

# blank=np.zeros(img.shape[:2],dtype="uint8")
blank=np.ones(img.shape[:2],dtype="uint8")*255
cv.imshow("blank",blank)


b,g,r=cv.split(img)
cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

# blue=cv.merge([b,blank,blank])
# green=cv.merge([blank,g,blank])
# red=cv.merge([blank,blank,r])
# cv.imshow("Blue",blue)
# cv.imshow("Green",green)
# cv.imshow("Red",red)
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged_img=cv.merge([b,g,r])
cv.imshow("Merged",merged_img)


cv.waitKey( )
cv.destroyAllWindows()

