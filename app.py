from flask import Flask

app = Flask(__name__, static_path='/public')

@app.route('/')
def index():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug=True)
