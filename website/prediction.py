from flask import Blueprint, render_template, request, send_from_directory
from .app_functions import ValuePredictor, pred
import os
from werkzeug.utils import secure_filename

prediction = Blueprint('prediction', __name__)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

dir_path = os.path.dirname(os.path.realpath(__file__))



@prediction.route('/predict', methods=["POST", 'GET'])
def predict():

    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result, page = ValuePredictor(to_predict_list) 
        return render_template("result.html", prediction=result, page=page)
    else:
        return render_template( 'base.html')

@prediction.route('/upload', methods=['POST','GET'])
def upload_file():
    if request.method=="GET":
        return render_template('pneumonia.html', title='Pneumonia Disease')
    else:
        file = request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath,'uploads',  secure_filename(file.filename))
        file.save(file_path)
        indices = {0: 'Normal', 1: 'Pneumonia'}
        result = pred(file_path)

        if result>0.5:
            label = indices[1]
            accuracy = result * 100
        else:
            label = indices[0]
            accuracy = 100 - result
        return render_template('deep_pred.html', image_file_name=file.filename, label = label, accuracy = accuracy)

@prediction.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)