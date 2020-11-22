from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os


credentials_dict = {} #removed credentials for security purposes
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict)

client = storage.Client(credentials=credentials, project='Emotion Detection - ACTUAL')
bucket = client.get_bucket('bijan-hackathon')
blob = bucket.blob('test_image.png')
blob.upload_from_filename('test_image.png')
