import sys, os


def set_path(filename):
    slash = check_system_slash()
    # expanduser() works for windows as well as unix based systems
    user_home_path = os.path.expanduser("~")
    downloads_path = user_home_path + slash + 'Downloads'
    desktop_path = user_home_path + slash + 'Desktop'

    if os.path.isdir(downloads_path):
        return downloads_path + slash + filename
    elif os.path.isdir(desktop_path):
        return desktop_path + slash + filename
    else:
        return user_home_path + slash + filename


def check_system_slash():
    if sys.platform.startswith("win32"):
        slash = '\\'
    else:
        slash = '/'
    return slash
