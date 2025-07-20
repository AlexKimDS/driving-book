from playwright.sync_api import sync_playwright


class DVSAWebCrawler:
    """A simple crawler to load the DVSA booking site."""

    def __init__(self, base_url: str = "https://driverpracticaltest.dvsa.gov.uk/application"):
        self.base_url = base_url

    def fetch_homepage(self) -> str:
        """Navigate to the base URL and return page HTML."""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.base_url)
            content = page.content()
            browser.close()
            return content
