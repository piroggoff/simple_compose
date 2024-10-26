import urllib.request

fp = urllib.request.urlopen("http://localhost:1234/index.html")

encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

print(decodedContent)

fp.close()