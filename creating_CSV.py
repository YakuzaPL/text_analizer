import csv

def creator_csv(data_dict):
    with open('resul_file.csv', 'w') as f:
        for key in data_dict.keys():
            f.write("%s, %s\n" % (key, data_dict[key]))

