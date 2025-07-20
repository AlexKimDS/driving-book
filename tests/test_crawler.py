import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import MagicMock, patch

from driving_book import crawler


def test_fetch_homepage_returns_html():
    mock_playwright = MagicMock()
    mock_browser = MagicMock()
    mock_page = MagicMock()
    mock_page.content.return_value = '<html>ok</html>'
    mock_browser.new_page.return_value = mock_page
    mock_playwright.chromium.launch.return_value = mock_browser

    with patch('driving_book.crawler.sync_playwright') as sync_playwright:
        sync_playwright.return_value.__enter__.return_value = mock_playwright
        c = crawler.DVSAWebCrawler(base_url='http://example.com')
        html = c.fetch_homepage()
        assert html == '<html>ok</html>'
        mock_browser.new_page.assert_called_once()
        mock_page.goto.assert_called_with('http://example.com')
