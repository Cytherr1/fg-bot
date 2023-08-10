import requests

url = 'https://www.youtube.com/watch?v=WM8bTdBs-cw'
response = requests.get(url)
video_json = response.json()

print(video_json)