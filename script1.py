import cv2, time

first_frame = None
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (21,21),0) #for better accuracy

    if first_frame is None:
        first_frame = gray
        continue   #skip the rest of the lines in this iteration


    delta_frame = cv2.absdiff(gray, first_frame)
    thres_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]


    thres_frame = cv2.dilate(thres_frame, None, iterations = 2)

    (_,cnts,_) = cv2.findContours(thres_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame", thres_frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

