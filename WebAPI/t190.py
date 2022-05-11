import requests
import pprint

#https://api.telegram.org/bot<token>/НАЗВАНИЕ_МЕТОДА
#5393673860:AAEfqPIaY9J5vVMiemzD4faUph0NAdsSXlM/getUpdates
result = requests.get('https://api.telegram.org/bot5393673860:AAEfqPIaY9J5vVMiemzD4faUph0NAdsSXlM/getUpdates')
print(result.text)
answer = result.json()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(answer)