def exists_word(word, instance):
    result = []

    for file_info in instance.queue:
        file_occurrences = []
        line_number = 0

        for line_content in file_info['linhas_do_arquivo']:
            line_number += 1

            if word.lower() in line_content.lower():
                file_occurrences.append({'linha': line_number})

        if file_occurrences:
            result.append({
                'palavra': word,
                'arquivo': file_info['nome_do_arquivo'],
                'ocorrencias': file_occurrences
            })

    return result



def search_by_word(word, instance):
    """Aqui irá sua implementação"""
