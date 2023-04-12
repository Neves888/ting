def exists_word(word, instance):
    list = []
    file_text_line = instance.search(0)["linhas_do_arquivo"]
    data = {
        "palavra": word,
        "arquivo": instance.search(0)["nome_do_arquivo"],
        "ocorrencias": [
            {
                "linha": i + 1
            } for i, line in enumerate(file_text_line)
            if word.lower() in line.lower()
        ]
    }

    if data["ocorrencias"]:
        list.append(data)

    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
