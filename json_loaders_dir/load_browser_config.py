import json

json_file = open('./json_dir/config.json', 'r')
data = json.load(json_file)

browser = data['browserType']
current_url = data['current_url']
chrome_driver_patch = data['chrome_driver_patch']
firefox_driver_patch = data['firefox_driver_patch']
