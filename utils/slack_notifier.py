import certifi, logging, os, ssl, sys
from datetime import date
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

block_reply = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ""
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "View run",
					"emoji": True
				},
				"value": "view_run",
				"url": "",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ""
			}
		}
	]

failed = {
    "result_lede": ":x:",
    "result_text": "Workflow failed.",
    "color": "#FB3728"
}

passed = {
    "result_lede": ":white_check_mark:",
    "result_text": "Workflow successful.",
    "color": "#1F5E19"
}

skipped = {
    "result_lede": ":no_entry_sign:",
    "result_text": "Workflow skipped.",
    "color": "#C4BCC0"
}


def alert_reply(alert, threadID):

    block = block_reply

    if alert["state"] == "up":
        color = passed["color"]
        block[0]["text"]["text"] = "{0} *{1}*".format(passed["result_lede"], alert["template"])
        block[0]["accessory"]["url"] = alert["run"]
        block[1]["text"]["text"] = "<{0}|View the pull request>".format(alert["pr"])
    elif alert["state"] == "down":
        color = failed["color"]
        block[0]["text"]["text"] = "{0} *{1}*\n\n{2}".format(failed["result_lede"], alert["template"], failed["result_text"])
        block[0]["accessory"]["url"] = alert["run"]
        block[1]["text"]["text"] = "_{}_".format(alert["message"])
    elif alert["state"] == "skip":
        color = skipped["color"]
        block[0]["text"]["text"] = "{0} *{1}*\n\n{2}".format(skipped["result_lede"], alert["template"], skipped["result_text"])
        block[0]["accessory"]["url"] = alert["run"]
        block[1]["text"]["text"] = "_{}_".format(alert["message"])

    try:
        result = client.chat_postMessage(
            channel=channel_id, 
            thread_ts=threadID,
            text='',
            attachments = [{
                "color": color,
                "blocks": block
            }]
        )
        return result
    except SlackApiError as e:
        logger.error(f"Error posting message: {e}")


def alert_start(alert):
    try:
        today = date.today()
        # Call the chat.postMessage method using the WebClient
        result = client.chat_postMessage(
            channel=channel_id, 
            text='',
            link_names=True,
            attachments = [
                {
                    "color": os.environ.get("JOB_COLOR"),
                    "blocks": [
                        {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": os.environ.get("JOB_ID"),
                                "emoji": True
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": alert["message"]
                            },
                            "accessory": {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "View run",
                                    "emoji": True
                                },
                                "value": "view_run",
                                "url": alert["run"],
                                "action_id": "button-action"
                            }
                        },
                        {
                            "type": "context",
                            "elements": [
                                {
                                    "type": "plain_text",
                                    "text": today.strftime("%d %B %Y"),
                                    "emoji": True
                                }
                            ]
                        },
                        {
                            "type": "divider"
                        }
                    ]
                }
            ]
        )
        return result["message"]["ts"]

    except SlackApiError as e:
        logger.error(f"Error posting message: {e}")

def alert_finish(alert, messageID):
    try:
        today = date.today()
        # Call the chat.postMessage method using the WebClient
        result = client.chat_update(
            channel=channel_id, 
            ts=messageID,
            link_names=True,
            text='',
            attachments = [{
                "color": os.environ.get("JOB_COLOR"),
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": os.environ.get("JOB_ID"),
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": alert["message"]
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "View run",
                                "emoji": True
                            },
                            "value": "view_run",
                            "url": alert["run"],
                            "action_id": "button-action"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Finished*"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "cc: <@chad>"
                        }
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "plain_text",
                                "text": today.strftime("%d %B %Y"),
                                "emoji": True
                            }
                        ]
                    },
                    {
                        "type": "divider"
                    }
                    ]
                }]
        )
        return result

    except SlackApiError as e:
        logger.error(f"Error posting message: {e}")


channel_id = os.environ.get("CHANNEL_ID")
ssl_context = ssl.create_default_context(cafile=certifi.where())
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"), ssl=ssl_context)
logger = logging.getLogger(__name__)
message_ts = os.environ.get("THREAD_ID")

if sys.argv[1] == "start":
    alert = {
        "state": sys.argv[1],
        "run": sys.argv[2],
        "message": sys.argv[3],
    }
    result = alert_start(alert)
elif sys.argv[1] == "finish":
    alert = {
        "state": sys.argv[1],
        "run": sys.argv[2],
        "message": sys.argv[3]
    }
    result = alert_finish(alert, message_ts)
else:
    alert = {
        "state": sys.argv[1],
        "template": sys.argv[2],
        "run": sys.argv[3],
        "pr": sys.argv[4],
        "message": sys.argv[5]
    }
    result = alert_reply(alert, message_ts)
print(result)
