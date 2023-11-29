import csv

# Nome do arquivo CSV de entrada
arquivo_csv = 'arquivo.csv'

# Nome do arquivo TXT com as palavras corrigidas
arquivo_txt_corrigido = 'palavras_corrigidas.txt'

# Nome do arquivo CSV de saída
arquivo_csv_corrigido = 'arquivo_corrigido.csv'

# Dicionário para armazenar as correções
correcoes = {}

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

# Leitura do arquivo TXT com as palavras corrigidas
with open(arquivo_txt_corrigido, 'r', encoding='utf-8') as txt_file:
    for linha in txt_file:
        # Divide a linha e remove espaços em branco
        partes = linha.strip().split(',')
        correcoes[partes[0]] = partes[1]

# Lista para armazenar as linhas corrigidas
linhas_corrigidas = []

# Função para aplicar correções nas palavras
def corrigir_palavra(palavra):
    return correcoes.get(palavra, palavra)

# Leitura do arquivo CSV de entrada
with open(arquivo_csv, 'r', encoding='utf-8') as csv_file:
    leitor_csv = csv.DictReader(csv_file)

    # Processa cada linha do CSV
    for linha in leitor_csv:
        linha_corrigida = {
            'id': linha['id'],
            'texto': ' '.join([corrigir_palavra(palavra) for palavra in linha['texto'].split()])
        }
        linhas_corrigidas.append(linha_corrigida)

# Escreve as linhas corrigidas no arquivo CSV de saída
with open(arquivo_csv_corrigido, 'w', encoding='utf-8', newline='') as csv_file:
    campos = ['id', 'texto']
    escritor_csv = csv.DictWriter(csv_file, fieldnames=campos)

    # Escreve o cabeçalho
    escritor_csv.writeheader()

    # Escreve as linhas corrigidas
    for linha_corrigida in linhas_corrigidas:
        escritor_csv.writerow(linha_corrigida)

print(f'Arquivo CSV corrigido salvo em {arquivo_csv_corrigido}.')
