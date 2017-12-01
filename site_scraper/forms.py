from flask_wtf import FlaskForm
from wtforms import TextField, SelectField
from wtforms.validators import InputRequired


class UrlRequest(FlaskForm):
    """docstring for url_request"""

    url = TextField("Url to scrape:", validators=[InputRequired()])
    file_name = TextField("Filename:", validators=[InputRequired()])
    file_extension = SelectField("File type:", choices=[('.docx', '.docx')])
    stop_words = TextField('Words to remove from keyword analysis:')
