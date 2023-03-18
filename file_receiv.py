import docx2txt
import glob



def open_txt_file():
    """Function recives .txt document, and converting in to the list of words. """
    file_name = input("Provide the file name without extension: ")
    with open(f"files/{file_name}.txt", "r") as f:
        read_file = f.read()
        return read_file




def open_docx_file():
    directory = glob.glob('C:/PycharmProjects/text_analizer/files/*.docx')

    for file_name in directory:
        with open(file_name, 'rb') as infile:
            outfile = open(file_name[:-5] + '.txt', 'w', encoding='utf-8')
            doc = docx2txt.process(infile)

            outfile.write(doc)

        outfile.close()
        infile.close()

    # print("=========")
    # print("All done!")


# open_docx_file()