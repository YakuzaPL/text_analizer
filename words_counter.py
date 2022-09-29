import re
def text_to_words(text):
    list_of_words = re.split(r'\W+', text)
    for element in list_of_words:
        if element == '':
            list_of_words.remove('')
    if '' in list_of_words:
        list_of_words.remove('')
    return list_of_words


def text_to_letters(text):
    list_of_words = re.split(r'\W*', text)
    for element in list_of_words:
        if element == '':
            list_of_words.remove('')
    if '' in list_of_words:
        list_of_words.remove('')

    return list_of_words


def words_or_letters_counter(words_list):
    counted_words = {}

    for word in words_list:
        if word.lower() in counted_words.keys():
            counted_words[word.lower()] = counted_words[word.lower()] + 1
        else:
            counted_words[word.lower()] = 1

    return counted_words

