import os

from flask import Flask, render_template, send_file
from forms import UrlRequest

from document.processing import process_form_data


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UrlRequest()
    if form.validate_on_submit():
        process_form_data(form)
        filename = form.filename.data + form.file_extension.data
        return render_template('processing.html', filename=filename)
    return render_template('form.html', form=form)


@app.route('/download/<filename>')
def download(filename):
    file_path = f'/tmp/{filename}'
    return send_file(file_path)


if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    app.run()
