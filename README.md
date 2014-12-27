OpenHIIT
========

**HIIT (High Intensity Interval Training) Timer App**

* Set the warm up time, number of rounds, work and rest times.
* Defaults to the Tabata settings.
* Stores a history of your settings for easy selection
* 'Start' and 'Complete' counts for each history item
* Text to speech countdown “3,2,1” as each work or rest period ends.
* View the [ScreenShot](https://github.com/bobemoe/OpenHiit/blob/master/screenshot.png)

To Do / Known Bugs
------------------
The .apk provided in the repo is unsigned and will probably not install.  You will need to build and push this to your device yourself. I am working on signing the app. I would like to submit to [F-Droid](https://f-droid.org/) in the near future.

The 'Load from history...' drop down shows info about the saved items (e.g work and rest times, stared and complete counts etc) but is not very clear which number means what unless you know the format:  " (warmup) rounds x work <-> rest [ complete / started ] " this could do with a more user friendly display, and also ordering by the most complete first.

Download
--------
[OpenHIIT-1.0.2-release-unsigned.apk](https://github.com/bobemoe/OpenHiit/blob/master/bin/OpenHIIT-1.0.2-release-unsigned.apk?raw=true)

Build
-----

This project is coded in Python using [Kivy](http://kivy.org).

Only tested on Android, buit by [Buildozer](https://buildozer.io/) on linux using the buildozer.spec provided. 

Should work on iOS and other platforms, but you'll have to build your own package:

http://kivy.org/docs/guide/packaging.html

Credits
-------

Inspired by and based on http://1.log.brandonthomson.com/2009/06/python-based-hiit-workout-timer.html but re-factored so much, that none of the original code exists!

Using https://github.com/brousch/saythis-kivy-intro-app for the Text to Speech.

Using icon from http://www.iconarchive.com/show/oxygen-icons-by-oxygen-icons.org/Apps-preferences-desktop-accessibility-icon.html
