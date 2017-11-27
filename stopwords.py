from stop_words import get_stop_words

# Pre-existing list of stop words. Full list found at:
# https://github.com/Alir3z4/stop-words/blob/0e438af98a88812ccc245cf31f93644709e70370/english.txt
stop_words = get_stop_words('english')

# Insert extra words to ignore here
extra_words = [
    '',
    '&'
]

stop_words.extend(extra_words)
