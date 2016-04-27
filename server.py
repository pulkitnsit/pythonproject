import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = './uploads'
COMPRESSION_FOLDER = './compressed'
ALLOWED_EXTENSIONS = set(['wav'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['COMPRESSION_FOLDER'] = COMPRESSION_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def hello():
    filename = None
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('index.html', uploaded=filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/oversample', methods=['GET', 'POST'])
def oversample_main():
    if request.method == 'POST':
        name = request.form['s1text']
        upfile = os.path.join(app.config['UPLOAD_FOLDER'], name)
        print upfile
    return redirect(url_for('hello'))

@app.route('/undersample', methods=['GET', 'POST'])
def undersample_main():
    if request.method == 'POST':
        name = request.form['stext']
        upfile = os.path.join(app.config['UPLOAD_FOLDER'], name)
        print upfile
    return redirect(url_for('hello'))

@app.route('/lowpass', methods=['GET', 'POST'])
def lpf_main():
    if request.method == 'POST':
        name = request.form['s2text']
        upfile = os.path.join(app.config['UPLOAD_FOLDER'], name)
        print upfile
    return redirect(url_for('hello'))

@app.route('/bandpass', methods=['GET', 'POST'])
def bpf_main():
    if request.method == 'POST':
        name = request.form['s3text']
        upfile = os.path.join(app.config['UPLOAD_FOLDER'], name)
        print upfile
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run()
