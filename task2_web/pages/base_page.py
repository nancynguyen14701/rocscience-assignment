from playwright.sync_api import Page


class BasePage:
    base_url = None

    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def url(self) -> str:
        return self.page.url