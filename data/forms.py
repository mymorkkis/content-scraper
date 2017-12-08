from flask_wtf import FlaskForm
from wtforms import TextField, SelectField, RadioField
from wtforms.validators import InputRequired, URL


class UrlRequest(FlaskForm):
    """TODO"""

    url = TextField("Url to scrape:", validators=[InputRequired(),
            URL(message="Not valid. Please enter the entire url.")])
    filename = TextField("Filename:", validators=[InputRequired()])
    # TODO add functionality to save as different file types
    file_extension = SelectField("File type:", choices=[('.docx', '.docx')])
    scraping_type = RadioField('Scraping option:', default='url', choices=[
            ('url', 'Just this URL'), ('internal_links', 'This URL and all internal links')])
    stop_words = TextField('Words to remove from keyword analysis:')
