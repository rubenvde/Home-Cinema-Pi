from kivy.uix.screenmanager import ScreenManager, RiseInTransition
from screens import AppMenu
from helpers import BasicFunctions
import json
import importlib

class ScreenHandler(ScreenManager):
    sharedinstance = None
    currentApp = None

    def __new__(cls, *args, **kwargs):
        if not cls.sharedinstance:
            cls.sharedinstance = super(ScreenHandler, cls).__new__(cls, *args, **kwargs)
        return cls.sharedinstance

    def __init__(self, **kwargs):
        super(ScreenHandler, self).__init__(**kwargs)

    def start(self):
        startapp = AppMenu(name='AppMenu', backgroundcolor='#FFFFFF', color='#000000')
        self.currentApp = startapp
        self.add_widget(startapp)

    def open_app(self, app_name):
        if self.__check_programs_installed__(app_name):
            i = importlib.import_module('screens.' + app_name)
            _class = getattr(i, app_name)
            self.switch_to(_class(name=app_name), transition=RiseInTransition())
        else:
            print("App not installed")

    def __check_programs_installed__(self, name):
        rootdir = BasicFunctions.get_root()
        with open(rootdir + '/programs_installed.json', 'r') as f:
            programs = json.load(f)

        return name in programs