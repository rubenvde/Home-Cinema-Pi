from kivy.app import App
from kivy.core.window import Window
from base import ScreenHandler
import os
from helpers import ConfigLoader
from debug import Debugger
from helpers import BasicFunctions

class HomeCinemaApp(App):

    def build(self):
        ScreenHandler().start()
        Window.size = (480, 800)
        return ScreenHandler.sharedinstance

if __name__ == '__main__':
    Debugger.error = True
    Debugger.frontend = True     # Just for debugging
    Debugger.backend = True      # Just for debugging
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    BasicFunctions.set_root(ROOT_DIR)
    ConfigLoader()
    HomeCinemaApp().run()
