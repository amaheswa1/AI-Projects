import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Image",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)

blurry = cv2.GaussianBlur(image, (9,9),0)
cv2.imshow("blurry",blurry)
cv2.waitKey(0)

dialate = cv2.dilate(blurry,None,iterations=2)
cv2.imshow("Dialated",dialate)
cv2.waitKey(0)

erode = cv2.erode(gray,None,iterations = 2)
cv2.imshow("eroded",erode)
cv2.waitKey(0)

grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
cv2.waitKey(0)

(t, thresh) = cv2.threshold(blurred, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("Otsu's Threshold: {}".format(t), thresh)
cv2.waitKey(0)


t = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,1)
cv2.imshow(" Adaptive Threshold",t)
cv2.waitKey(0)