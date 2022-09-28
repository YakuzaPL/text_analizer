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

text_1 = "Lorem ipsum dolor sit amet."
text_2 = "Test, test, kolejny, dla potrzeb, tej funkcji."
text_3 = "Some some, exaple teXt, given. Here, just, for fun"

list_1 = text_splitter(text_1)
list_2 = text_splitter(text_2)
list_3 = text_splitter(text_3)
print(list_3)

words_1 = words_counter(list_1)
words_2 = words_counter(list_2)
words_3 = words_counter(list_3)

print(words_1)
print(words_2)
print(words_3)