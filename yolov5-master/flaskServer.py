import os
from flask import Flask, request, send_file
import detect

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

@app.route('/image',methods = ['GET','POST'])
def index():
    img = request.files.get('imagefile')
    path = basedir + "/getimage/"
    img_name = img.filename
    file_path = path + img_name
    img.save(file_path)
    detect.startidentify(file_path)
    print(img_name)
    return img_name

@app.route('/imageget', methods=['GET', 'POST'])
def indexget():
    filename = request.form.get("filename")
    return send_file(basedir + "/setimage/" + filename, mimetype="image/jpeg")


app.run("127.0.0.1", 5555)