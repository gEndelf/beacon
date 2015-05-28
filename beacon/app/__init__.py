import os


def get_env_var(key):
    try:
        return os.environ[key]
    except KeyError:
        raise KeyError('%s was not defined' % key)
