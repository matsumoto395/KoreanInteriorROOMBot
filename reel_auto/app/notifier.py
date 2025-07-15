import os, json
from slack_sdk.webhook import WebhookClient
from .config import SLACK_WEBHOOK

def notify(text: str, link: str):
    if not SLACK_WEBHOOK:
        return
    WebhookClient(SLACK_WEBHOOK).send(json={"text": text, "attachments":[{"text": link}]})
