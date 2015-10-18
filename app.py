from flask import Flask, send_file
from PIL import Image
from io import BytesIO
from os import listdir
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!'

@app.route('/<int:width>', defaults={'height': None})
@app.route('/<int:width>/<int:height>')
def get_nic_pic(width, height):
    if height is None:
        height = width

    img = Image.open(get_best_suited_pic(width, height))
    out = img.resize((width, height))

    img_io = BytesIO()
    out.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

def get_best_suited_pic(width, height):
    aspect_ratio = width / height
    images_path = Path('private/images')
    ratios = [0.7, 1.0, 1.2, 1.3, 1.5, 1.8]
    ratio = min(ratios, key=lambda x:abs(x - aspect_ratio))
    return str(images_path / 'nic{}.jpg'.format(ratio))

if __name__ == '__main__':
    app.run(debug=True)
