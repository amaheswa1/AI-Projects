import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"]) # reads image
cv2.imshow("Image",image)
cv2.waitKey(0)

resize = imutils.resize(image, width = 500, inter = cv2.INTER_CUBIC)
cv2.imshow("resize", resize)
cv2.waitKey(0)

rotate = imutils.rotate(image,10,center=(10,10))
cv2.imshow("rotate", rotate)
cv2.waitKey(0)

(B,G,R) = cv2.split(image)

cv2.imshow("R",R)
cv2.waitKey(0)
cv2.imshow("G",G)
cv2.waitKey(0)
cv2.imshow("B",B)
cv2.waitKey(0)
merge = cv2.merge([B,G,R])
cv2.imshow("merged",merge)
cv2.waitKey(0)

cv2.rectangle(image,(100,30),(275,200),(0,0,255),2)
cv2.circle(image, (140, 133), 20, (0, 0, 255), 0)
cv2.imshow("Drawing", image)
cv2.waitKey(0)

cv2.putText(image, "OpenCV", (10,  25), cv2.FONT_HERSHEY_SIMPLEX,
	0.8, (0,0,255), 2)
cv2.imshow("Text",image)
cv2.waitKey(0)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)



