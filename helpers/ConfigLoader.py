import json
from debug import Debugger
from .FontLoader import FontLoader
from .ImageLoader import ImageLoader
from .BasicFunctions import BasicFunctions

class ConfigLoader:

    def __init__(self):
        rootdir = BasicFunctions.get_root()
        with open(rootdir + '/config.json', 'r') as f:
            config = json.load(f)
        Debugger.back_print("Config file loaded")
        FontLoader.set_folder(rootdir + config['directories']['font'])
        ImageLoader.set_folder(rootdir + config['directories']['image'])
