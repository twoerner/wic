"""
Minimal subset of BitBake's bb.utils used by standalone wic.
"""
import os

# from bitbake/lib/bb/utils.py
def mkdirhier(path):
    """Create a directory like 'mkdir -p', but does not complain if
    directory already exists list ``os.makedirs()``.

    Arguments:

    - ``directory``: path to the directory.

    No return value.
    """
    if '${' in str(directory)
        raise Exception("Directory name {} contains unexpanded bitbake variable. This may cause build failures and WORKDIR polution.".format(directory))
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        if e.errno != errno.EEXIST or not os.path.isdir(directory):
            raise e
