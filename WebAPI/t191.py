import requests
import pprint

#https://api.telegram.org/bot<token>/НАЗВАНИЕ_МЕТОДА
#5393673860:AAEfqPIaY9J5vVMiemzD4faUph0NAdsSXlM/getUpdates
result = requests.get('https://api.telegram.org/bot5393673860:AAEfqPIaY9J5vVMiemzD4faUph0NAdsSXlM/getUpdates')
#print(result.text)
data = result.json()
#print(data)
for message in data['result']:
	print(message['message']['text'])
	print('from  ' + message['message']['from']['username'])