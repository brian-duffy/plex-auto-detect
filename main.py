import configparser
import os
from omdb.get_omdb_api import get_omdb
config = configparser.ConfigParser()
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
# Get config files
config_file = os.path.join(CURRENT_DIR, 'config', 'config.ini')
config.read(config_file)
omdb_url = config.get('DEFAULT', 'OMDBAPIUrl')
download_dir = config.get('DEFAULT', 'DownloadDirectory')


values = {
    't': 'sausage'
}

result = get_omdb(omdb_url, values)

print result
