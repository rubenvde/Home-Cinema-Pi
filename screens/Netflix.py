from base import BasicScreen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.colorpicker import Color
from kivy.uix.label import Label
from helpers import FontLoader
from debug import Debugger

class Netflix(BasicScreen):

    def __init__(self, **kwargs):
        super(Netflix, self).__init__(name='Netflix', backgroundcolor='#000000', color='#FFFFFF')
        anchor_header = AnchorLayout(anchor_x='left', anchor_y='top')
        header = Label(text="Netflix", size=(150, 80), size_hint=(None, None), font_size='50sp',
                       font_name=FontLoader.get_font('bold'), color=Color(rgb=self.color).rgba)
        anchor_header.add_widget(header)
        self.add_widget(anchor_header)
        Debugger.front_print("Netflix app loaded")
