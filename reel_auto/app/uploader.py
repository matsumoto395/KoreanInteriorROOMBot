from pydrive2.auth import GoogleAuth, ServiceAccountCredentials
from pydrive2.drive import GoogleDrive
import json, os
from .config import SERVICE_JSON, DRIVE_FOLDER_ID

def get_drive():
    gauth = GoogleAuth()
    gauth.auth_method = 'service'
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        SERVICE_JSON, ['https://www.googleapis.com/auth/drive.file'])
    return GoogleDrive(gauth)

def upload(file_path: str) -> str:
    drive = get_drive()
    meta = {"title": os.path.basename(file_path)}
    if DRIVE_FOLDER_ID:
        meta["parents"] = [{"id": DRIVE_FOLDER_ID}]
    f = drive.CreateFile(meta)
    f.SetContentFile(file_path)
    f.Upload()
    return f["alternateLink"]
