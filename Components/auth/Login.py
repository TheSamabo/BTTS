import webview
from .Auth import twitch_api
import time

auth = twitch_api()
url = auth.request_url()
window = webview.create_window('Authorization',url=url)
#

# Rework this into class based, so you can access 
# disableButton, codeUrl, etc.
def Login():

        window.closed += on_closed
        window.loaded += on_loaded

        webview.start()

        codeUrl = None
        disableButton = False
def on_closed():
    window.destroy()
    print(window)



def on_loaded():
    try:
        while(True):
            if isinstance(window,webview.Window):
                browserUrl = window.get_current_url()
                if "code=" in browserUrl:
                    print(browserUrl)
                    codeUrl = browserUrl
                    on_closed()
                    disableButton = True
                    break
            time.sleep(5)


    # This always throws an error after window is closed 
    # it still waits for the object

    except KeyError as e:
        pass

def get_disableButton():

