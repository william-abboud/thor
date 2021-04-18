from bs4 import BeautifulSoup


class TorrentsHtmlParser:
    def __init__(self, html_content, torrents_selector):
        # Use html5lib to patch broken HTML
        self.soup = BeautifulSoup(html_content, 'html5lib')
        self.parsed_torrents = self.soup.select(torrents_selector)
