from dotenv import dotenv_values, load_dotenv
import requests
import json
import os

load_dotenv()

slack_token= os.getenv("token")
slack_channel= os.getenv("channel")
slack_icon_emoji= os.getenv("slack_icon_emoji")
slack_user_name= os.getenv("slack_user_name")

print(slack_channel)

def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': text,
        'icon_emoji': slack_icon_emoji,
        'username': slack_user_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()	

slack_info = 'Test Message'

post_message_to_slack(slack_info)
print("Message sent")