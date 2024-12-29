import requests
import json
from time import sleep
from logger_hand import logger

url = "http://server:8000/login"
data = {"name":"evgenz", "password":"bad"}
headers = {"Content-Type": "application/json"}

for i in range(10):
    with requests.post(url, headers=headers, json=data) as response:
        logger.info(response.json())
        sleep(5)