from pywinauto import Application, Desktop
import time


class NotepadPage:

    def __init__(self):
        self.app = None
        self.window = None
        self.editor = None

    def launch(self):
        self.app = Application(backend="uia").start("notepad.exe")

        self.window = Desktop(backend="uia").window(
            title_re=".*Notepad$"
        )

        self.window.wait("visible", timeout=10)
        self.window.set_focus()

        self.editor = self.window.child_window(control_type="Document")
        self.editor.wait("ready", timeout=10)

    def click_edit_button(self):
        edit_btn = self.window.child_window(
            title="Edit",
            auto_id="Edit",
            control_type="MenuItem"
            )

        edit_btn.click_input()

        print("============ Control Identifiers ==============")
        self.window.print_control_identifiers(filename = r"output/control_identifiers.txt")

    def write(self, text):
        self.editor.iface_value.SetValue(text)

    def append(self, text):
        current = self.editor.window_text()
        self.editor.iface_value.SetValue(current + text)

    def get_text(self):
        return self.editor.window_text()

    def save_as(self, file_path):
        self.window.type_keys("^s")

        save_dialog = self.window.child_window(
            title="Save as",
            control_type="Window"
        )

        save_dialog.wait("visible", timeout=10)

        filename = save_dialog.child_window(
            auto_id="1001",
            control_type="Edit"
        )

        filename.set_edit_text(file_path)

        save_dialog.child_window(
            auto_id="1",
            control_type="Button"
        ).click()

        # overwrite confirmation
        try:
            confirm = self.window.child_window(
                title_re="Confirm Save As",
                control_type="Window"
            )

            confirm.wait("visible", timeout=2)

            confirm.child_window(
                title="Yes",
                control_type="Button"
            ).click()

        except Exception:
            pass

    def open_file(self, file_path):
        self.window.type_keys("^o")

        open_dialog = self.window.child_window(
            title="Open",
            control_type="Window"
        )

        open_dialog.wait("visible", timeout=10)

        filename = open_dialog.child_window(
            auto_id="1148",
            control_type="Edit"
        )

        filename.set_edit_text(file_path)

        open_dialog.child_window(
            title="Open",
            control_type="Button",
            auto_id="1"
        ).click()
                
    def close(self):
        self.window.set_focus()
        self.window.type_keys("^W")
        time.sleep(0.5)
        if self.window.exists():            
            self.window.close()