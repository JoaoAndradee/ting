import sys
from ting_file_management.file_management import txt_importer

processed_files = set()


def process(path_file, instance):
    for path in range(len(instance)):
        file = instance.search(path)
        if path_file == file["nome_do_arquivo"]:
            return

    lines = txt_importer(path_file)

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    instance.enqueue(file_data)

    print(file_data)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        removed = instance.dequeue()
        print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        sys.stderr.write("Posição inválida\n")
    else:
        file_info = instance.search(position)
        print(file_info)
