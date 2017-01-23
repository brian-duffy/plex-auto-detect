import configparser
import shutil
import os
from omdb.get_omdb_api import get_omdb
from get_title_name import get_title_name
config = configparser.ConfigParser()
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
# Get config files
config_file = os.path.join(CURRENT_DIR, 'config', 'config.ini')
config.read(config_file)
omdb_url = config.get('DEFAULT', 'OMDBAPIUrl')
download_dir = config.get('DEFAULT', 'DownloadDirectory')
TV_DIR = config.get('DEFAULT', 'TVDirectory')
MOVIE_DIR = config.get('DEFAULT', 'MovieDirectory')

for title_name in os.listdir(download_dir):
    film_details = get_title_name(download_dir, title_name)
    current_dirpath = os.path.join(download_dir, title_name)

    if(film_details['type'] == 'tv'):
        dest_filepath = os.path.join(TV_DIR, film_details['title'], 'S'+ film_details['season'])
        if not (os.path.exists(dest_filepath)):
            os.makedirs(dest_filepath)
        shutil.move(current_dirpath, dest_filepath)
    elif(film_details['type'] == 'movie'):
        dest_filepath = os.path.join(MOVIE_DIR, film_details['title'])
        shutil.move(current_dirpath, dest_filepath )