from flask import Blueprint, render_template, session, redirect, request, flash

import dao.XRDao as xr_dao
import utils.util as util
from werkzeug.utils import secure_filename
from flask import current_app as app
import os
import operator
import dao.label_image as label_image

blueprint = Blueprint('xr_controller', __name__)


@blueprint.route('/', methods=['GET'])
def calendar_assigned_to_me():
    result = None
    return render_template('scan.html', result=result)


@blueprint.route('test/', methods=['POST'])
def test():
    status = 200
    result = None
    return util.to_json(status, result)


@blueprint.route('process/', methods=['POST'])
def process():
    print "I am here"
    print request.files
    f = request.files['image.jpg']
    filename = secure_filename(f.filename)
    extension = filename.split(".")
    new_name = util.get_uuid() + "." + str(extension[1])
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
    print "Done"
    file_name = os.path.join(app.config['UPLOAD_FOLDER'], new_name)
    model_file = os.path.join(app.config['UPLOAD_FOLDER'], "retrained_graph.pb")
    label_file = os.path.join(app.config['UPLOAD_FOLDER'], "retrained_labels.txt")
    prod_dict = label_image.start(file_name, model_file, label_file)
    obj = max(prod_dict.iteritems(), key=operator.itemgetter(1))[0]
    obj_prob = prod_dict[obj]
    if obj_prob > 0.95:
        result = get_facts(obj)
    else:
        result = "Sorry"
    status = 200
    return util.to_json(status, result)


def get_facts(x):
    return {
        'apple': 'Apple',
        'mango': 'Mango',
        'blue berry': 'Blue Berry'
    }.get(x, 'Sorry')
