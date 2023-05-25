import docx2txt
import glob
import PyPDF2


def open_txt_file(file_name):
    """Function recives .txt document, and converting in to the list of words. """
    with open(f"files/{file_name}.txt", "r") as f:
        read_file = f.read()
        return read_file


def open_docx_file(file_name):
    directory = glob.glob(f'C:/PycharmProjects/text_analizer/files/{file_name}')

    for file_name in directory:
        with open(file_name, 'rb') as infile:
            outfile = open(file_name[:-5] + '.txt', 'w', encoding='utf-8')
            doc = docx2txt.process(infile)

            outfile.write(doc)

        outfile.close()
        infile.close()
