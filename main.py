## DedSec APP

# IMPORTS
from kivy.app import App
import random
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

# MAIN CLASS
class DedSecApp(App):

    # UPDATE FUNCTION
    def update(self, instance):
        keys = "abWXc9$dVAeYU8fTZBg7ShR6iCQjk#D5PlmEOn4RNFMoK3LpqGr2sHt@uI1vwxJ0yz!"   
        types = ["apk","exe","py","c","h","bf"]
        self.Text2.text = "".join(random.choices(keys, k=9)) + ".[color=#aa0000]" + "".join(random.choices(types)) + "[/color]"


    # BUILD FUNCTION
    def build(self):
        # HOME SCREEN
        self.Home = FloatLayout()

        # Toolbar
        self.Text = Label(
            pos_hint = {"center_x": 0.5, "center_y":0.3},
            font_size = 20,
            color = "#ffffff",
            text = '[b]Generating Malware[/b]',
            markup = True,
        )

        # LABLE
        self.Text2 = Label(
            pos_hint = {"center_x": 0.5, "center_y":0.2},
            font_size = 20,
            color = "#AAAAAA",
            text = '',
            markup = True,
            bold = True
        )

        # GIF IMAGE
        self.Gif = Image(
            size_hint = (0.5, 0.5),
            pos_hint = {"center_x": 0.5, "center_y":0.75},
            source = "data/dedsec2.gif",
            anim_delay = 0.025,
            mipmap = True,
            color = "#ffffff"
        )
        

        # ADD WIDGETS
        self.Home.add_widget(self.Text)
        self.Home.add_widget(self.Gif)
        self.Home.add_widget(self.Text2)
        
        # Update Text text        
        Clock.schedule_interval(lambda _:self.update(self), 0.2)


        # RETRUN HOME       
        return self.Home
# RUN
DedSecApp().run()
# -> END