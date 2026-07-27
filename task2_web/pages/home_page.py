from pages.base_page import BasePage
from config import URL

class HomePage(BasePage):

    def open(self) -> "HomePage":
        self.page.goto(URL, wait_until="domcontentloaded")
        self.page.wait_for_selector("#portal-icon-container")
        self.dismiss_cookie_banner()
        return self

    def dismiss_cookie_banner(self) -> "HomePage":
        try:
            accept_btn = self.page.locator("button:has-text('Accept'), #onetrust-accept-btn-handler")
            accept_btn.wait_for(state="visible", timeout=10000)
            accept_btn.click()
        except Exception:
            pass
        return self

    def click_profile_icon(self) -> "HomePage":
        self.page.wait_for_selector(".portal-dropdown-toggle")
        self.page.locator(".portal-dropdown-toggle").click()
        self.page.wait_for_selector(".account-dropdown-item")
        return self

    def click_login_to_portal(self) -> None:
        self.page.locator("text=Log in to RocPortal").click()
        self.page.wait_for_load_state("domcontentloaded")
