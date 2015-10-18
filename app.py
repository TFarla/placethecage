from flask import Flask

app = Flask(__name__, static_path='/public')

@app.route('/')
def index():
    return 'hello world!'

@app.route('/<int:width>', defaults={'height': None})
@app.route('/<int:width>/<int:height>')
def get_nic_pic(width, height):
    if height is None:
        height = width
    return ''

if __name__ == '__main__':
    app.run(debug=True)
