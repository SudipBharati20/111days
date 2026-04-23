import pyautogui
import pyperclip
import time
from config import SHORT_DELAY

def copy_chat_history():
    """
    Select and copy chat history
    NOTE: You may need to adjust coordinates based on your screen
    """
    print("[INFO] Copying chat history...")

    # Click on chat area (adjust coordinates!)
    pyautogui.click(500, 500)
    time.sleep(SHORT_DELAY)

    # Select all text
    pyautogui.hotkey("ctrl", "a")
    time.sleep(SHORT_DELAY)

    # Copy
    pyautogui.hotkey("ctrl", "c")
    time.sleep(SHORT_DELAY)

    return pyperclip.paste()