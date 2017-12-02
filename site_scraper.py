from flask import Flask, render_template, redirect
from site_scraper.forms import UrlRequest


app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UrlRequest()

    if form.validate_on_submit():
        # return f'{form.url.data} - {form.file_name.data} - {form.file_extension.data}'
        return redirect('processing')
    return render_template('form.html', form=form)


@app.route('/processing')
def processing():
    return render_template('processing.html')


# TODO add some styling
@app.errorhandler(404)
def page_not_found(error):
    return 'This page can not be found. Is the url correct?', 404


if __name__ == '__main__':
    app.run()
