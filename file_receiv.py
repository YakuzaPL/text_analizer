def open_txt_file():
    """Function recives .txt document, and converting in to the list of words. """
    file_name = input("Provide the file name without extension: ")
    with open(f"files/{file_name}.txt", "r") as f:
        read_file = f.read()
        return read_file





