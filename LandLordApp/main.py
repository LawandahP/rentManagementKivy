from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.label import Label
import time
from kivymd.uix.button import MDRoundFlatButton


class Rootwidget(ScreenManager):
    pass


class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]username and/ or password required[/color]'
        else:
            if uname == 'Misheck' and passw == 'Misheck123':
                info.text = '[color=#00FF00]Logged In successfully![/color]'
                time.sleep(4)
                App.get_running_app().root.current = "SignedIn"
            else:
                info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'


class LandlordApp(App):
    def build(self):
        return Rootwidget()


if __name__ == "__main__":
    LandlordApp().run()
