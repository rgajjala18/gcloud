import pathlib
import google.cloud.storage as gcs
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os


credentials_dict = {} #removed credentials for security purposes

credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    credentials_dict
)
client = storage.Client(credentials=credentials, project='Emotion Detection - ACTUAL')

#set target file to write to
target = pathlib.Path("local_file.txt")

#set file to download
FULL_FILE_PATH = "gs://voice-files/en-AU.wav"

#open filestream with write permissions
with target.open(mode="wb") as downloaded_file:
	#download and write file locally 
	client.download_blob_to_file(FULL_FILE_PATH, downloaded_file)
