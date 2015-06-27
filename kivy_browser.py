import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from android.runnable import run_on_ui_thread
from jnius import *

activity = autoclass('org.renpy.android.PythonActivity').mActivity
WebView = autoclass('android.webkit.WebView')
LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
WebViewClient = autoclass('org.renpy.android.KivyJSClient')

class KivyBrowser(FloatLayout):
    def __init__(self, url, **kwargs):
        super(KivyJS, self).__init__(**kwargs)
        self.browser = Browser(url)
        self.add_widget(self.browser)

    def get_browser(self):
        return self.browser

class Browser(Widget):
    def __init__(self, url, **kwargs):
        super(Browser, self).__init__(**kwargs)
        self.js = None
        self.wvc = None
        self.webview = None
        self.isset = False
        self.url = url
        Clock.schedule_once(self.__create_webview, -1)

    def get(self, url):
        self.webview.loadUrl(url)

    @run_on_ui_thread
    def __create_webview(self, *args):
        self.wvc = WebViewClient()
        #self.js = self.wvc.get_interface()
        self.webview = WebView(activity)
        self.webview.getSettings().setJavaScriptEnabled(True)
        #self.webview.addJavascriptInterface(self.js, "PAGE")
        self.webview.setWebViewClient(self.wvc)
        activity.addContentView(self.webview, LayoutParams(-1, -1))
        self.get(self.url)











