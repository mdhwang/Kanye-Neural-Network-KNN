import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui





def process_img(original_image,sigma=0.33):
    v = np.median(original_image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, lower, upper)
    return processed_img



def screen_record(): 
    # last_time = time.time()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(64,150,720,620)))
        new_screen = process_img(screen)
        # print("Loop took {} seconds".format(time.time()-last_time))
        # last_time = time.time()
        print("down")
        pyautogui.keyDown('left')
        time.sleep(1)
        print('up')
        pyautogui.keyUp('left')
        cv2.imshow('window',new_screen)
        # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

screen_record()