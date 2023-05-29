from words_counter import TextAnalizer
import creating_CSV
import os


if __name__ == '__main__':
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


                # creating file name and file path
                file_name = chosen_file.split('.')[0]
                file_path = f'files/{chosen_file}'

                text_for_analize = TextAnalizer(file_path)


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
                for key, value in text_for_analize.letter_count().items():
                    print(f'{key} = {value}')
            elif menu_list[user_choice - 1] == 'Print the number of words in text':
                for key, value in text_for_analize.word_count().items():
                    print(f'{key} = {value}')
            elif menu_list[user_choice - 1] == 'Save the results in CSV file':
                creating_CSV.creator_csv(text_for_analize.word_count(), f'{file_name}_words')
                creating_CSV.creator_csv(text_for_analize.letter_count(), f'{file_name}_letters')
            elif menu_list[user_choice - 1] == 'Choose different file':
                chosen_file = None


