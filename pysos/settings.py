DEBUG = True
DATABASE = ''

try:
    from .local_settings import *
except:
    #  if local_settings doesn't exist
    pass