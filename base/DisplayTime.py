from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.colorpicker import Color
from kivy.clock import Clock
from helpers import BasicFunctions
from helpers import FontLoader
import time


class DisplayTime(AnchorLayout):
    def __init__(self, **kwargs):
        super(DisplayTime, self).__init__()
        self.current_minute = -1
        self.color = BasicFunctions.hex_to_rgb("#FFFFFF")
        for key, value in kwargs.items():
            if key == 'color':
                self.color = BasicFunctions.hex_to_rgb(value)

        self.anchor_x = 'right'
        self.anchor_y = 'top'
        self.label_time = Label(text=time.strftime("%H") + ":" + time.strftime("%M"), size=(70, 80), size_hint=(None, None),
                           font_size='20sp', font_name=FontLoader.get_font('regular'), color=Color(rgb=self.color).rgba)
        self.add_widget(self.label_time)
        Clock.schedule_interval(self.update_time, 1.0)

    def update_time(self,dt):
        if int(time.strftime("%M")) is not self.current_minute:
            self.current_minute = int(time.strftime("%M"))
            self.label_time.text = time.strftime("%H") + ":" + time.strftime("%M")
