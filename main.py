import configparser
import os
import time
from move_file import move_file

# Get/set config vars
config = configparser.ConfigParser()
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(CURRENT_DIR, 'config', 'config.ini')
config.read(config_file)
download_dir = config.get('DEFAULT', 'DownloadDirectory')
TV_DIR = config.get('DEFAULT', 'TVDirectory')
MOVIE_DIR = config.get('DEFAULT', 'MovieDirectory')
video_filetypes = tuple(config.get('DEFAULT', 'FileTypes').split(','))
# Configs set

before = dict ([(f, None) for f in os.listdir (download_dir)])
while 1:
    after = dict ([(f, None) for f in os.listdir (download_dir)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added: 
        print "New item detected in directory"
        for dirpath, dirname, filenames in os.walk(download_dir):
            if not filenames:
                pass
            elif ((dirpath != download_dir) and (filenames[0].lower().endswith(video_filetypes))): # Video file detected
                _file = os.path.join(dirpath, filenames[0])
                print "Opening file to check if if file is locked"
                try:
                    fp = open(_file)
                except IOError as e:
                    print "File is locked. Not attempting to move to directory yet"
                else:
                    print "Successfully opened file, moving to directory."
                    fp.close()
                    move_file(download_dir, TV_DIR, MOVIE_DIR)
                    before = after
    time.sleep(10)