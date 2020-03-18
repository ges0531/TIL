import requests
url = 'http://13.125.222.176/quiz/jordan'
headers = {
    'Accept': 'application/json',
    'Content-Type' : 'application/json; charset=utf-8'
}
data = {
    'nickname' : "서울 1반김은수",
    'yourAnswer' : "Kubernetes"
}

res = requests.post(url, headers=headers, json=data)
print(res.text)