import sys


def txt_importer(path_file):
    try:
        if path_file.endswith(".txt"):
            with open(path_file, "r") as file:
                file = [word.replace("\n", "") for word in file.readlines()]
                return file
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        sys.stderr.write("Formato inválido")
