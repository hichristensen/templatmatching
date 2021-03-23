#
# Code from PyImageSearch
# Template matching
#
import argparse
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
                help="path to input image")
ap.add_argument("-t", "--template", type=str, required=True,
                help="path to template image")
args = vars(ap.parse_args())

# Load input image and template from disk and display

print("[INFO] loading image ...")
image = cv2.imread(args["image"])
template = cv2.imread(args["template"])
cv2.imshow("Image", image)
cv2.imshow("Template", image)

# convert image and template to grayscale for matching

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# perform template matching

print("[INFO] performing template matching")
result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(result)
(startX, startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

cv2.rectangle(image, (startX,startY), (endX, endY), (255,0,0), 3)

# show output image

cv2.imshow("Output", image)
cv2.waitkey(0)
