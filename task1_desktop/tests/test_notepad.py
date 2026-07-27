from config import (
    TEXT,
    APPEND_TEXT,
    EXPECTED_TEXT,
    FILE_PATH,
)

from utils.file_helper import (
    file_exists,
    read_file,
)


def test_notepad_workflow(notepad):
    """
    Scenario:
    1. Launch Notepad (handled by fixture)
    2. Type text
    3. Append text
    4. Save file
    5. (Bonus) Reopen file and verify content
    """
    notepad.write(TEXT)
    notepad.append(APPEND_TEXT)

    # Verify editor content before saving
    assert notepad.get_text() == EXPECTED_TEXT

    # Save
    notepad.save_as(FILE_PATH)

    # Close current Notepad
    notepad.close()

    # Verify file exists
    assert file_exists(FILE_PATH)

    # Launch again
    notepad.launch()

    # Open the saved file
    notepad.open_file(FILE_PATH)
    
    # Verify content matches expected text
    assert read_file(FILE_PATH) == EXPECTED_TEXT

