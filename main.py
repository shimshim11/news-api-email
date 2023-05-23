import requests

api_key = "pub_22601ab85ce30946048f7320360f8399787b4"
url = "https://newsdata.io/api/1/news?apikey=" \
      "pub_22601ab85ce30946048f7320360f8399787b4&q=stock%20market%20us "

# Make request
request = requests.get(url)

# Get a dictionary with data
result = request.json()

# Access article titles and descriptions
for article in result["results"]:
      print(article["title"])
      print(article["description"])
