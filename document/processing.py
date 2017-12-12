import re
from stop_words import get_stop_words
from document import docx

# Pre-existing list of stop words. Full list found at:
# https://github.com/Alir3z4/stop-words/blob/0e438af98a88812ccc245cf31f93644709e70370/english.txt
stop_words = get_stop_words('english')
stop_words.extend(['', '&'])


def process_form_data(form):
    url = form.url.data
    filename = form.filename.data + form.file_extension.data
    added_words = re.findall("[a-z|A-Z|.|']+", form.stop_words.data)
    stop_words.extend(added_words)

    # TODO add functionality to create differnt document types (.odt, .pages etc)
    docx.create_document(filename, url, stop_words)
