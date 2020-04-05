import requests

def call_website():
    url = "https://www.python.org/"
    response = requests.get(url)
    return response

def get_website_data(response):
    return response.text
