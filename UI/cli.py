import click
from requests import exceptions

from Exceptions.TorrentMatchNotFoundException import TorrentMatchNotFoundException
from Kickass.KickassMain import main
from Preferences.TorrentPreferences import TorrentPreferences


@click.command()
@click.argument('query')
def init(query):
    preferences = TorrentPreferences(5, 'movie', 20)
    print(f'Searching for "{query}" with a minimum of {preferences.min_num_seeders} seeders...\n')

    try:
        best_match = main(query, preferences)

        print(f'Match found! {best_match.name} Check your installed Torrent Client.')
    except exceptions.ConnectionError as conn_error:
        print(conn_error)
    except TorrentMatchNotFoundException as not_found_error:
        print(not_found_error)
        print('Hint: If you don\'t find the results you are looking for on the first run try being more specific.\n ')


if __name__ == '__main__':
    init()
