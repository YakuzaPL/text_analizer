
def open_txt_file(file_name: str):
    with open(f"files/{file_name}.txt", "r") as f:
        read_file = f.read()
        return read_file





# print(open_txt_file("test_file_txt"))
