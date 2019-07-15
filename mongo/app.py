from flask import Flask, render_template, request, redirect, url_for
from mongodb2 import get_all_food, insert_food, delete_food_id

app = Flask(__name__)



# foods = [
#     {'name': 'com rang', 'price': 30, 'id': 1},
#     {'name': 'ga ran', 'price': 160, 'id': 2}
# ]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data = get_all_food())


@app.route('/delete/<food_id>')
def delete_food(food_id):
    delete_food_id(food_id)
    return redirect(url_for('index'))


@app.route('/', methods=['POST'])
def post_food():
    food_name = request.form.get('name')
    food_price = request.form.get('price')
    insert_food(food_name,food_price)
    # foods.append({'name': food_name, 'price': food_price})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
