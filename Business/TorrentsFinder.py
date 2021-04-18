from fuzzywuzzy import fuzz

from Exceptions.TorrentMatchNotFoundException import *
from Utils.utils import open_magnet


def is_torrent_over_min_gb(torrent_info):
    # TODO: Handle size_with_unit could fail
    # TODO: Add preferences
    size, unit = torrent_info.size.split(' ')

    return unit == 'GB' and (float(size) > 2)


def is_torrent_hd(result_info):
    # TODO: HD Should be preference
    return '1080p' in result_info.name


def is_result_good_match(torrent_info, search_query):
    match_percentage = fuzz.ratio(search_query, torrent_info.name)

    # TODO: Percentage should be configurable
    return match_percentage > 20


def find_torrents_over_min_size(torrents_list):
    return list(filter(is_torrent_over_min_gb, torrents_list))


def find_torrents_with_hd(torrents_list):
    return list(filter(is_torrent_hd, torrents_list))


def find_best_torrent_match(torrents_list):
    return sorted(torrents_list, key=lambda m: m.seeders, reverse=True)[0]


def has_torrent_min_seeders(torrent, min_num_seeders):
    try:
        return torrent.seeders >= min_num_seeders
    except ValueError:
        return False


def find_torrents_with_min_seeders(torrents_list, min_seeders):
    return list(filter(lambda t: has_torrent_min_seeders(t, min_seeders), torrents_list))


def find_torrents_that_best_match(torrents_list, search_query):
    return list(filter(lambda t: is_result_good_match(t, search_query), torrents_list))


def download_torrent_from_magnet_link(magnet_link):
    open_magnet(magnet_link)


class TorrentsFinder:
    def __init__(self, torrents, preferences, search_query):
        self.torrents = torrents
        self.preferences = preferences
        self.search_query = search_query

    def find_best_match(self):
        try:
            min_size_torrents = find_torrents_over_min_size(self.torrents)
            min_seeders_torrents = find_torrents_with_min_seeders(min_size_torrents, self.preferences.min_num_seeders)
            hd_torrents = find_torrents_with_hd(min_seeders_torrents)
            best_matches = find_torrents_that_best_match(hd_torrents, self.search_query)
            best_match = find_best_torrent_match(best_matches)

            return best_match
        except IndexError:
            raise TorrentMatchNotFoundException(f'Could not find any good matches for query "{self.search_query}"')

    def download_torrent(self, torrent):
        download_torrent_from_magnet_link(torrent.magnet_link)
