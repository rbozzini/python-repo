from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus
from pprint import pprint
import urllib
import json

url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"

query = input("Cosa vuoi cercare?")

query = urlencode( {'q' : query } )

response = urlopen (url + query ).read()

data = json.loads ( response )

pprint(data)