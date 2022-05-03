import requests
result = requests.get('https://letpy.com/simple-html-example/').text
result = result.replace('/', '')
nums = result.split('<strong>')
print(int(nums[-2]))