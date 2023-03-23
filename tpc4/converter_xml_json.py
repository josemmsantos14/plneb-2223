import re
import json

# abrir o ficheiro xml e trabalhar com ele com o mesmo objetivo da aula passada
file = open('dicionario_medico.xml', encoding='UTF-8')
text = file.read()

# 1º - remover <page...> e </page>, que equivale a remover \f quando trabalhamos com o ficheiro de texto
text = re.sub(r'</?page.*>', '', text)
# 2º - remover <text...> e </text>, para limpar ainda mais o ficheiro
# é necessário tirar o greedy (guloso) da expressão anterior, de modo a não remover os <b></b> e, com isso, as designações
# text = re.sub(r'<text.*?>(.*)</text>', r'\1', text) é uma solução, mas não precisa de ser tão complicada
text = re.sub(r'</?text.*?>', '', text)

# 3ª - procurar os nossos tuplos definindo grupos de captura
# entries = re.findall(r'<b>(.*)</b>(\n.+\.)', text) -> desta forma não apanha mais que 1 linha de descrição, nem apanha descrições sem ponto final
# desta forma apanha tudo o que esteja depois da designação, até apanhar o próximo <, que significa que começa um <b>
entries = re.findall(r'<b>(.*)</b>([^<]*)', text)


# em baixo: função para limpar o texto, nomeadamente substituir todos os tipos de espaços (" ", \n, etc) por um só espacinho


def limpa(text):
    text = re.sub(r'\\s+', r'\\s', text)
    return text.strip()  # já agora, a função retorna o texto que recebe também sem os \n no início e no fim; caso não se fizesse isso, ia substituir os \n no início e no fim da descrição por um espaço


# criação da lista em compreensão com a descrição já limpa de todas as formas possíveis
new_entries = [(designation, limpa(description))
               for designation, description in entries]


# passagem de lista de tuples para dicionário para ser melhor de trabalhar em json
dicionario = dict(new_entries)
# dicionario.items para voltar a ficar uma lista de tuples
# print(new_entries)


# SAVE DATA
# criação de um ficheiro json
# file = open('filename.json')

# para ler um ficheiro json
# terms = json.load(file)

# para escrever num ficheiro json: dump pede 2 argumentos, o que queremos escrever e onde queremos escrever
# json.dump(terms, file)


# criação de ficheiro json com as nossas entries
out = open('dicionario_medico.json', 'w', encoding='UTF-8')

# argumento ensure_ascii: para aceitar todos os carateres, acentuados etc
# argumento indent: para organizar melhor o output
json.dump(dicionario, out, ensure_ascii=False, indent=4)

out.close()
