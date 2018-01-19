# Python-Motion-Detector
A Python program that can detects moving objects with webcam and log their entry and exit time to/from the camera


# How it works
The script "motion_detector.py" utilizes the **openCV** library to capture video from the default webcam of the 
loacal machine. and we basically store the first frame, which ideally would capture the static background, and then
check every coming frame captured from the camera to see if the difference (delta) in all pixels surpasses the 
set threshold. If it does, we draw rectangular contours on the frame to indicate where the detected objects are. 

After we are able to successfully detect the moving objects, the next step is to record the entry and exit points in 
time and plot a time series with my second script- "plotting.py". The time series chart is plotted with the **bokeh** 
library and we also enable hovering effect to show the time stamps. The only thing left to do is to fine tune the parameters such as the threshold in order to make the detection more accurate.  Pretty fun, right ? 


# Screen Shot 

<img width="1654" alt="screen shot 2018-01-09 at 3 07 17 am" src="https://user-images.githubusercontent.com/19476654/34904129-00ebe058-f7f4-11e7-92f7-9e82980b40a6.png">

<img width="1290" alt="screen shot 2018-01-12 at 11 57 25 pm" src="https://user-images.githubusercontent.com/19476654/35132957-a4839aac-fc82-11e7-8276-af0644ca2faa.png">



# Author 


[@Daniel Huang](https://www.linkedin.com/in/daniel-huang-443546115/)
