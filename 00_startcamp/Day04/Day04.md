# 190711 startcamp - day4



## Art

```python
import datetime

from art import *  # *은 모든것을 가져온다는 의미
from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)

@app.route('/art')
def art():
    return render_template('art.html')  # art.html에게 요청한다.
```

```html
<!DOCTYPE html>
<html lang="kr">  <!-- 자주 사용하는 언어가 kroean이다.  -->
<head>  <!-- 뇌를 의미 -->
    <meta charset="UTF-8">  <!-- 한글을 안깨지게 해줌 -->
    <title>Make art</title>  <!-- 창 제목 -->
</head>
<body>  <!-- 외관을 의미 -->
    <h1>Put some text</h1>  <!-- 제목 -->
    <form action="/result">  <!-- form과 action은 붙어다님 action 목적지 설정 -->
        <input type="text" name="input_text" >
        <select name="font">  <!-- select는 범위를 잡아주기 위한 것 -->
            <option value="random">랜덤</option>  <!-- 텍스트 : 랜덤, 실제값 : random --> 
            <option value="block">블록</option>  <!-- 텍스트 : 블록, 실제값 : block -->
            <option value="white_bubble">동그라미</option>  <!-- 텍스트 : 동그라미, 실제값 : white_bubble -->
        </select>
        <input type="submit" value="결과보기">  <!-- 형식 : 제출 형식, 텍스트 : 결과보기 -->
    </form>
</body>
</html>
```



## result



```python
@app.route('/result')
def result():
    input_text = request.args.get('input_text')  # art.html에 있는 name=input_text를 가져온다.
    font = request.args.get('font')  #  art.html에 있는 name=font를 가져온다.
    print(input_text, font)  # input_text, font 출력한다.
    
    result = text2art(input_text, font=font)  # input_text에 font를 font(랜덤, 블록 ...) 바꿔준다.
    
    return render_template('result.html', result=result)   # ??
```



```html
<!DOCTYPE html>
<html lang="kr">  <!-- 자주 사용하는 언어가 kr이다. -->
<head>
    <meta charset="UTF-8">  <!-- 한글을 깨지지 않게 해줌 -->
    <title>Result</title>  <!-- 창 제목 -->
</head>
<body>
    <h1>Result</h1>  <!-- 제목 -->
    <pre>{{  result  }}</pre>  <!-- pre 글자 그대로를 내보내줌 -->
</body>
</html>
```



```python
@app.route('/add')
def add():
    return render_template('add.html') # add.html에게 요청한다
```



```html
<!DOCTYPE html>
<html lang="kr">  <!-- 자주 사용하는 언어가 kr이다. -->
<head>
    <meta charset="UTF-8">  <!-- 한글이 깨지지 않게 해줌 -->
    <title>Add 2 numbers</title>  <!-- 창 제목 -->
</head>
<body>
    <h1>Plus</h1>
    <form action="/result">  <!-- form과 action은 붙어다님 action 목적지 설정 -->
        <input type="text" name="num1" placeholder="give me number" autofocus>
        <!-- 텍스트 타입, 이름=num1, 입력 전 문구=give me number, 자동으로 포커스를 잡아줌 -->
        + <input type="text" name="num2" placeholder="give me number" autofocus>
        <!-- 텍스트 타입, 이름=num2, 입력 전 문구=give me number, 자동으로 포커스를 잡아줌 -->
        <input type="submit" value="결과보기">  <!-- 형식 : 제출 형식, 텍스트 : 결과보기 -->
    </form>
</body>
</html>
```



```python
@app.route('/result')
def result():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    result = int(num1) + int(num2)
    
    return render_template('result.html', result=result)
```







app.route('/')

def index():

​    return render_template('index.html')





def send():

​    print(request.headers)

​    return render_template('send.html')





def receive():



​    stock = Stock(request.args.get('stk'), token='pk_63c229409ff14b67a6cc81e38927f1c4').get_quote()

​    company_name = stock['companyName']

​    latest_price = stock['iexRealtimePrice']

​    data = request.args.get('msg')

​    print(request.args)

​    return render_template(

​        'receive.html',

​        c_name=company_name,

​        l_price=latest_price

​    )





def dday():

​    today = datetime.datetime.now()

​    end_date = datetime.datetime(2019, 11, 29)

​    left = end_date - today

​    return render_template('dday.html', left_days=left.days)





def boxoffice():

​    top_5 = [

​        '스파이더맨 파 프롬 홈',

​        '알라딘',

​        '토이스토리4',

​        '존윅3',

​        '라이온킹'

​    ]

​    return render_template('boxoffice.html', movies=top_5)



if __name__ == '__main__':

​    app.run(debug=True)



<head>
     <meta charset="utf-8">
</head>