import os
import slack

from config import config

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    print(data.get('text', []))
    if 'Hello' in data.get('text', []):
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!",
            thread_ts=thread_ts
        )

# slack_token = os.environ["SLACK_API_TOKEN"]
slack_token = config['Slacker Squad'].get("oauth")
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
