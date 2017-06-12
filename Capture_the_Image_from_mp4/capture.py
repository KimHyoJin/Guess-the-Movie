import numpy as np
import cv2
import time


for i in range(0, 6):
    # title of video file

    title = str(i) + ".mp4"
    cap = cv2.VideoCapture(title)
    number = 0
    count = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if count == 24:
            if(ret):
                now = time.localtime()
            	# save the frame : [title + #number . jpg]
            	cv2.imwrite(str(i) + "_" + str(number) + ".jpg" ,frame)
                number = number + 1
               
                if (cv2.waitKey(1) & 0xFF) == ord('q'):
               	    break
            else:
            	break

            count = 0

        else:
            count = count+1

    cap.release()
    cv2.destroyAllWindows()