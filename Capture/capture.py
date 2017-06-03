import numpy as np
import cv2
import time


for i in range(0, 80):

    # title of video file
    title = str(i) + ".mp4"
    cap = cv2.VideoCapture(title)

    # parsing the title : split the extension
    title_parsing = title.split(".")[0]

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if(ret):
        	now = time.localtime()

        	# save the frame : [title + timestamp(min) + timestamp(sec) . jpg]
        	cv2.imwrite(title_parsing + str(now.tm_min) + str(now.tm_sec) + ".jpg" ,frame)
        
        	if cv2.waitKey(1) & 0xFF == ord('q'):
           		break
        else:
        	break

    cap.release()
    cv2.destroyAllWindows()