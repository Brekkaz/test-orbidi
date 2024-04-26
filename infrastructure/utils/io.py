def read_file(path: str) -> str:
    fd = open(path, 'r')
    file_text = fd.read()
    fd.close()

    return file_text
