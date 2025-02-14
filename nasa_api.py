import requests

api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(api_url)

data = response.json()
print(f"Title: {data['title']}")
print(f"URL: {data['url']}")
print(f"Explanation: {data['explanation']}")



