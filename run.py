from flask import Flask

import controller.XRController as xrController

# creating flask object
app = Flask(__name__, static_url_path="/static", static_folder="static")

# set the secret key.  keep this really secret:
app.secret_key = 'XR_SECRET_KEY'
app.config['UPLOAD_FOLDER'] = "/Users/saksekar/Downloads/"
app.config['TEMP_FOLDER'] = "/Users/saksekar/Downloads/"
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024 # 100MB


# registering blueprint objects to flask
app.register_blueprint(xrController.blueprint, url_prefix='/')

if __name__ == '__main__':
    #app.run(port=7000,host='192.168.0.101')
    app.run(port=7000, host='192.168.122.238')
