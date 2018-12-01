from urllib.parse import urlencode
import requests

url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
query = input("Cosa vuoi cercare?")
query = urlencode( {'q' : query } )

print(requests.get(url+query).json())