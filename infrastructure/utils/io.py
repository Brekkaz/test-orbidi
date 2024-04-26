def read_file(path: str) -> str:
    """
    Obtiene el contenido de un archivo local
    Args:
    path: ruta absoluta del archivo a consultar.
    """
    fd = open(path, "r")
    file_text = fd.read()
    fd.close()

    return file_text
