from urllib.parse import unquote

from Data.TorrentData import TorrentData


class KickassTorrentHtmlData(TorrentData):
    def __init__(self, tag):
        name = tag.select_one('.torrentname .cellMainLink').text
        size = tag.select_one('.nobr').text
        link = tag.select_one('a[data-download]').attrs['href']
        download_link = unquote(unquote(link))
        magnet_link = download_link.split('?url=')[1]

        try:
            seeders = int(tag.select_one('.green.center').text)
        except ValueError:
            seeders = 0

        super().__init__(name, size, magnet_link, seeders)
