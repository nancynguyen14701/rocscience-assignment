import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestRocPortalLogin:

    @pytest.mark.ab1
    def test_login_page_elements(self, page):
        # Arrange
        home = HomePage(page).open()

        # Act
        home.click_profile_icon()
        home.click_login_to_portal()

        # Assert
        login = LoginPage(page)

        assert login.is_login_url(), "Expected to be redirected to the RocPortal login page."
        assert login.is_email_visible(), "Expected the email field to be visible."
        assert login.is_password_visible(), "Expected the password field to be visible."
        assert login.is_login_button_visible(), "Expected the Login button to be visible."
        assert login.is_login_button_enabled(), "Expected the Login button to be enabled."