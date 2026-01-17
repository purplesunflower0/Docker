from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <body>
                <form action="/greet" method="POST">
                    Enter Your Name: <input type="text" name="username">
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    return f'Hello, {username}! Welcome to our website.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
