import pytest

from pages.notepad_page import NotepadPage

@pytest.fixture
def notepad():
    page = NotepadPage()
    page.launch()
    yield page
    page.close()
