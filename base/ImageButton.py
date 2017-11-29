from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


class ImageButton(ButtonBehavior, Image):

    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)

    def on_press(self):
        print('pressed')
