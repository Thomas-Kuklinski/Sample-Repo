# welcome message
print("桃子果然復活了")

import requests

r = requests.get("https://coreyms.com")
print(r.status_code)
