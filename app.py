from flask import Flask, send_file
from PIL import Image
from io import BytesIO

app = Flask(__name__, static_path='/public')

@app.route('/')
def index():
    return 'hello world!'

@app.route('/<int:width>', defaults={'height': None})
@app.route('/<int:width>/<int:height>')
def get_nic_pic(width, height):
    if height is None:
        height = width

    img = Image.open('public/images/nic1.jpg')
    out = img.resize((width, height))

    img_io = BytesIO()
    out.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
