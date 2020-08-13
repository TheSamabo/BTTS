import requests
from requests_oauthlib import OAuth2Session
import json
import configparser


client_id = "gqozun4l4eg9dk43yb1wjdpch0z4jk"
client_secret = "gqkg0pf9vonqdezw071og9emi6l459"
authorization_base_url = "https://id.twitch.tv/oauth2/authorize"
redirect_uri = "https://duckduckgo.com"
response_type = "code"
scope = "channel_read channel:read:redemptions"

config = configparser.ConfigParser()
class twitch_api():

    def request_url(self):
        

        twitch = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri, scope=scope)

        authorization_url, state = twitch.authorization_url(authorization_base_url)

        return authorization_url


    def setCode(self, value):
        self.auth_code = value

    def request_token(self):
        url = "https://id.twitch.tv/oauth2/token"

        payload = "client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=authorization_code&scope=" + scope + "&code=" + self.auth_code + "&redirect_uri=https%3A%2F%2Fduckduckgo.com"
        headers = {
            'content-type': "application/x-www-form-urlencoded"}

        response = requests.request("POST", url, data=payload, headers=headers)

        
        
        # ACCESS and REFRESH tokens 
        print(response.text)
        self.tokens =  json.loads(response.text)
        config['Tokens'] = {"AccessToken": self.tokens["access_token"],
                            "RefreshToken": self.tokens["refresh_token"]
                            }
        with open('data.ini','w') as configfile:
            config.write(configfile)

    def request_channel(self):
        
        url = "https://api.twitch.tv/kraken/channel"

        payload = ""
        headers = {
            'authorization': "OAuth " + self.tokens["access_token"],
            'accept': "application/vnd.twitchtv.v5+json",
            'client-id': "gqozun4l4eg9dk43yb1wjdpch0z4jk"
            }

        response = requests.request("GET", url, data=payload, headers=headers)
        self.channel = json.loads(response.text)
        
    
    def getChannel(self):
        return self.channel

    def getTokens(self):
        return self.tokens

def checkTokens():
    config.read('data.ini')
    rt = config["Tokens"]["RefreshToken"]

    url = "https://id.twitch.tv/oauth2/token"

    payload = "refresh_token=" + rt + "&client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=refresh_token&scope=" + scope 
    headers = {
        'content-type': "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, data=payload, headers=headers)
    return json.loads(response.text)
    







