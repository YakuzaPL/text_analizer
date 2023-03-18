from file_receiv import open_txt_file
from words_counter import text_to_words, words_or_letters_counter, text_to_letters
import creating_CSV



text = open_txt_file("lorem")

word_list = text_to_words(text)
letter_list = text_to_letters(text)

word_count = words_or_letters_counter(word_list)
letter_count = words_or_letters_counter(letter_list)

creating_CSV.creator_csv('words', word_count)
creating_CSV.creator_csv('letters', letter_count)