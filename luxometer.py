#-------------------------------------------------------------------------------
# Name:        Luxometer
# Purpose:     Measures light for use in sleep research
#
# Author:      Miles Gordenker
#
# Created:     13/07/2012
# Copyright:   (c) Miles Gordenker 2012
# Licence:     For Rob's eyes only
#-------------------------------------------------------------------------------
import cv
import cv2
import time


def displaySample(seconds):
    cv.NamedWindow("Image Captured for Analysis", 1)
    capture = cv.CreateCameraCapture(-1)

    width = None #leave None for auto-detection
    height = None #leave None for auto-detection

    if width is None:
        width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))
        print "here is the width of the capture window:"
        print width
    else:
    	cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,width)

    if height is None:
    	height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
        print "here is the height of the capture window:"
        print height
    else:
    	cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,height)

    img = cv.QueryFrame(capture)
    cv.ShowImage("Image Captured for Analysis", img)
    cv2.waitKey(10)

    img = cv.QueryFrame(capture)
    cv.ShowImage("Image Captured for Analysis", img)
    cv2.waitKey(seconds*1000)

    cv.DestroyWindow("Image Captured for Analysis")

def estimateLux():
    capture = cv.CreateCameraCapture(-1)

    width = None #leave None for auto-detection
    height = None #leave None for auto-detection

    if width is None:
        width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))
        print "here is the width:"
        print width
    else:
    	cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,width)

    if height is None:
    	height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
        print "here is the height:"
        print height
    else:
    	cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,height)

    img = cv.QueryFrame(capture)
    cv2.waitKey(10)

    img = cv.QueryFrame(capture) # so we currently have BGR image
    img = cv.GetMat(img, allowND=0) # iplImage -> CvMat

    #initialize placeholders for BGR values

    # get a CvScalar (tuple) with the sum of each of the 3 channels
    resultsTuple = cv.Sum(img)

    #return results as a list in RGB order for simplicty's sake
    pixels = height * width
    statsRGB = list([resultsTuple[2]/pixels, resultsTuple[1]/pixels, resultsTuple[0]/pixels])

    #calculate the light index using formula found at autohotkey.com
    red = statsRGB[0]
    green = statsRGB[1]
    blue = statsRGB[2]

    lux = (red*.229) + (green*.587) + (blue*.114)
    statsRGB.insert(0, lux)

    return statsRGB

def main():
    #demos the script provided there is no preexisting main function
    displaySample(5)
    print estimateLux()

if __name__ == '__main__':
    main()
