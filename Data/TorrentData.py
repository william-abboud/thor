class TorrentData:
    def __init__(self, name: str, size: str, magnet_link: str, seeders: int):
        self.name = name
        self.size = size
        self.magnet_link = magnet_link
        self.seeders = seeders
