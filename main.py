import file_receiv
from file_receiv import open_txt_file
from words_counter import word_counter, letter_counter
import creating_CSV
import os

dir_list = os.listdir('files/')

chose_file_menu = ['Choose file to analise.', 'EXIT']
menu_list = ['Print the number of letters in text', 'Print the number of words in text',
             'Save the results in CSV file', 'Choose different file', 'EXIT']
chosen_file = None

is_on = True
while is_on:

    while chosen_file == None and is_on:
        # first menu display
        for index, option in enumerate(chose_file_menu):
            print(f'{index + 1} - {option}')
        first_menu_pick = int(input('Choose your option: '))

        # exiting the loop
        if chose_file_menu[first_menu_pick - 1] == 'EXIT':
            print('Thank you for useing our software! Good bye!')
            is_on = False

        # choosing a file
        elif chose_file_menu[first_menu_pick - 1] == 'Choose file to analise.':
            for index, name in enumerate(dir_list):
                print(f'{index + 1}-{name}')
            user_file_name = int(input("Choose a file number to proceed: "))
            chosen_file = dir_list[user_file_name - 1]

            # creating file name
            file_name = chosen_file.split('.')[0]

            # generating word and letter list from .txt
            if chosen_file[-4:] == ".txt":
                text = open_txt_file(file_name)

                letter_count_dict = letter_counter(text)

                word_count_dict = word_counter(text)

            # generating word and letter list from .docx
            elif chosen_file[-5:] == '.docx':
                file_receiv.open_docx_file(chosen_file)
                text = open_txt_file(file_name)

                letter_count_dict = letter_counter(text)

                word_count_dict = word_counter(text)

                os.remove(f'files/{chosen_file[:-5]}.txt')


            elif chosen_file[-4:] == '.pdf':
                print('Sorry, we are not yet supporting PDF files!')
                chosen_file = None

    while chosen_file != None:
        print(f'"{chosen_file}" file is chosen!')
        for index, option in enumerate(menu_list):
            print(f'{index + 1} - {option}')

        user_choice = int(input('Choose the number: '))
        if menu_list[user_choice - 1] == 'EXIT':
            print('Thank you for useing our software! Good bye!')
            chosen_file = None
            is_on = False
        elif menu_list[user_choice - 1] == 'Print the number of letters in text':
            for key, value in letter_count_dict.items():
                print(f'{key} = {value}')
        elif menu_list[user_choice - 1] == 'Print the number of words in text':
            for key, value in word_count_dict.items():
                print(f'{key} = {value}')
        elif menu_list[user_choice - 1] == 'Save the results in CSV file':
            creating_CSV.creator_csv(word_count_dict, f'{file_name}_words')
            creating_CSV.creator_csv(letter_count_dict, f'{file_name}_letters')
        elif menu_list[user_choice - 1] == 'Choose different file':
            chosen_file = None
