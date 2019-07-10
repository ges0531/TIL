import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
# print(response)
# print(type(response))
# print(dict(response))

data = json.loads(response)

print(type(data), data)

print(data['bnusNo'])

real_numbers = []
for key, value in data.items():  # items()를 안쓰면 딕셔너리에서 키 밖에 못 뽑는다.
    # real_numbers[i] = data[f'drwtNo{i+1}']
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)
