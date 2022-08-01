"""
Arguments:
-text file

Exceptions:
-IOError if the file is not found

Return
- a list of all the words in lowercase
"""

import sys

def load(file):
    """  try to open a .txt file and give back a lower case list of all the words"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program".format(e, file), file=sys.stderr)
        sys.exit(1)
