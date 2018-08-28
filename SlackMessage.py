#Posting to a Slack Channel
def send_message_to_slack(text):
	from urllib import request,parse
	import json

	post={"text": "{0}".format(text)}

	try:
		json_data=json.dumps(post)
		req=request.Request("******",
		data=json_data.encode('ascii'),
		headers={'Content-Type':'application/json'})
		resp=request.urlopen(req)
	except Exception as em:
		print("EXCEPTION: "+str(em))

send_message_to_slack("Hi Channel!.. Good Morning....")