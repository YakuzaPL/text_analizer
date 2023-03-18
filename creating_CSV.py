import csv

def creator_csv(file_name, data_dict):
    with open(f'{file_name}.csv', 'w') as f:
        for key in data_dict.keys():
            f.write("%s, %s\n" % (key, data_dict[key]))

