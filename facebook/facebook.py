import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv('.env'))

def get_60_days_token(token):

    SHORT_LIFE_ACCESS_TOKEN = token
    APP_ID = os.getenv('fb_app_id')
    APP_SECRET = os.getenv('fb_app_secret')

    response = requests.get(f"""
            https://graph.facebook.com/v14.0/oauth/access_token?grant_type=fb_exchange_token&\
            client_id={APP_ID}&client_secret={APP_SECRET}&\
            fb_exchange_token={SHORT_LIFE_ACCESS_TOKEN}
        """)
    long_life_access_token = response.json()['access_token']

    return long_life_access_token

def check_long_token():
    long_life_token = os.getenv('fb_60_days_token')
    
    url = f"https://graph.facebook.com/v15.0/me?access_token={long_life_token}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False