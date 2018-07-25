#this does not work because you cannot import things in python_scripts.
#I'm reimplementing this functionality in a RESTful command 

import requests
import re
import json

bearer_token = data.get('bearer_token')
text = data.get('status')
emoji = data.get('emoji')

if re.match(":[a-zA-Z]+:",emoji) is None:
	logger.error("Emoji not valid")


url = "https://slack.com/api/users.profile.set"

payload = "{\"profile\":{\"status_text\": \""+ text +"\",\"status_emoji\": \""+ emoji +"\"}}"
headers = {
	'Content-Type': "application/json; charset=utf-8",
	'Authorization': "Bearer "+ bearer_token,
	'Cache-Control': "no-cache",
	}

response = requests.request("POST", url, data=payload, headers=headers)

logger.info(json.decode(response.text)["ok"])

