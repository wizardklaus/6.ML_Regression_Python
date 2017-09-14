import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, urllib
import requests

subscription_key = 'fc2f005320f249dd9925ea43855c43ec'
# subscription_key = 'f24bd15a-0323-4305-9d36-4c4b295b8de3'

url = 'https://api.projectoxford.ai/face/v1.0/detect'

body = ""

filename = 'C:\Temp\Taylor.jpg'

# data = open(filename, 'rb')
with open(filename, 'rb') as f :
    data = f.read()

# you'll need to define the following variables yourself:
# - params
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,'
                            'facialHair,glasses,emotion,hair,makeup,occlusion,'
                            'accessories,blur,exposure,noise',
}

# - header
headers = {
    'Content-type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

try :
    response = requests.post(url, params=params, headers=headers, data=data)
    # returned = response.json()
    parsed = json.loads(response.text)
    print(json.dumps(parsed, sort_keys=True, indent=2))

except Exception as e :
    print("Error:")
    print(e)

"""
try :
    response = requests.post(url, headers=headers, data=data)
    print('Response:')
    parsed = json.loads(response.text)
    # parsedData = json.loads(response.text)
    print(json.dumps(parsed, sort_keys=True, indent=2))

except Exception as e :
    print("Error:")
    print(e)
"""