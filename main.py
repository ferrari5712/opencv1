import cv2

img = cv2.imread("IMG_1116.JPG", cv2.IMREAD_COLOR)
copy_img = img.copy()
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg', img2)
blur = cv2.GaussianBlur(img2, (3, 3), 0)
cv2.imwrite('blur.jpg', blur)

for i in range(100, 255):
    canny = cv2.Canny(blur, 100, i)
    cv2.imshow('canny', canny)
    print(i)
    cv2.waitKey(500)

# canny = cv2.Canny(blur, 100, 255)

# cv2.imwrite('canny.jpg', canny)
#
# sobel = cv2.Sobel(img2, cv2.CV_8U, 1, 0, 3)
# cv2.imwrite('sobel.jpg', sobel)
#
# laplacian = cv2.Laplacian(img2, cv2.CV_8U, ksize=3)
# cv2.imwrite('laplacian.jpg', laplacian)
#
# cv2.imshow('laplacian', laplacian)
# cv2.waitKey()

# cv2.imshow("sobel", cv2.Sobel(img2, cv2.CV_8U, 1, 0, 3))

