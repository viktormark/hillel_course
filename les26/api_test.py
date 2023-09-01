from pprint import pprint

import requests


r = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=sold")
pprint(r.json())
