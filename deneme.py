import requests

url = 'https://tracker.gg/valorant/profile/riot/Doraliçe%23UUR/overview'
response = requests.get(url)
html_response = response.text
stats_json = 0 # html_to_json.convert(html_response)

print(stats_json)