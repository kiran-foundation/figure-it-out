from flask import Flask, render_template, request

from fio import figure_it_out
from fio.resources import *
from fio.figure_it_out import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'],)
def submit():
    bustval = request.form.get('bust')
    waistval = request.form.get('waist')
    hipval = request.form.get('hip')
    highhipval = request.form.get('highhip')

    bust = float(bustval)
    waist = float(waistval)
    hip = float(hipval)
    highhip = float(highhipval)

    body_type_images_list = []
    bodytype = figure_it_out.find_body_type(bust, waist, hip, highhip)
    body_type_images_list = list(figure_it_out.body_type_images(bodytype[0]))
    if type(bodytype) == tuple:
        return render_template('submit.html', value=bodytype, images=body_type_images_list, bust=bustval,
                               waist=waistval, hip=hipval, highhip=highhipval)
    else:
        return render_template('invalid.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)




