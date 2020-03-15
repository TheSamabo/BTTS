import requests
from requests_oauthlib import OAuth2Session


client_id = "gqozun4l4eg9dk43yb1wjdpch0z4jk"
client_secret = "ykqv7h9a9rnusijzs1c6ovdib05ykj"
authorization_base_url = "https://id.twitch.tv/oauth2/authorize"
token_url = "https://id.twitch.tv/oauth2/token"
redirect_uri = "https://duckduckgo.com"
response_type = "code"
scope = "channel_read"
auth_code = ""

class auth():

    def auth_request_url():
        

        twitch = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri, scope=scope)

        authorization_url, state = twitch.authorization_url(authorization_base_url)

        return authorization_url


    def auth_request_code():

        url = "https://id.twitch.tv/oauth2/token"

        payload = "client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=authorization_code&scope=" + scope + "&code=" + auth_code + "&redirect_uri=https%3A%2F%2Fduckduckgo.com"
        headers = {
            'content-type': "application/x-www-form-urlencoded"}

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response)

auth.auth_request_code()