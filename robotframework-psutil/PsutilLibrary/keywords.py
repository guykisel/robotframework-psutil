"""

This is a very thin wrapper for psutil. You can access all of psutil's usual
methods via PsutilLibrary calls in Robot Framework.

"""
# pylint: disable=E1120,W0613
import ast
import inspect

import psutil
import wrapt


def _str_to_data(string):
    try:
        return ast.literal_eval(str(string).strip())
    except Exception:
        return string


@wrapt.decorator
def _str_vars_to_data(f, instance, args, kwargs):
    args = [_str_to_data(arg) for arg in args]
    kwargs = dict(
        (arg_name, _str_to_data(arg)) for arg_name, arg in kwargs.items())
    result = f(*args, **kwargs)
    return result


class PsutilKeywords(object):
    """
    This looks tricky but it's just the Robot Framework Hybrid Library API.
    http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#hybrid-library-api
    """

    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self):
        self.names = [name.lower() for name, function in inspect.getmembers(psutil) if
                      inspect.isfunction(function)]

    def get_keyword_names(self):
        return self.names

    def __getattr__(self, name):
        func = None
        if name.lower() in self.names:
            func = getattr(psutil, name.lower())
        if func:
            return _str_vars_to_data(func)
        raise AttributeError('Non-existing keyword "{0}"'.format(name))
