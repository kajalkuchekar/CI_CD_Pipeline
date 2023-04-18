from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the calculator!'

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        result = float(num1) + float(num2)
        return 'The sum of {} and {} is {}'.format(num1, num2, result)
    else:
        return '''
            <form method="post">
                <label>Number 1:</label>
                <input type="text" name="num1"><br>
                <label>Number 2:</label>
                <input type="text" name="num2"><br>
                <input type="submit" value="Add">
            </form>
        '''

@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        result = float(num1) - float(num2)
        return 'The difference between {} and {} is {}'.format(num1, num2, result)
    else:
        return '''
            <form method="post">
                <label>Number 1:</label>
                <input type="text" name="num1"><br>
                <label>Number 2:</label>
                <input type="text" name="num2"><br>
                <input type="submit" value="Subtract">
            </form>
        '''

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        result = float(num1) * float(num2)
        return 'The product of {} and {} is {}'.format(num1, num2, result)
    else:
        return '''
            <form method="post">
                <label>Number 1:</label>
                <input type="text" name="num1"><br>
                <label>Number 2:</label>
                <input type="text" name="num2"><br>
                <input type="submit" value="Multiply">
            </form>
        '''

@app.route('/divide', methods=['GET', 'POST'])
def divide():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        if float(num2) == 0:
            return 'Error: cannot divide by zero'
        else:
            result = float(num1) / float(num2)
            return 'The quotient of {} and {} is {}'.format(num1, num2, result)
    else:
        return '''
            <form method="post">
                <label>Number 1:</label>
                <input type="text" name="num1"><br>
                <label>Number 2:</label>
                <input type="text" name="num2"><br>
                <input type="submit" value="Divide">
            </form>
        '''
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
