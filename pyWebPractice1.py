import requests

url = 'http://www.iheartquotes.com/api/v1/random'
resp = requests.get(url)
resp
print ('Response =' + resp.text)