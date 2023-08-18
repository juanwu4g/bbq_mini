import cv2
import mss
import pyautogui
import numpy as np
from pathlib import Path

def input_keys(target_img):
    keys = str(target_img).split('_')
    for key in keys:
        pyautogui.typewrite(key)
        pyautogui.typewrite('space')
    

class BbqImages:
    def __init__(self, img_name):
        self.img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
        self.__name = img_name
    def __str__(self):
        return Path(self.__name).stem
    
a_e = BbqImages('a_e.png')
a_q_w = BbqImages('a_q_w.png')
a_w = BbqImages('a_w.png')

target_images = [a_e, a_q_w, a_w]


with mss.mss() as sct:
    # Part of the screen to capture (2560x1600)
    monitor = {"top": 280, "left": 890, "width": 760, "height": 820}
    while "Screen capturing":
        grey_img = cv2.cvtColor(np.array(sct.grab(monitor)), cv2.COLOR_RGB2GRAY)

        for target_image in target_images:
            result = cv2.matchTemplate(grey_img, target_image.img, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            threshold = 0.7
            if max_val >= threshold:  # Check if the match is above the threshold
                input_keys(target_image)
                # h, w = target_image.shape
                # top_left = max_loc
                # center_x = top_left[0] + w // 2
                # center_y = top_left[1] + h // 2 - 150
                # print(center_x)
                # print(center_y)
                # bottom_right = (top_left[0] + w, top_left[1] + h)
                # cv2.rectangle(grey_img, top_left, bottom_right, (0, 255, 0), 2)
                # cv2.circle(grey_img, (center_x, center_y), 5, (0, 255, 0), -1)
                # cv2.imshow('Template Matching Result', grey_img)
            # else :
            #     print("Target image not found in screenshot.")


        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


# Problem: if the target image is present in the screen, pyautogui will keep input the keystrokes, how to make it only input once