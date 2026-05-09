### routing in flask
from flask import Flask,request,render_template,redirect,url_for
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, Rakesh from Flask!'

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f'Hello, {name}! Welcome to Flask!'

@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def add(num1, num2):
    result = num1 + num2
    return f'The sum of {num1} and {num2} is {result}.'

@app.route('/result', methods=['POST'])
def result():
    return 'This is a POST request to /result.'

@app.route('/about', methods=['GET', 'POST'])
def about():
    return 'This is the about page.'

@app.route('/multiple/<string:comma_separated_numbers>', methods=['GET', 'POST'])
def multiple(comma_separated_numbers):
    if request.method == 'POST':
        return 'This is a POST request to /multiple.'
    elif request.method == 'GET':
        listnumbers = comma_separated_numbers.split(',')
        return f'multiple of {listnumbers} is: { eval("*".join(str(int(num)) for num in listnumbers)) }'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        math = request.form.get('maths')
        science = request.form.get('science')
        history = request.form.get('history')
        # Perform calculations or further processing here
        # For example, calculate the average of the three subjects
        try:
            math = int(math)
            science = int(science)
            history = int(history)
            average = (math + science + history) / 3
            #return f'The average marks are: {average:.2f}'
            #return render_template('form.html', result=int(average))
            reqUrl = ""
            if average >= 30:
                reqUrl = "success"
            else:
                reqUrl = "fail"
            return redirect(url_for(reqUrl, result=int(average)))
        except ValueError:
            return 'Please enter valid numbers for all subjects.'
        
    elif request.method == 'GET':
        return render_template('form.html')
    
@app.route('/success/<int:result>', methods=['GET', 'POST'])
def success(result):
    return f'The result marks are: {result:.2f} - Congratulations!'

@app.route('/fail/<int:result>', methods=['GET', 'POST'])
def fail(result):
    return f'The result marks are: {result:.2f} - Better luck next time!'

@app.route('/api/addition',methods=['POST'])
def api_addition():
    data = request.get_json()
    num1 = data.get('a')
    num2 = data.get('b')
    result = num1 + num2
    return {'Addition value': result}

@app.route('/api/substraction',methods=['POST'])
def api_subtraction():
    data = request.get_json()
    num1 = data.get('a')
    num2 = data.get('b')
    result = num1 - num2
    return {'Subtraction value': result}

@app.route('/api/multiplication',methods=['POST'])
def api_calculation():
    data = request.get_json()
    num1 = data.get('a')
    num2 = data.get('b')
    result = num1 * num2
    return {'Multiplication value': result}

@app.route('/api/division',methods=['POST'])
def api_division():
    data = request.get_json()
    num1 = data.get('a')
    num2 = data.get('b')
    result = num1 / num2 if num2 != 0 else None
    return {'Division value': result}

@app.route('/api/ArgCalculations',methods=['POST'])
def api_ArgCalculations():
    num1 = int(request.args.get('a'))
    num2 = int(request.args.get('b'))
    num3 = int(request.args.get('c'))
    num4 = int(request.args.get('d'))
    result = num1 * num2 * num3 * num4
    return {'Multiplication value by multiple arguments': result}

@app.route('/api/GetUserDetails',methods=['POST'])
def api_GetUserDetails():
    df = pd.read_csv('customers100.csv')
    user_id = request.args.get('user_id')
    user_details = df[df['Customer Id'] == user_id].to_dict(orient='records')
    return {'user_details': user_details}

@app.route('/api/GetUserDetails3',methods=['POST'])
def api_GetUserDetails3():
    df = pd.read_csv('customers100.csv')
    user_id = request.args.get('user_id')
    user_details = df[df['Customer Id'] == user_id].to_dict(orient='records')
    return {'user_details': user_details}

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)