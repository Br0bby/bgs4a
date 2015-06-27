import kivy
from sys import exit
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import platform
from kivy_brpwser import KivyBrowser
from server import get_server

class Bgs4aApp(App):
    def build(self):
        root = FloatLayout(size_hint=(1, 1))

        self.server = get_server(8000)
        Clock.schedule_interval(self.run_server, 0.032)

        self.browser = KivyBrowser("http://localhost:8000/index.html")
        root.add_widget(self.browser)
        return root

    def run_server(self, *args):
        self.server.serve_forever()

    def post_build_init(self, *args):
        if platform() == 'android':
            import android
            android.map_key(android.KEYCODE_BACK, 1001)

        win = Window
        win.bind(on_keyboard=self.my_key_handler)

    def my_key_handler(self, window, keycode1, keycode2, text, modifiers):
        if keycode1 in [27, 1001]:
            exit()
            return True
        return False

if __name__ == '__main__':
    Bgs4aApp().run()



