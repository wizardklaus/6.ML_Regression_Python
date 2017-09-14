params = urllib.urlencode({
    'subscription-key': "****",

    'analyzesFaceLandmarks': 'true',

    'analyzesAge': 'true',

    'analyzesGender': 'true',

    'analyzesHeadPose': 'true',

})

#specify image from file

#For a local image, Content-Type should be application/octet-stream or multipart/form-data AND JSON SHOULD BE EMPTY

headers = {

    'Content-type': 'application/octet-stream',

}

body = ""

#load image

filename = 'C:/testPicutre.JPG'

f = open(filename, "rb")

body = f.read()

f.close()

conn = httplib.HTTPSConnection('api.projectoxford.ai')

conn.request("POST", "/face/v0/detections?%s" % params, body, headers)

response = conn.getresponse("")

data = response.read()

print(data)

conn.close()