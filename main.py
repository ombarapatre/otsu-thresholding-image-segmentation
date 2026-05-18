import cv2

img = cv2.imread('image.jpg', 0)

threshold, result = cv2.threshold(
    img,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

cv2.imwrite('output.jpg', result)

print("Optimal Threshold:", threshold)