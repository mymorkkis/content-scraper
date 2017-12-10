from flask_wtf import FlaskForm
from wtforms import TextField, SelectField
from wtforms.validators import InputRequired, URL


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
