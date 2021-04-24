import click
from requests import exceptions

from Exceptions.TorrentMatchNotFoundException import TorrentMatchNotFoundException
from Kickass.KickassMain import main
from Preferences.TorrentPreferences import TorrentPreferences


@click.command()
@click.option("--query", prompt="Enter your search (try being as specific as possible)", help="Specify your query",
              required=True)
def init(query):
    preferences = TorrentPreferences(5, 'movie', 20)
    click.secho(f'Searching for "{query}" with a minimum of {preferences.min_num_seeders} seeders...\n', fg='cyan')

    try:
        best_match = main(query, preferences)

        click.secho(f'Match found! {best_match.name} Check your installed Torrent Client.', fg='green')
        click.pause()
    except exceptions.ConnectionError as conn_error:
        click.secho(str(conn_error), fg='red')
        click.pause()
    except TorrentMatchNotFoundException as not_found_error:
        click.secho(str(not_found_error), fg='red')
        click.secho(
            'Hint: If you don\'t find the results you are looking for on the first run try being more specific.\n',
            fg='yellow')
        click.pause()
    except Exception as err:
        click.secho(str(err), fg='red')
        click.pause()
