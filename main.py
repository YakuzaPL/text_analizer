import file_receiv

from file_receiv import open_txt_file
from words_counter import text_to_words, words_or_letters_dict_creator, text_to_letters
import creating_CSV
import os


dir_list = os.listdir('files/')
chose_file_menu = ['Choose file to analise.', 'EXIT']
menu_list = ['Print the number of letters in text', 'Print the number of words in text',
             'Save the results in CSV file', 'EXIT']
chosen_file = None

is_on = True
while is_on:


    while chosen_file == None:
        for index, option in enumerate(chose_file_menu):
            print(f'{index + 1} - {option}')
        first_menu_pick = int(input('Choose your option: '))

        if chose_file_menu[first_menu_pick - 1] == 'Choose file to analise.':
            file_list = []
            # for direction in dir_list:
            #     file_list.append(direction.split('.')[0])
            for index, name in enumerate(dir_list):
                print(f'{index + 1}-{name}')
            user_file_name = int(input("Choose a file number to proceed: "))
            chosen_file = dir_list[user_file_name - 1]

            file_name = chosen_file.split('.')[0]
            file_extention = chosen_file.split('.')[-1]

            if file_extention == 'docx':
                file_receiv.open_docx_file()
            text = open_txt_file(file_name)

        elif menu_list[first_menu_pick -1] == 'EXIT':
            print('Thank you for useing our software! Good bye!')
            is_on = False

    print(f'"{file_name}" file is chosen!')
    for index, option in enumerate(menu_list):
        print(f'{index + 1 } - {option}')

    user_choice = int(input('Choose the number: '))
    if menu_list[user_choice-1] == 'EXIT':
        print('Thank you for useing our software! Good bye!')
        is_on = False
    elif menu_list[user_choice-1] == 'Print the number of letters in text':
        letter_list = text_to_letters(text)
        letter_count_dict = words_or_letters_dict_creator(letter_list)
        for key, value in letter_count_dict.items():
            print(f'{key} = {value}')
        continue_chooice = input('Continue? [Y/N]')
        if continue_chooice.lower() == 'n':
            print('Thank you!')
            is_on = False
    elif menu_list[user_choice - 1] == 'Print the number of words in text':
        word_list = text_to_words(text)
        word_count_dict = words_or_letters_dict_creator(word_list)
        for key, value in word_count_dict.items():
            print(f'{key} = {value}')
        continue_chooice = input('Continue? [Y/N]')
        if continue_chooice.lower() == 'n':
            print('Thank you!')
            is_on = False
    elif menu_list[user_choice - 1] == 'Save the results in CSV file':
        creating_CSV.creator_csv(word_count_dict,f'{file_name}_words')
        creating_CSV.creator_csv(letter_count_dict, f'{file_name}_letters')
        continue_chooice = input('Continue? [Y/N]')
        if continue_chooice.lower() == 'n':
            print('Thank you!')
            is_on = False
