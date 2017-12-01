from flask import Flask, request, render_template, redirect, url_for, flash
from forms import UrlRequest

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test1test2'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UrlRequest()

    if form.validate_on_submit():
        return f'{form.url.data} - {form.file_name.data} - {form.file_extension.data}'
    return render_template('form.html', form=form)


@app.route('/processing')
def processing():
    return "<h1>Success</h1>"

# TODO error handling http 404

# if __name__ == '__main__':
#     app.run(debug=True)
