import requests

url = "http://127.0.0.1:5000/projets"

payload = "title=zefzef&description=zefezfezfzeffezfez&author=fezfz&wanted_price=500"
headers = {
    'Content': "application/json",
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "7eb100b9-4c4d-454e-84a6-d8fbbe108900,e9b9d02a-b89a-40bf-a196-bed0edd85f9e",
    'Host': "127.0.0.1:5000",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "73",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

count = 0
max = 1000

while count < max:
    response = requests.request("POST", url, data=payload, headers=headers)
    count = count + 1
    print(response.text)