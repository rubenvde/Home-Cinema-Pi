import json
from debug import Debugger
from .FontLoader import FontLoader
from .ImageLoader import ImageLoader

class ConfigLoader:

    def __init__(self, rootdir):
        self.rootdir = rootdir
        with open(self.rootdir + '/config.json', 'r') as f:
            config = json.load(f)
        Debugger.back_print("Config file loaded")
        FontLoader.set_folder(self.rootdir + config['directories']['font'])
        ImageLoader.set_folder(self.rootdir + config['directories']['image'])
