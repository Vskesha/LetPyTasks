import requests
import time

last_update_id = 0
while True:
    result = requests.get('https://api.telegram.org/bot5393673860:AAEfqPIaY9J5vVMiemzD4faUph0NAdsSXlM/getUpdates', params={'offset':last_update_id + 1})
    data = result.json()
    for update in data['result']:
        if 'text' in update['message']:
            print(update['message']['text'])
            last_update_id = update['update_id']    
    time.sleep(2)