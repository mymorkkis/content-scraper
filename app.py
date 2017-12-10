from flask import Flask, render_template
from forms import UrlRequest, process_data
from document.doc_path import set_path


app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UrlRequest()
    if form.validate_on_submit():
        process_data(form)
        filename = form.filename.data + form.file_extension.data
        file_path = set_path(filename)
        return render_template('processing.html', file_path=file_path)
    return render_template('form.html', form=form)


# TODO add some styling
# @app.errorhandler(404)
# def page_not_found(error):
#     return "This page can't be found. Is the url correct?", 404


if __name__ == '__main__':
    app.run()
