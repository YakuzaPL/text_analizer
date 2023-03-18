import file_receiv
from directiory_list import giving_directory_list_of_files_folder
from file_receiv import open_txt_file
from words_counter import text_to_words, words_or_letters_dict_creator, text_to_letters
import creating_CSV
import os

dir_list = os.listdir('files/')

for directory in dir_list:
    if directory.split('.')[1] == "docx":
        file_receiv.open_docx_file()
        print("docx converted!")


text = open_txt_file()

#creating words count csv
word_list = text_to_words(text)
word_count_dict = words_or_letters_dict_creator(word_list)
creating_CSV.creator_csv(word_count_dict)

#creating letters count csv
letter_list = text_to_letters(text)
letter_count_dict = words_or_letters_dict_creator(letter_list)
creating_CSV.creator_csv(letter_count_dict)