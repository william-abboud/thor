from Business.TorrentsHtmlParser import TorrentsHtmlParser
from Kickass.Data.KickassTorrentHtmlData import KickassTorrentHtmlData


def get_torrent_info(tag):
    return KickassTorrentHtmlData(tag)


class KickassTorrentsHtmlParser:
    def __init__(self, html_content):
        self.parser = TorrentsHtmlParser(html_content, '#torrent_latest_torrents')

    def parse(self):
        return list(map(get_torrent_info, self.parser.parsed_torrents))
