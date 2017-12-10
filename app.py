from flask import Flask, render_template
from forms import UrlRequest
from document.doc_path import set_path
from document.processing import process_form_data


app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UrlRequest()
    if form.validate_on_submit():
        process_form_data(form)
        filename = form.filename.data + form.file_extension.data
        file_path = set_path(filename)
        return render_template('processing.html', file_path=file_path)
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()
