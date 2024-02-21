import base64
import random
import string
import os
from flask import Flask, request, send_file, jsonify
import detect


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


@app.route('/image',methods = ['GET','POST'])
def index():
    print(request.files)
    img = request.files.get('imagefile')
    path = basedir + "/getimage/"
    img_name = img.filename
    file_path = path + img_name
    img.save(file_path)
    # url = '/static/img/' + img_name
    detect.startidentify(file_path)
    # print(img_name)
    data = {
        "imgName":img_name
    }
    return jsonify(data)

@app.route('/imageget', methods=['GET', 'POST'])
def indexget():
    filename = request.form.get("filename")
    return send_file(basedir + "/setimage/" + filename, mimetype="image/jpeg")

    # img = request.files.get('imagefile')
    # path = basedir + "/getimage/"
    # img_name = img.filename
    # file_path = path + img_name
    # img.save(file_path)
    # # url = '/static/img/' + img_name
    # detect.startidentify(file_path)
    # return send_file(basedir + "/setimage/" + img.filename, mimetype='image/jpeg')

@app.route('/upload',methods=['GET', 'POST'])
def base64get():
    base64_str = request.json['base64']
    image_path = base64_to_images(base64_str)

    detect.startidentify(image_path)
    data = {
        "imgName": image_path
    }
    return jsonify(data)

def base64_to_images(base64_str):
    avatar_str = base64_str.replace('data:image/png;base64,', '')
    avatar_bytes = base64.b64decode(avatar_str)
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    image_path = basedir + "/getimage/" + random_string +".jpg"
    with open(image_path, 'wb+') as fp:
        fp.write(avatar_bytes)
    return image_path




app.run("127.0.0.1", 5555)