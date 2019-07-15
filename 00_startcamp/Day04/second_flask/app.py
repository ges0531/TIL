import datetime

from art import *
from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/result')
def result():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    print(input_text, font)

    result = text2art(input_text, font=font)

    return render_template('result.html', result=result)


# @app.route('/add')
# def add():
#     return render_template('add.html')
# # pass  # add.html => <input> * 2


# @app.route('/result')
# def result():
#     num1 = request.args.get('num1')
#     num2 = request.args.get('num2')
#     result = int(num1) + int(num2)

#     return render_template('result.html', result=result)
# pass  # result.html => input_data 의 합


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send')
def send():
    print(request.headers)
    return render_template('send.html')


# @app.route('/receive')  # /receive는 유일한 통로
# def receive():

#     stock = Stock(request.args.get('stk'), token='pk_63c229409ff14b67a6cc81e38927f1c4').get_quote()
#     company_name = stock['companyName']
#     latest_price = stock['iexRealtimePrice']
#     data = request.args.get('msg')
#     print(request.args)
#     return render_template(
#         'receive.html',
#         c_name=company_name,
#         l_price=latest_price
#     )

@app.route('/receive', methods=['POST'])  # /receive는 유일한 통로, methods로 쓴 이유는 리스트로 받을 수 있기 떄문에
def receive():

    stock = Stock(request.form.get('stk'), token='pk_63c229409ff14b67a6cc81e38927f1c4').get_quote()
    company_name = stock['companyName']
    latest_price = stock['iexRealtimePrice']
    data = request.args.get('msg')
    print(request.args)
    return render_template(
        'receive.html',
        c_name=company_name,
        l_price=latest_price
    )


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리4',
        '존윅3',
        '라이온킹'
    ]
    return render_template('boxoffice.html', movies=top_5)

if __name__ == '__main__':
    app.run(debug=True)
