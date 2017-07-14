import urllib.request

req = urllib.request.urlopen("https://google.com")

print(req.read())