import pyautogui
import time
import pyperclip

# Step 1: click the whatsaap icon
pyautogui.click(1155, 874,  button='left')
time.sleep(1)

# Step 2: drag to select text
pyautogui.moveTo(431, 137)
pyautogui.dragTo(1481, 779, duration=1.0, button='left')


# Step 3: copy selected text
pyautogui.hotkey('ctrl', 'c')

time.sleep(0.5)

# Step 4: get clipboard content into variable
copied_text = pyperclip.paste()

print("Copied Text:")
print(copied_text)
