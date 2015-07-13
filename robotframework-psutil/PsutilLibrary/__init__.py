__author__ = 'gkisel'

import pkg_resources

from keywords import PsutilKeywords


__version__ = pkg_resources.get_distribution('robotframework-psutil').version


class PsutilLibrary(PsutilKeywords):
    """

    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
