from flask import Flask, render_template, redirect
from models.forms import UrlRequest
from data.processing import process_data


app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UrlRequest()
    if form.validate_on_submit():
        process_data(form)
        return redirect('processing')
    return render_template('form.html', form=form)


@app.route('/processing')
def processing():
    return render_template('processing.html')


# TODO add some styling
@app.errorhandler(404)
def page_not_found(error):
    return "This page can't be found. Is the url correct?", 404


if __name__ == '__main__':
    app.run()
