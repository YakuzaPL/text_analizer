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
    list_of_letters = re.split(r'\W*', text)
    for element in list_of_letters:
        if element == '':
            list_of_letters.remove('')
    if '' in list_of_letters:
        list_of_letters.remove('')

    return list_of_letters


def words_or_letters_counter(word_or_letter_list):
    counted_words_or_letters = {}
    for word in word_or_letter_list:
        word = word.lower()
        if word in counted_words_or_letters.keys():
            counted_words_or_letters[word] = counted_words_or_letters[word] + 1
        else:
            counted_words_or_letters[word] = 1

    return counted_words_or_letters


