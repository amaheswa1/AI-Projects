import easyocr
import argparse
import cv2
from gtts import gTTS
from playsound import playsound

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])


print("[Info] Detecting And Recognizing Text..")
reader = easyocr.Reader(['en'],gpu = -1 > 0)
results = reader.readtext(image ,detail = 0,paragraph = True)

print("[Info] Translating Text..")
a = gTTS(text=results[0], lang="en")
a.save("speech.mov")

cv2.putText(image, results[0], (10,  25), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)

cv2.imshow("Image", image)
cv2.waitKey(1000)
playsound("./speech.mov")
cv2.waitKey(0)
