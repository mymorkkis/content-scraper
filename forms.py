from flask_wtf import FlaskForm
from wtforms import TextField, SelectField
from wtforms.validators import InputRequired, URL
from document import docx


class UrlRequest(FlaskForm):
    """Home page URL request form"""

    url = TextField(
        "Url to scrape:",
        validators=[
            InputRequired(),
            URL(message="Not valid. Please enter the entire url.")
        ])
    filename = TextField("Filename:", validators=[InputRequired()])
    # TODO add functionality to save as different file types
    file_extension = SelectField("File type:", choices=[('.docx', '.docx')])
    stop_words = TextField('Words to remove from keyword analysis:')


def process_data(form):
    url = form.url.data
    filename = form.filename.data + form.file_extension.data
    # stop_words = [word for word in form.stop_words.data.split(' ')]

    # TODO add functionality to create differnt document types (.odt, .pages etc)
    docx.create_document(filename, url)
