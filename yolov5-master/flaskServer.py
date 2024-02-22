import base64
import random
import string
import os
from time import sleep

from flask import Flask, request, send_file, jsonify
import detect

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def base64get():
    base64_str = request.json['base64']
    image_path = base64_to_images(base64_str)
    object_list = detect.startidentify(basedir + "/getimage/" + image_path)
    encode_str = image_to_base64(basedir + "/setimage/" + image_path)
    data = {
        "imgName": image_path,
        "base64": encode_str,
        "objectList": object_list
    }
    return jsonify(data)


def base64_to_images(base64_str):
    avatar_str = base64_str.replace('data:image/png;base64,', '')
    avatar_bytes = base64.b64decode(avatar_str)
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    image_path = basedir + "/getimage/" + random_string + ".jpg"
    with open(image_path, 'wb+') as fp:
        fp.write(avatar_bytes)
    return random_string + ".jpg"


def image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode("utf-8")


app.run("127.0.0.1", 5555)
