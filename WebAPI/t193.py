import requests
import pprint

last_update_id = 0
pp = pprint.PrettyPrinter(indent=2)
while True:
	result = requests.get('https://api.telegram.org/bot5393673860:AAEfqPIaY9J5vVMiemzD4faUph0NAdsSXlM/getUpdates', params={'offset': last_update_id + 1})
	data = result.json()
	for update in data['result']:
		pp.pprint(data)
		last_update_id = update['update_id']
		chat_id = update['message']['chat']['id']
		send_result = requests.get('https://api.telegram.org/bot5393673860:AAEfqPIaY9J5vVMiemzD4faUph0NAdsSXlM/sendMessage', params={'chat_id':chat_id, 'text':'Hi from VsKesha'})
