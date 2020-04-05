import requests

def call_website():
    url = "https://www.python.org/"
    response = requests.get(url)
    return response

def call_website_if_status():
    url = "https://www.python.org/"
    response = requests.get(url)
    if requests.exceptions.Timeout:
        return None
    return response

def get_website_data(response):
    return response.text
    