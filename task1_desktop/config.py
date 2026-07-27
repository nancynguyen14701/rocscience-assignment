import os

NOTEPAD_PATH = r"C:\Windows\System32\notepad.exe"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
FILE_NAME = "desktop_automation.txt"
FILE_PATH = os.path.join(OUTPUT_DIR, FILE_NAME)

TEXT = "Desktop automation test"
APPEND_TEXT = " \u2013 completed"
EXPECTED_TEXT = TEXT + APPEND_TEXT
