import requests
from pandas.io.json import json_normalize
import json

access_token='334472808.8864b68.7521807dc0074a0dbbaeb7b45bb4c42f'

url = 'https://api.instagram.com/v1/users/self/?access_token=334472808.8864b68.7521807dc0074a0dbbaeb7b45bb4c42f'

r = requests.get(url)
response = json.loads(r.text)