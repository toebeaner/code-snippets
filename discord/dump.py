import requests
import json

token = input("discord token - ")


def login(token = None):
    if token:
        data = requests.get(
            "https://discord.com/api/v9/users/@me",
             headers = { 
                'authorization': token, 
                'user-agent': 'Mozilla/5.0'
                } 
        )

        if data.status_code == 200:
            print(json.loads(data.content))
        


login(token)
