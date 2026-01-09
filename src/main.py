import time
from vision import locate_element
from actions import click_human_like
from config import CONFIDENCE_THRESHOLD, SCAN_INTERVAL, CLICK_DELAY
import os

EXECUTED = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, "assets", "target.png")


print("[VisionAct] Engine Started")

while True:
    x, y, confidence = locate_element(TEMPLATE_PATH)

    print(f"[VisionAct] Match Confidence: {confidence:.2f}")

    if confidence >= CONFIDENCE_THRESHOLD and not EXECUTED:
        EXECUTED = True
        click_human_like(x, y, CLICK_DELAY)
        break
    else:
        print("[VisionAct] Confidence too low. Waiting...")

    time.sleep(SCAN_INTERVAL)

print("[VisionAct] Task Completed Safely.")