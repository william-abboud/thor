from Business.TorrentsFinder import TorrentsFinder
from Kickass.Business.KickassTorrentsHtmlParser import KickassTorrentsHtmlParser
from Kickass.Data.KickassTorrentsUrlProvider import KickassTorrentsUrlProvider


def main(query, preferences):
    kickass_provider = KickassTorrentsUrlProvider(query)
    kickass_torrents_content = kickass_provider.get_torrents()
    kickass_parser = KickassTorrentsHtmlParser(kickass_torrents_content)
    kickass_torrents = kickass_parser.parse()
    finder = TorrentsFinder(kickass_torrents, preferences, query)
    best_match = finder.find_best_match()
    finder.download_torrent(best_match)

    return best_match
