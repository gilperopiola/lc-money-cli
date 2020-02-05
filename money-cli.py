import requests 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("amount")
args = parser.parse_args()

name = args.name
amount = args.amount

URL = "http://localhost:9005/Transaction"

HEADERS = {
}

data = {
    "name": name,
    "amount": amount,
    "description": ""
}

r = requests.post(url=URL, json=data, headers=HEADERS) 
data = r.json() 

print(data)
