import numpy as np
import cv2
import time


title = "sample.mp4";
cap = cv2.VideoCapture(title)
title_parsing = title.split(".")[0]

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    if(ret):
    	now = time.localtime()
    	cv2.imwrite(title_parsing + str(now.tm_min) + str(now.tm_sec) + ".jpg" ,frame)
    
    	if cv2.waitKey(1) & 0xFF == ord('q'):
       		break
    else:
    	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()