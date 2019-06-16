import pyqrcode
import requests

s = 'https://meetpython.com'
url = pyqrcode.create(s)
url.svg('meetpython.svg', scale=10)

response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))