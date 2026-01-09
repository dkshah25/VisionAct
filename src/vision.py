import cv2
import numpy as np
import pyautogui

def locate_element(template_path):

    screenshot = pyautogui.screenshot()
    screen_np = np.array(screenshot)

    screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

    template = cv2.imread(template_path)
    if template is None:
        raise FileNotFoundError(f"Template image not found at path: {template_path}")
    
    h, w = template.shape[:2]

    result = cv2.matchTemplate(
        screen_bgr,
        template,
        cv2.TM_CCOEFF_NORMED
    )

    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    centre_x = max_loc[0] + w // 2
    centre_y = max_loc[1] + h // 2

    return (centre_x, centre_y, max_val)