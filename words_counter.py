import re
def text_splitter(text):
    list_of_words = re.split(r'\W+', text)
    if '' in list_of_words:
        list_of_words.remove('')
    return list_of_words

def words_counter(words_list):
    counted_words = {}

    for word in words_list:
        if word.lower() in counted_words.keys():
            counted_words[word.lower()] = counted_words[word.lower()] + 1
        else:
            counted_words[word.lower()] = 1

    return counted_words

