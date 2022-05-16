import requests
import pprint

response = requests.get('https://api.telegram.org/bot5393673860:AAEfqPIaY9J5vVMiemzD4faUph0NAdsSXlM/getMe')
result = response.json()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(result)