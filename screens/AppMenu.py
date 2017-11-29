from base import BasicScreen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.colorpicker import Color
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from helpers import FontLoader
from base.ImageButton import ImageButton
from helpers import ImageLoader


class AppMenu(BasicScreen):

    def __init__(self, **kwargs):
        super(AppMenu, self).__init__(**kwargs)
        anchor_header = AnchorLayout(anchor_x='left', anchor_y='top')
        header = Label(text="Apps", size=(150, 80), size_hint=(None, None), font_size='50sp', font_name=FontLoader.get_font('bold'), color=Color(rgb=self.color).rgba)
        anchor_header.add_widget(header)
        self.add_widget(anchor_header)

        scroll_layout = GridLayout(cols=3, spacing=40, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))
        for i in range(100):
            imgurl = ImageLoader.get_image("app.png")
            imagebtn = ImageButton(size_hint_y=None, height=80, source=imgurl)
            scroll_layout.add_widget(imagebtn)
        scroll = ScrollView(size_hint=(1, None), size=(self.width, self.height - 90))
        scroll.add_widget(scroll_layout)
        self.add_widget(scroll)
