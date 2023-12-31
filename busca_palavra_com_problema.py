import csv

# Nome do arquivo CSV
arquivo_csv = 'arquivo.csv'

arquivo_csv_corrigido = 'arquivo_corrigido.csv'

# Nome do arquivo TXT de saída
arquivo_txt = 'palavras_com_problema.txt'

# Lista para armazenar as linhas corrigidas
linhas_corrigidas = []

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

# Função para substituir os caracteres ☺☺ por caracteres corretos
def corrigir_caracteres(palavra):
    return palavra.replace('Aten☺☺o', 'Atenção').replace('Qu☺☺mica', 'Química').replace('Ci☺☺ncia', 'Ciência').replace('incr☺☺vel', 'incrível')

# Leitura do arquivo CSV
with open(arquivo_csv, 'r', encoding='utf-8') as csv_file:
    leitor_csv = csv.DictReader(csv_file)
    
    # Processa cada linha do CSV
    for linha in leitor_csv:
        linha_corrigida = {
            'id': linha['id'],
            'texto': corrigir_caracteres(linha['texto'])
        }
        linhas_corrigidas.append(linha_corrigida)

# Escreve as linhas corrigidas no mesmo arquivo CSV
with open(arquivo_csv_corrigido, 'w', encoding='utf-8', newline='') as csv_file:
    campos = ['id', 'texto']
    escritor_csv = csv.DictWriter(csv_file, fieldnames=campos)

    # Escreve o cabeçalho
    escritor_csv.writeheader()

    # Escreve as linhas corrigidas
    for linha_corrigida in linhas_corrigidas:
        escritor_csv.writerow(linha_corrigida)

print(f'Caracteres corrigidos no arquivo CSV: {arquivo_csv_corrigido}.')
