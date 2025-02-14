#!/usr/bin/python

# You get the environment parameters from your 
# application dashbord in your developer account 
# https://developers.ringcentral.com

import os
import sys
import time
 
from dotenv import load_dotenv
from urllib.request import urlopen
from ringcentral import SDK
load_dotenv()

CHAT_ID = '<GROUP ID>'

rcsdk = SDK( os.environ.get('RC_CLIENT_ID'),
             os.environ.get('RC_CLIENT_SECRET'),
             os.environ.get('RC_SERVER_URL') )
platform = rcsdk.platform()
try:
  platform.login( jwt=os.environ.get('RC_JWT') )

except Exception as e:
  sys.exit("Unable to authenticate to platform: " + str(e))

def create_compliance_export_task():
    print("Create export task.")
    endpoint = "/team-messaging/v1/data-export"
    params = {
	"timeFrom": "2021-01-01T00:00:00.000Z",
	"timeTo": "2021-01-31T23:59:59.999Z"
      }
    resp = platform.post(endpoint, params)
    json = resp.json()
    get_compliance_export_task(json.id)

def get_compliance_export_task(taskId):
    print("Check export task status ...")
    endpoint = "/team-messaging/v1/data-export/" + taskId
    response = platform.get(endpoint)
    jsonObj = response.json()
    if jsonObj.status == "Completed":
        length = len(jsonObj.datasets)
        for i in range(length):
            fileName = "rc-export-reports_" + jsonObj.creationTime + "_" + str(i) + ".zip"
            get_report_archived_content(jsonObj.datasets[i].uri, fileName)
    elif jsonObj.status == "Accepted" or jsonObj.status == "InProgress":
        time.sleep(5)
        get_compliance_export_task(taskId)
    else:
        print (jsonObj.status)

def get_glip_report_archived_content(contentUri, fileName):
    print("Save export zip file to the local machine.")
    uri = platform.create_url(contentUri, False, None, True);
    fileHandler = urlopen(uri)
    with open(zipFile, 'wb') as output:
        output.write(fileHandler.read())

try:
    rcsdk = SDK( os.environ.get('RC_CLIENT_ID'),
                 os.environ.get('RC_CLIENT_SECRET'),
                 os.environ.get('RC_SERVER_URL') )
    platform = rcsdk.platform()
    platform.login( jwt=os.environ.get('RC_JWT') )
    create_compliance_export_task()
except Exception as e:
    sys.exit( f'Could not generate export: {e}' )
else:
    sys.exit(0)
