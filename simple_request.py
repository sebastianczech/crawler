import requests

r = requests.get('https://api.github.com/events')
print(str(r.status_code) + ' for ' + r.url)

r = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(str(r.status_code) + ' for ' + r.url)