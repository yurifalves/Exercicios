import os

customizar = {
    'RED': '\033[1;31m', 'BLUE': '\033[1;34m', 'CYAN': '\033[1;36m', 'GREEN': '\033[0;32m',
    'BOLD': '\033[;1m', 'REVERSE': '\033[;7m', 'RESET': '\033[0m'
}


def pasta_tamanho(caminho):
    """
    :param caminho: caminho da pasta a ser pesquisada
    :return: retorna informações sobre o tamanho de uma pasta
    """
    os.chdir(caminho)
    cont_num_diretorios = cont_num_arquivos = tamanho_total = 0
    for t in os.listdir(caminho):
        if os.path.isdir(t):
            cont_num_diretorios += 1
        else:
            cont_num_arquivos += 1
        tamanho_total += os.path.getsize(t)
    print('-=' * 60)
    print(f'{customizar["BLUE"]}Caminho Fornecido: "{caminho}"{customizar["RESET"]} ({tamanho_total:.2f}B, {tamanho_total / 1048576:.2f}MB, {tamanho_total / 1073741824:.2f}GB)', end='\n\n')
    print(f'{customizar["BOLD"]}{customizar["RED"]}{cont_num_diretorios} PASTAS{customizar["RESET"]}')

    for z in os.listdir(caminho):
        if os.path.isdir(z):
            print(
                fr'-{z}, ({os.path.getsize(z):.2f}B, {os.path.getsize(z) / 1048576:.2f}MB, {os.path.getsize(z) / 1073741824:.2f}GB)')
        else:
            pass

    print(f'{customizar["BOLD"]}{customizar["RED"]}{cont_num_arquivos} ARQUIVOS{customizar["RESET"]}')
    for z in os.listdir(caminho):
        if os.path.isfile(z):
            print(
                fr'-{z}, ({os.path.getsize(z):.2f}B, {os.path.getsize(z) / 1048576:.2f}MB, {os.path.getsize(z) / 1073741824:.2f}GB)')
        else:
            pass
