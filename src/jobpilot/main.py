import time
import pyautogui


def main():
    print("JobPilot starting...")

    print("Opening Chrome...")
    pyautogui.hotkey("ctrl", "l")
    pyautogui.write("https://www.google.com", interval=0.03)
    pyautogui.press("enter")

    time.sleep(3)

    print("Moving mouse...")
    pyautogui.moveTo(600, 400, duration=1)

    print("Scrolling...")
    pyautogui.scroll(-5)

    time.sleep(2)

    print("JobPilot test complete.")


if __name__ == "__main__":
    main()