import os
import shutil
from get_title_name import get_title_name

def move_file(download_dir, TV_DIR, MOVIE_DIR):
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