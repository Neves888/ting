from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return None
    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
        }
    file_out = sys.stdout
    instance.enqueue(data)
    print(data, file=file_out)


def remove(instance):
    if not len(instance):
        print('Não há elementos', file=sys.stdout)
    else:
        file = instance.dequeue()
        file_out = sys.stdout
        print(
            f'Arquivo {file["nome_do_arquivo"]} removido com sucesso',
            file=file_out

        )


def file_metadata(instance, position):
    try:
        doc = instance.search(position)
        file_out = sys.stdout
        print(doc, file=file_out)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
