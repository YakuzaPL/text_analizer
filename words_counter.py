from collections import Counter
import re
import string


# counts the words frequency and returns it as a dict
def word_counter(text):
    word_count = Counter(re.findall('\w+', text.lower()))
    return dict(word_count)

def letter_counter(text):
    # Removing whitespace and punctuation marks
    text = text.translate(str.maketrans('', '', string.whitespace + string.punctuation))

    # Converting text to lowercase
    text = text.lower()

    # Counting the frequency of each letter
    letter_count = Counter(text)

    return dict(letter_count)


