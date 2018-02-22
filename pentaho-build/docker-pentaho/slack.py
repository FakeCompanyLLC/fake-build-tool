import requests, os

SLACK_TOKEN = os.environ['SLACK_TOKEN']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']

def postMessage(token=SLACK_TOKEN, channel=SLACK_CHANNEL, text=""):
  session = requests.session()
  data = {
    'token' : token,
    'channel' : channel,
    'text': text
  }
  r = session.post('https://slack.com/api/chat.postMessage', data=data)

