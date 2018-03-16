__version__ = "1.0"

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.core.window import Window


class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.onBackButton)

    def onBackButton(self, window, key, *args):
        if key == 27:
            return True
        return False

if __name__ == "__main__":
    MainApp().run()