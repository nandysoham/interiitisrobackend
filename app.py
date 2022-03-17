from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

from model import returnable
import json

app = Flask(__name__)
CORS(app)


@app.route("/", methods = ['POST', 'GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/upload", methods = ['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        # f.save(secure_filename(f.filename))
        f.save("icdata.ic")
        returndata = returnable()
        print(type(returndata))
        returnjsondata = json.dumps(returndata)
        print(type(returnjsondata))
        return returnjsondata
        return 'file uploaded successfully'


if __name__ == "__main__":
    app.run(debug= True)
