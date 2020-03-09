
from requests_oauthlib import OAuth2Session
import webbrowser

client_id = "gqozun4l4eg9dk43yb1wjdpch0z4jk"
client_sercret = "ykqv7h9a9rnusijzs1c6ovdib05ykj"
authorization_base_url = "https://id.twitch.tv/oauth2/authorize"
token_url = "https://id.twitch.tv/oauth2/token"
redirect_uri = "http://127.0.0.1:5501/"
response_type = "code"
scope = "channel_read"


twitch = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri, scope=scope)

authorization_url, state = twitch.authorization_url(authorization_base_url)

print("Please go here and authorize" + " "+ authorization_url)

webbrowser.open(authorization_url)
 
user_auth = input("Please insert the WHOLE URL after you logged in: " )

print(user_auth)



'''
https://id.twitch.tv/oauth2/authorize?state=c00a836c7b3024606f75f56ab41cb1ed
&scope=channel_read&response_type=code&approval_prompt=auto&redirect_uri=http%3A%2F%2F127.0.0.1%3A5501%2F&client_id=gqozun4l4eg9dk43yb1wjdpch0z4jk
'''