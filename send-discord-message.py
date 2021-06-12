import requests
import time

while True:
    token = "" #insert token here
    request_url = "" #insert channel link here
    message = input(">> ")
    payload = {
    'content': message
    }
    header = {
    'authorization': token,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    requests.post(request_url, data=payload, headers=header)
    time.sleep(0.5)
