from kivy.core.window import Window
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import time

from kivy.uix.widget import Widget

Window.size = (500, 300)
Window.borderless = True
Window.allow_screensaver = True


class TimeLabel(Label):
    def update(self, *args):
        self.text = time.strftime('%H:%M:%S')
        self.font_size = 100


class WidgetApp(App, Widget):

    def build(self):
        curent_time = TimeLabel()
        Clock.schedule_interval(curent_time.update, 1)
        return curent_time


if __name__ == '__main__':
    app = WidgetApp()
    app.run()
