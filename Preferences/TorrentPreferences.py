class TorrentPreferences:
    def __init__(self, min_num_seeders: int, torrent_type: str, matched_percentage: int):
        self.min_num_seeders = min_num_seeders
        self.torrent_type = torrent_type
        self.matched_percentage = matched_percentage
