
def words_counter(text):
    counted_words = {}
    # ToDo find the way to get read of the dots and commas
    splited_text = text.split()
    words_list = [word.lower() for word in splited_text]

    for word in words_list:
        if word in counted_words.keys():
            counted_words[word] = counted_words[word] + 1
        else:
            counted_words[word] = 1

    return counted_words

print(words_counter("This this, is is a test test file, For for my ProGram"))