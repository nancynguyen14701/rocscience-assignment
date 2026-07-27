from pages.base_page import BasePage
from config import AUTHEN_URL

class LoginPage(BasePage):
    @property
    def email_input(self):
        return self.page.locator("input[type='email'], input[name='email'], input[name='username'], input[name='login']")

    @property
    def password_input(self):
        return self.page.locator("input[type='password'], input[name='password']")

    @property
    def login_button(self):
        return self.page.locator("button[type='submit'], button:has-text('Log in'), button:has-text('Login')")

    def is_login_url(self) -> bool:
        return AUTHEN_URL in self.page.url

    def is_email_visible(self) -> bool:
        return self.email_input.first.is_visible()

    def is_password_visible(self) -> bool:
        return self.password_input.first.is_visible()

    def is_login_button_visible(self) -> bool:
        return self.login_button.first.is_visible()

    def is_login_button_enabled(self) -> bool:
        return self.login_button.first.is_enabled()
