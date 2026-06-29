from kivy.app import App
from kivy.app import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button

class Inicio(Screen):
    pass

class pantalla1(Screen):
    pass

class pantalla2(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("omoriclase.kv")

class omoriiapp(App):
    Window.size = (600, 400)

    def build(self):
        return kv
    







if __name__ == "__main__":
    omoriiapp().run()