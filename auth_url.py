
from requests_oauthlib import OAuth2Session
def auth_request_url():
    client_id = "gqozun4l4eg9dk43yb1wjdpch0z4jk"
    client_sercret = "ykqv7h9a9rnusijzs1c6ovdib05ykj"
    authorization_base_url = "https://id.twitch.tv/oauth2/authorize"
    token_url = "https://id.twitch.tv/oauth2/token"
    redirect_uri = "https://duckduckgo.com"
    response_type = "code"
    scope = "channel_read"




    twitch = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri, scope=scope)

    authorization_url, state = twitch.authorization_url(authorization_base_url)

    return authorization_url

auth_request_url()

