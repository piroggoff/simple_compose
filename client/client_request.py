import requests
import json
from logger_hand import *

url = "http://127.0.0.1:8000/login"
data = {"name":"evgenz", "password":"bad"}
headers = {"Content-Type": "application/json"}

with requests.post(url, headers=headers, json=data) as response:
    logger.info(response.json())