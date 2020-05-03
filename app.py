import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record(): 
    last_time = time.time()
    while True:
        printscreen_pil =  ImageGrab.grab(bbox=(260,150,720,620))
        print("Loop took {} seconds".format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',np.array(printscreen_pil))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()