import sys, os


def set_path(filename, extension):
    if sys.platform.startswith("win32"):
        slash = '\\'
    else:
        slash = '/'

    user_home_path = os.path.expanduser("~")
    downloads_path = user_home_path + slash + 'Downloads'
    desktop_path = user_home_path + slash + 'Desktop'

    if os.path.isdir(downloads_path):
        return downloads_path + slash + filename + extension
    elif os.path.isdir(desktop_path):
        return desktop_path + slash + filename + extension
    else:
        return user_home_path + slash + filename + extension
