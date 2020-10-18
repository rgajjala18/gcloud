import pathlib
import google.cloud.storage as gcs
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os


credentials_dict = {
    'type': 'service_account',
    'client_id': "116099216654881955752",
    'client_email': "emotdetection@emotion-detection-292814.iam.gserviceaccount.com",
    'private_key_id': "de00388cb1fa027a7ad89a502caa38c424ee99b9",
    'private_key': "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDJeRgeUu0TVG4b\nTOPq/ftdtISpnLa3VOVOe8nYp4rVm1jIMRZJ0OCGOA9WvVVEbAQ0gOmUvYhzoudE\npOZcR/i6OBApbBcUOoxDf9A1udxJTR0u5ddFofFYH5ypQCsLZnWPThC1tcTDRvXb\nSEWFmNKwMjFA2A4Yq933bFIjNDpnVD4C7fpfY3N7MWi9nq0h0W9FtI3HKSRAANuD\nW3L1eXDuLKHFGBRRhpuhmw4vuAyppaBOkZmkgrjMVAg2QVuAIpNUCU1zB4WbniEm\n14lHYscOjj2pbxG4tqtixf7Tw7M0Oln3hnFTEVbusxnP0xm9nmSrxzRqh+47AtiE\nmphGEcEPAgMBAAECggEAEGu3vQT6QKiRftUiAG2p9qW3aFGXDNM1C1QIjAl/xdAv\nCMYDcIm/OwFHssSktfptz0+wegiGnhIpck1UXzIYgij+nDmsmd/5vailsjNPUoQf\n/EoMZScBUjLlZGAQAhJcQ41TzFOf0WCvuismS3C8v1Kf9A6H+5fKdBeWjDr+BZzR\nk7vVJye91I8xoEVOtEAi3K7D9sMAVQ6EIw4OrB5bHbV+XbHnva6rm2GliWywtUqa\nScMXFg864c75+kB1+u2+7HYb05Gt8pr3v4j3JAe4liY/QZWouFq2h5qjTkxL+3o8\nbCXKLZ1W7u2KgnPXq532cuzGGeLgHycwI51WUgA7jQKBgQDrZez3tXD/qL9JIYc5\n8WuTjGQcH1pfo6NIwqcMq60v4SZSbkgNMp7dp+TZ0EL+vuf52LbXPzVKzRpa1T1r\nEAYeRwqNEuUkXymxWmiAqdlV6w/0IOTNCnq+F1TQPcmAdXD+DYPJj2LT9/Fpha+2\nIyOMzYEfe3SAUGx8CRj8AnB4owKBgQDbGxRIRyChYsaPsBSHE2jxtPiD/HKf5W/Z\nFOcF7GM2MUB9Pmersk7LXlJOM7B6HLagC3B3JM1TG7l1uaiam05hP0TCKgyAIpo7\n3rUeLry3w8STfgAUzSBBPzZ559TBDNk6QFDnZDwoCMc6JpuVSAQHrjFUC6pNTQmo\nn5J701wApQKBgQDDIUyb0eYHp6RZRNfJqlxYhQn/XeYWXZlfGSxMjosTo3mW3yAP\nAKU8bI6CF+dRMIMvUvvN1fGhPf/Yx+cPtsq7knwmkUEtM01mXOE/towYcrBY2GOR\nrFwu8zw1GuLL/45Yqm9SR+/OcjvGEzGis+ImN7wPktDyBLjI4Om7DXKaLQKBgQDD\n+i2jFJO4JnyKKynBQ/g7Me6TR6tTH8pyNgMJxk1bPKR9IeNirMNTnhMqRYuVPbeP\n4Yt/1hgdPRAen6iSWVW7H/clYKz7s3eXE3WXAKDmEaHzduElufAezCay1Uz0O8TV\nGJAE2CACgw+IEN5aoSaRpBoVHbX/HGgGPmysevmwzQKBgQDkfGvbHMnQ+UAWOZvj\nCQxCIE46PVuxFoAE+1HPquo2I6uPGtd0qj47nvh1wpe5sEc2MmmuVURNTtZyG1GW\nzNZR/TedtJB516IYS3DFvtzfglbZxPAPUaKk2mw3kuAoEaTBmRs7lLCDSUzvuHzj\nSU28MqHo6za7kU7w83gfqH/vRQ==\n-----END PRIVATE KEY-----\n",
}
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