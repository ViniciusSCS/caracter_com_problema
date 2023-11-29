import csv

# Nome do arquivo CSV de entrada
arquivo_csv = 'arquivo.csv'

# Nome do arquivo TXT de saída
arquivo_txt = 'palavras_com_problema.txt'

# Lista para armazenar as palavras com problemas
palavras_com_problema = []

# Função para verificar se a palavra contém os caracteres ☺☺
def contem_problema(palavra):
    return '☺☺' in palavra

# Leitura do arquivo CSV
with open(arquivo_csv, 'r', encoding='utf-8') as csv_file:
    leitor_csv = csv.DictReader(csv_file)
    
    for linha in leitor_csv:
        # Divide a linha em palavras
        palavras = linha['texto'].split()
        
        # Verifica cada palavra
        for palavra in palavras:
            if contem_problema(palavra):
                # Adiciona a palavra à lista
                palavras_com_problema.append(palavra)

# Escreve as palavras com problema no arquivo TXT
with open(arquivo_txt, 'w', encoding='utf-8') as txt_file:
    for palavra in palavras_com_problema:
        txt_file.write(palavra + '\n')

print(f'Palavras com problema foram salvas em {arquivo_txt}.')
