from urllib.parse import urlparse, urljoin, urlencode, quote, urlunparse, parse_qsl
from Data.TorrentsUrlProvider import TorrentsUrlProvider

BASE_URL = 'https://kickass.onl/usearch/'
MOST_SEEDERS_QUERY = 'field=seeders&sorder=desc'


def compose_full_url(query) -> str:
    search_url_with_query = urljoin(BASE_URL, quote(f"{query}/"))
    parsed_search_url_with_query = urlparse(search_url_with_query)
    query_params = dict(parse_qsl(MOST_SEEDERS_QUERY))
    url_parts = list(parsed_search_url_with_query)
    url_parts[4] = urlencode(query_params)

    return urlunparse(url_parts)


class KickassTorrentsUrlProvider:
    def __init__(self, query):
        full_url = compose_full_url(query)
        self.url_provider = TorrentsUrlProvider(full_url)

    def get_torrents(self):
        return self.url_provider.get_torrents()
