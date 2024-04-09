A few scripts for taking images of a solar eclipse. Code was written for an EOS R5 and was not tested with other cameras, so YMMV.
# How to use
1. Install `gphoto2` for python with pip (you may have to install some packages with homebrew/apt/etc. before this)
2. Run `python3 listcameras.py` to make sure that your camera is detected
3. Run `python3 takepics.py` to start the sequence. You will be guided through a few steps. You can manually adjust the `steps` variable in the code to use custom exposure/ISO values.

You may need to run the above python commands with `sudo` for it to actually connect to the camera
