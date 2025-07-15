import os, json

RAKUTEN_APP_ID = os.getenv("RAKUTEN_APP_ID")
RAKUTEN_AFF_ID = os.getenv("RAKUTEN_AFF_ID")
GENRE_ID = "558944"  # 韓国インテリア

SERVICE_JSON = json.loads(os.getenv("SERVICE_JSON", "{}"))
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")
