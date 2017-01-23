import os
import re

def get_title_name(_dir, filename):
    """
    First step: check if filename contains regex something like S01E01:
        If it does, it must be a TV show
    """
    details = re.findall(r"""(.*)          # Title
                        [ .]
                        S(\d{1,2})    # Season
                        E(\d{1,2})    # Episode
                        [ .a-zA-Z]*  # Space, period, or words like PROPER/Buried
                        (\d{3,4}p)?   # Quality
                    """, filename, re.VERBOSE)
    if(len(details) is not 0):
        return {
            'type': 'tv',
            'title': details[0][0],
            'season': details[0][1]
        }
    else:
        return {
            'type': 'movie',
            'title': re.compile("^([^(]+)").match(filename).groups()[0].lstrip()
        }