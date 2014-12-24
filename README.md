OpenHIIT
========

**HIIT (High Intensity Interval Training) Timer App**

Currently bare bones, but fully functional. [ScreenShot](https://github.com/bobemoe/OpenHiit/blob/master/screenshot.png)

* Set the warm up time, number of rounds, work and rest times.
* Text to speech countdown “3,2,1” as each work or rest period ends.
* Defaults to the Tabata settings.
* Stores a history of your settings for easy selection
* 'Start' and 'Complete' counts for each history item



Download
--------
[OpenHIIT-1.0.2-release-unsigned.apk](https://github.com/bobemoe/OpenHiit/blob/master/bin/OpenHIIT-1.0.2-release-unsigned.apk?raw=true)

Build
-----

This project is coded in Python using [Kivy](http://kivy.org).

Only tested on Android and can be built using [Buildozer](https://buildozer.io/) and the buildozer.spec provided. 

Should work on iOS and other platforms, but you'll have to build your own package:
http://kivy.org/docs/guide/packaging.html

Credits
-------

Inspired by and based on http://1.log.brandonthomson.com/2009/06/python-based-hiit-workout-timer.html but re-factored so much, that none of the original code exists!

Using https://github.com/brousch/saythis-kivy-intro-app for the Text to Speech.

Using icon from http://www.iconarchive.com/show/oxygen-icons-by-oxygen-icons.org/Apps-preferences-desktop-accessibility-icon.html
