import cv2, time, pandas
from datetime import datetime

first_frame = None
video = cv2.VideoCapture(0)  #0 is the default camera (webcam) of my computer
status_list = [None, None]  #to prevent index out of bound error at the beginning
times = []
df = pandas.DataFrame(columns= ["Start", "End"])


time.sleep(2)
while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (21, 21), 0)  # for better accuracy

    if first_frame is None:
        first_frame = gray
        continue  # skip the rest of the lines in this iteration

    delta_frame = cv2.absdiff(first_frame,gray)
    thres_frame = cv2.threshold(delta_frame, 80, 255, cv2.THRESH_BINARY)[1]
    thres_frame = cv2.dilate(thres_frame, None, iterations=2)

    # find all contours in the thres_frame
    (_, cnts, _) = cv2.findContours(thres_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # filter the contours that have more than 1000 pixels
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        else:
            status = 1   #first object found entering the frame
            # draw a rectangle around the contour
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)  # green rectangle

    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())



    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thres_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())  #treat quitting as the last exit time
        break
    #end of loop

print(status_list)
print(times)

for i in range(0, len(times),2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index= True)

df.to_csv("Times.csv") #output the csv file for plotting
video.release()
cv2.destroyAllWindows()
