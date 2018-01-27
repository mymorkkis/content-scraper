"""Forms for app. UrlRequestForm: Home page URL request form."""
from flask_wtf import FlaskForm
from wtforms import TextField, SelectField
from wtforms.validators import InputRequired, URL, Regexp


class UrlRequest(FlaskForm):
    """Home page URL request form"""
    url = TextField(
        "Url to scrape:",
        validators=[
            InputRequired(),
            URL(message="Not valid. Please enter the entire url.")
        ],
        description='Enter full URL: https://example.com')
    filename = TextField(
        "Filename:",
        validators=[
            InputRequired(),
            Regexp(
                r'^[a-z|A-Z][\w| ]+$',
                message="Filename must start with a letter and can't include \
                            any special characters except underscores.")
        ],
        description="Enter the filename you wish the document to be saved as.")
    # TODO add functionality to save as different file types
    file_extension = SelectField("File type:", choices=[('.docx', '.docx')])
    stop_words = TextField(
        'Words to remove from keyword analysis:',
        description='Enter words separated by space or comma. \
                     Leave blank if no extra words required.')
