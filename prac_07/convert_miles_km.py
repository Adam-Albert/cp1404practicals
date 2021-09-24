from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_to_kilometers(self):
        """ convert miles to kilometers """
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_valid_miles(self):
        """ get valid miles from user input """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, increment):
        value = self.get_valid_miles() + increment
        self.root.ids.input_miles.text = str(value)
        self.convert_miles_to_kilometers()





MilesConverterApp().run()
