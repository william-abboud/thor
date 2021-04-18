from requests import get, exceptions


class TorrentsUrlProvider:
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/89.0.4389.82 Safari/537.36'

    def __init__(self, url):
        self.url = url

    def get_torrents(self):
        # Needs User-Agent header otherwise it throws 403
        headers = {'User-Agent': TorrentsUrlProvider.USER_AGENT}
        response = get(self.url, headers=headers)

        if response.ok:
            return response.content
        else:
            raise exceptions.ConnectionError(f'Unable to reach tracker. Response code: {response.status_code}.')
