

# 190710 startcamp - day3

## git

### 터미널

* Ctrl + C (Cancle) : 취소

* Ctrl + D (destroy) : 종료

보통 Ctrl + C를 하고 Ctrl + D를 함

## 사용자의 입력을 받는 방법

* input - 검은화면에서 사용(거의 안씀)

* @app.route('/hello/<name>')

  ​	def hello(name):

  ​    return f'hi, {name}'

* 패키지로 가져오기

----

## 같은 말

* 'What is your name?' = 'What`/'`s your name?'

* import random

  `random.choice([1, 2, 3, 4, 5]) =`

  ` from random import choice`

  `choice([1, 2, 3, 4, 5])`

   # 두개가 같다. 뭉태기가 클 때 쓴다.

  

## 첫 글자와 마지막 글자 출력

```python
words = input('입력 고고: ')  # 사용자의 입력을 받는 방법(1)
print(type(words))  # input안에 들어가는 타입은 string
print(words[0], words[-1])  # words 의 첫 글자와 마지막 글자를 출력하라.
# words[-1] = words[length - 1]
int(words)  # type(words) : str -> int
for number in range(1, words + 1):  # n을 입력받고, 1부터 n까지 출력하라.
print(number, end='반 ')
```



## Fizz Buzz

* 3배수 fizz / 5배수 buzz / 15배수 fizzbuzz

```python
number = int(input('숫자를 입력하세요: '))

for i in range(1, number + 1)
if(i % 3 == 0) and (i % 5 == 0):
    print('fizzbuzz')

elif i % 3 == 0:
    print('fizz')

elif i % 5 == 0:
    print('buzz')

else:
    print(i)
```



## api로 가져오기

```python
import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
# {
  "totSellamnt": 81961886000,
  "returnValue": "success",
  "drwNoDate": "2019-07-06",
  "firstWinamnt": 2240409000,
  "drwtNo6": 39,
  "drwtNo4": 34,
  "firstPrzwnerCo": 9,
  "drwtNo5": 37,
  "bnusNo": 12,
  "firstAccumamnt": 20163681000,
  "drwNo": 866,
  "drwtNo2": 15,
  "drwtNo3": 29,
  "drwtNo1": 9 }

response = requests.get(url).text
print(response)  # text값으로 출력
print(type(response))  # <class 'str'>
print(dict(response))  # <class 'dict'>

data = json.loads(response)  # response의 dict의 값을 data의 저장

print(type(data),data)
print(data['bnusNo'])  # Key가 'bnusNo'인 Value값을 가져온다.

real_numbers = []  # real_numbers의 리스트를 만든다.
for key, value in data.items:
    if 'drwtNo' in key:
        real_numbers.append(value) 
        #  key에 'drwtNo'가 포함되어 있으면 real_numbers 리스트에 value값을 추가한다.
        
print(real_numbers)  # real_numbers 출력
```



## Flask

```python
import random
from flask import Flask # 웹으로 전달 가능하게 해주는 것

app = Flask(__name__)  # ??


@app.route('/')  # '/'는 기본값
def index():
    return 'Hello World!'


@app.route('/hi')
def hi():
    return 'Hi'


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


if __name__ == '__main__':  # ??
    app.run(debug=True)

```

## HTML의 기본구조

```html
<html>

	<head>

		<meta charset="utf-8">

	</head>

    <body>

        <h1>Today I Learnde</h1>

        <h2>Learn Flask</h2>

        <ol>

            <li>pip install flask</li>

            <li>touch app.py</li>

            <li>python app.py</li>

        </ol>

        <h2>Learn HTML</h2>

        <u1>

            <li>doctype html</li>

            <li>head, body</li>

            <li>h1, h2, ol, ul</li>

        </u1>

    </body>

</html>
```





## 로또

my = [1, 2, 3, 4, 5, 6]



real = [1, 2, 3, 4, 5, 6]

bonus = 7



\# my 와 real 의 6개가 같으면 1등

\# my 와 real 이 5개가 같고 나머지 하나가 bonus 면 2등

\# my 와 real 이 5개가 같으면 3등

\# '' 4개가 같으면 4등

\# '' 3개가 같으면 5등

\# 나머지는 꽝



for i in range(6):

​    for j in range(6):

​        if my[i] == real[j]:

​            true = 1

​            true = true + 1



if true == 6:

​    print('1등')

elif true == 5:

​    print('3등')

elif true == 4:

​    print('4등')

elif true == 3:

​    print('5등')

else:

​    print('꽝')

