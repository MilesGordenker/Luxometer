Version: 1.0 (First public release)

Description:

Luxometer is a tool for estimating ambient light levels using your webcam. The algorithm works by capturing a frame from your webcam, then weighting the RGB values of each pixel to estimate how bright the room is. 

Dependencies:

Luxometer has only been tested in Windows 7 with openCV 2.4 and Python 2.72 installed. Earlier versions of openCV should work, but make sure your version supports the Mat() class.

In theory, Luxometer should work just fine on any hardware running openCV with the python bindings.

Usage and Limitations:

Simply point your computer's webcam towards an unchanging part of the room. Since the algorithm relies on color to make its estimates, something as trivial as moving a green shirt into the webcam's field of vision can skew your results. To be on the safe side, you might consider pointing the webcam at the ceiling.

I anticipate two main use cases for the script- tracking fluctuations in ambient light levels at a single location, and testing to see whether a room is dark enough to facilitate deep sleep. It SHOULD NOT be used to compare the ambient light levels of two different locations, unless both places are very dark.

Documentation and Testing:

estimateLux() is the worker method of Luxometer. It returns a python list formatted like so: [lux, average R value of all pixels, averge G value, average B value]. In general, an increasing lux value signifies that the room is becoming darker. This trend stops as the webcam's environment approaches pitch darkness- complete darkness yields a lux value of 0.

displaySample(seconds) flashes what the webcam sees on screen for the duration of time specified using the parameter "seconds". This can be used to verify the operation of the webcam, and check to make sure the lux readings correspond to its field of view. Display sample also prints the dimensions of the webcam's capture window to console.

