from flask_wtf import FlaskForm
from wtforms import TextField, SelectField, RadioField
from wtforms.validators import InputRequired, URL


class UrlRequest(FlaskForm):
    """docstring for url_request"""

    url = TextField("Url to scrape:", validators=[InputRequired(),
            URL(message="Not valid. Please enter the entire url.")])
    file_name = TextField("Filename:", validators=[InputRequired()])
    file_extension = SelectField("File type:", choices=[('.docx', '.docx')])
    scraping_type = RadioField('Scraping option:', default='url', choices=[
            ('url', 'Just this URL'), ('internal_links', 'This URL and all internal links')])
    stop_words = TextField('Words to remove from keyword analysis:')
