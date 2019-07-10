import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


# @app.rouet('/get_lotto/1')
# def get_lotto_1()  # 1회차 로또정보


# @app.rouet('/get_lotto/<int:num>')
# def get_lotto_1()

@app.route('/hello/<name>')
def hello(name):
    return f'hi, {name}'


@app.route('/pick_lunch/<int:count>')
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '사천탕면',

    ]
    picks = random.sample(menus, count)
    return str(picks)


@app.route('/cube/<int:number>')
def cube(number):
    number = number * number * number  # number ** 3
    return str(number)




if __name__ == '__main__':
    app.run(debug=True)
