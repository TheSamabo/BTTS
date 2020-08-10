import logging
import webview
import urllib3
from urllib.parse import urlparse, parse_qs
from .Auth import twitch_api
import time

#

# Rework this into class based, so you can access 
# disableButton, codeUrl, etc
class Login():
    def __init__(self):
        self.logger = logging.getLogger("__main__")
        self.logger.setLevel(20)
        self.auth = twitch_api()
        
        self.window = webview.create_window('Authorization',url=self.auth.request_url())

        self.window.closed += self.on_closed
        self.window.loaded += self.on_loaded

        self.codeUrl = None
        self.isOpened = False


    def open(self):
        self.isOpened = True
        webview.start()



    def on_closed(self):
        self.isOpened = False
        self.window.destroy()
        self.window = None
        self.logger.info(msg="Closing Auth Window")



    def on_loaded(self):
        try:
            self.logger.info(msg="Auth window opened")
            while(self.window != None):
                self.browserUrl = self.window.get_current_url()

                # If "code" is in the url parse it and set it to auth object
                if "code=" in self.browserUrl:
                    print(self.browserUrl)
                    self.codeUrl = self.browserUrl
                    self.parsed = urlparse(self.browserUrl)
                    self.code = parse_qs(self.parsed.query)["code"][0]
                    print(self.code)
                    self.auth.setCode(self.code)
                    self.on_closed()
                    self.auth.request_token()
                    self.auth.request_channel()
                    self.channel = self.auth.getChannel()
                    break
                
                time.sleep(5)


        # This always throws an error after window is closed 
        # it still waits for the object

        except KeyError as e:
            pass

    def get_isOpened(self):
        return self.isOpened

    def get_channelId(self):
        return self.channel["_id"]

    def get_accessToken(self):
        return self.auth.getTokens()["access_token"]
        
    

