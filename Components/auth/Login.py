import webview
from .Auth import twitch_api
import time

auth = twitch_api()
url = auth.request_url()
window = webview.create_window('Authorization',url=url)

def Login():

        window.closed += on_closed
        window.loaded += on_loaded

        webview.start()


def on_closed():
    window.destroy()
    print(window)



def on_loaded():
    try:
        while(True):
            if isinstance(window,webview.Window):
                browserUrl = window.get_current_url()
                print(browserUrl)
        
            time.sleep(5)


    # This always throws an error after window is closed 
    # it still waits for the object

    except KeyError as e:
        pass

