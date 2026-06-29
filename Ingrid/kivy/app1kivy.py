from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window




class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 2

        Window.clearcolor = "#FFBAFA"

        self.window.size_hint = (0.6, 0.6)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.window.add_widget(Image(source="imagen1.jpg"))

        self.boton = Button(text="botón 1")
        self.window.add_widget(self.boton)

        return self.window












app = SayHello()
app.title = "HELLO WORLD"
app.run()
