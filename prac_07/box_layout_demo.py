from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """ greet user on press of button."""
        print("greet")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_screen(self):
        """ clear all input and text."""
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
