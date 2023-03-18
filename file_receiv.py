import re
def open_txt_file():
    """Function recives .txt document, and converting in to the list of words. """
    file_name = input("Provide the file name without extension: ")
    with open(f"files/{file_name}.txt", "r") as f:
        read_file = f.read()
        return read_file





# print(open_txt_file("test_file_txt"))


# import docx2txt
#
# # replace "filename.docx" with the name of your Word document
# text = docx2txt.process("filename.docx")
#
# # replace "output.txt" with the name of the file you want to save the text to
# with open("output.txt", "w") as text_file:
#     text_file.write(text)