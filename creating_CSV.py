
import datetime


def creator_csv(data_dict):
    file_name = input("Name your resulting file: ")
    todays_date = datetime.date.today()
    with open(f'Output_files/{todays_date}-{file_name}.csv', 'w') as f:
        for key in data_dict.keys():
            f.write("%s, %s\n" % (key, data_dict[key]))

    print("File created!")


