from flask import Flask, render_template,request

app = Flask(__name__)

food = [{'name': 'com rang', 'price': 30}, {'name': 'ga ran', 'price': 160}]


@app.route('/', methods=['Get'])
def index():
    return render_template('index.html', data=food)


@app.route('/', methods=['POST'])
def post_food():
    food_name = request.form.get('name')
    food.append({'name': food_name,'price':0})
    return render_template('index.html', data=food)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
