import requests








r = requests.get('https://www.google.com/', auth=('user', 'pass'))
print(r.status_code)
print(r.headers)
print(r.content)
print(r.text)
print(r.json)
print(requests.post('https://www.google.com/', data={'key': 'value'}))
