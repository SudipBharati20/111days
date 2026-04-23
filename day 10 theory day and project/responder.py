import pyautogui
import pyperclip
import time
from config import SHORT_DELAY

def send_response(text):
    """Paste and send message"""
    print("[INFO] Sending response...")

    # Copy response
    pyperclip.copy(text)

    # Click input box (adjust coordinates!)
    pyautogui.click(500, 900)
    time.sleep(SHORT_DELAY)

    # Paste
    pyautogui.hotkey("ctrl", "v")
    time.sleep(SHORT_DELAY)

    # Send
    pyautogui.press("enter")