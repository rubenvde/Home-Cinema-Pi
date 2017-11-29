from kivy.uix.screenmanager import ScreenManager
from screens import AppMenu


class ScreenHandler(ScreenManager):
    sharedinstance = None

    def __init__(self, **kwargs):
        super(ScreenHandler, self).__init__(**kwargs)
        self.add_widget(AppMenu(backgroundcolor='#FFFFFF', color='#000000'))
