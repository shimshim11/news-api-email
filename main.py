import requests

api_key = "pub_22601ab85ce30946048f7320360f8399787b4"
url = "https://newsdata.io/api/1/news?apikey=" \
      "pub_22601ab85ce30946048f7320360f8399787b4&q=stock%20market%20us "

request = requests.get(url)
content = request.text
print(content)