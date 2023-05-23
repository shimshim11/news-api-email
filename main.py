import requests

api_key = "pub_22601ab85ce30946048f7320360f8399787b4"
url = "https://newsdata.io/api/1/news?apikey=" \
      "pub_22601ab85ce30946048f7320360f8399787b4&q=stock%20market%20us "

# Make request
request = requests.get(url)

# Get a dictionary with data
result = request.json()

# Access article titles and descriptions
body = ""
for article in result["results"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
