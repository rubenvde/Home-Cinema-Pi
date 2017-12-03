from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
import base.ScreenHandler
from debug import Debugger


class ImageButton(ButtonBehavior, Image):

    def __init__(self, **kwargs):
        self.location = None
        try:
            self.location = kwargs.pop('location')
        except:
            Debugger.front_print("No location was given")
        super(ImageButton, self).__init__(**kwargs)

    def on_press(self):
        if self.location:
            base.ScreenHandler().open_app(self.location)
        else:
            Debugger.display_error("No app found with name:%s" % self.location)
