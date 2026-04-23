import pyautogui
import time
from config import SHORT_DELAY, LONG_DELAY

def open_chat_app():
    """Open Chrome and chat app"""
    print("[INFO] Opening Chrome...")

    pyautogui.press("win")
    time.sleep(SHORT_DELAY)

    pyautogui.write("chrome")
    time.sleep(SHORT_DELAY)

    pyautogui.press("enter")
    time.sleep(LONG_DELAY)

def wait_for_app():
    """Wait for chat app to load"""
    print("[INFO] Waiting for app to load...")
    time.sleep(LONG_DELAY)