from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle
from .DisplayTime import DisplayTime
from helpers import BasicFunctions


class BasicScreen(Screen):
    def __init__(self, **kwargs):
        super(BasicScreen, self).__init__()
        self.backgroundcolor = BasicFunctions.hex_to_rgb("#000000")
        self.color = BasicFunctions.hex_to_rgb("#FFFFFF")
        self.size = Window.size
        for key, value in kwargs.items():
            if key == 'backgroundcolor':
                self.backgroundcolor = BasicFunctions.hex_to_rgb(value)
            elif key == 'color':
                self.color = BasicFunctions.hex_to_rgb(value)

        with self.canvas:
            Color(rgb=self.backgroundcolor)  # rgba might be better
            Rectangle(size=self.size, pos=self.pos)

        self.add_widget(DisplayTime(color=kwargs['color']))
