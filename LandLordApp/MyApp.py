from datetime import date

from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRoundFlatButton, MDFlatButton, MDFillRoundFlatButton
import time
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
# from rent import rent_Str
from kivy.base import runTouchApp
from kivymd.uix.datatables import MDDataTable
from kivy.storage.jsonstore import JsonStore


class WelcomeScreen(Screen):
    pass


class SignIn(Screen):
    pass


class HomeScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class KisimaniScreen(Screen):
    pass


class TenantScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(SignIn(name='signin'))
sm.add_widget(HomeScreen(name='homescreen'))
sm.add_widget(SettingsScreen(name='settings_screen'))
sm.add_widget(KisimaniScreen(name='Kisimani_Screen'))
sm.add_widget(TenantScreen(name='tenant_screen'))


class RentApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Blue'
        # self.strin = Builder.load_string(rent_Str)
        # return self.strin

    def validate_user(self, username, password):
        if username == 'yj' or password == 'jty':
            self.dialog = MDDialog(text='username and/or password required',
                                   size_hint=(0.7, 0.2))
            self.dialog.open()

        elif username == '' and password == '':
            continue_button = MDFillRoundFlatButton(text='continue', on_release=self.go_to_next_screen_dialogue)
            self.dialog = MDDialog(text='Login successful',
                                   size_hint=(0.7, 0.2),
                                   buttons=[continue_button])
            self.dialog.open()

        else:
            self.dialog = MDDialog(text='invalid username and/or password',
                                   size_hint=(0.7, 0.2))
            self.dialog.open()

    def go_to_next_screen_dialogue(self, obj):
        self.dialog.dismiss()
        time.sleep(0.2)
        MDApp.get_running_app().root.current = 'homescreen'
        MDApp.get_running_app().root.transition.duration = 0

    def exit(self):
        yes_button = MDFillRoundFlatButton(text='yes', on_release=self.yes_exit)
        no_button = MDFillRoundFlatButton(text='no', on_release=self.dont_exit)
        self.dialog = MDDialog(text='Are you sure you want to exit?',
                               size_hint=(0.7, 0.2),
                               buttons=[yes_button, no_button])
        self.dialog.open()

    def yes_exit(self, obj):
        quit()

    def dont_exit(self, obj):
        self.dialog.dismiss()
        MDApp.get_running_app().root.current = 'homescreen'

    ###########################################settings functions#######################################################
    def returning(self):
        MDApp.get_running_app().root.current = 'homescreen'
        MDApp.get_running_app().root.transition.direction = 'left'
        MDApp.get_running_app().root.transition.duration = 0

    def returning2(self):
        MDApp.get_running_app().root.current = 'Kisimani_Screen'
        MDApp.get_running_app().root.transition.direction = 'left'
        MDApp.get_running_app().root.transition.duration = 0

    def change_theme_style(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def developer(self):
        self.dialog = MDDialog(text='name: GITHAIGA KAIRUTHI\n'
                                    'email: pythongeeko@gmail.com',
                               size_hint=(0.7, 0.2))
        self.dialog.open()

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date, year=2020, month=8, day=18)
        date_dialog.open()

    def get_date(self, date):
        self.mydate = date
        self.get_screen('tenant_screen').ids.date_picker.text = str(self.mydate)
    

RentApp().run()
