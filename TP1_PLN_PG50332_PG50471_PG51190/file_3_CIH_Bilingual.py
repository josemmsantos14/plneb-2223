import re
import json

file = open('data/CIH Bilingual Medical Glossary English-Spanish.xml', encoding='UTF-8')
text = file.read()

text = re.sub(r'(<text.*\n*)*(<text.*>\d+\s<\/text>)', '', text)

#Delete every blank tags with single white space
text = re.sub(r'<text.*?>(?:\s|(<(b|i)>\s</(b|i)>))</text>', '', text)

#Delete tags <page> and <fontspec>
text = re.sub(r'(</?page.*>|</?fontspec.*>)', '', text)

#Delete final parte with Prefixes, Sufixes and Roots
text = re.sub(r'(<text.*><b>\bPREFIXES\b.*</b></?text>)(\n.*)*', '', text)

#Delete introdutory part
text = re.sub(r'(<text.*>\n*)*(\border\b\.\s</?text>)', '', text)

#Delete tags <b> and </b> 
text = re.sub(r'(<[bi]>|</[bi]>)', '', text)

text = re.sub(r'(\n+)?:', '', text)

#Get the parts inside the tags <text>
#List with the format ["TermEN","TranslationES","TermEN","TranslationES",...]
text = re.sub(r'</?text.*?>(.*?)</text>', r"\1", text)
#text = re.sub(r'\n{2,}', r'\n\n', text)

#Substituir multiplos espaços por apenas um
text = re.sub(r'([ ]{2,})', r' ', text)

#Unir expressoes em que numa linha temos parenteses de abertura e zero de fecho e este se encontra na seguinte
text = re.sub(r'(\(.[^\)]+)\n(.[^\(]*\))', r'\1\2', text)

#Encontrar casos em que as traduções se encontram separadas, ou seja, proxima linha começa por minuscula (resolver mais do que o que estragou)
text = re.sub(r'\n+([a-z])', r'\1', text)

#Junção de todo o texto seguido
text = re.sub(r'\n{2,}', '\n', text)

#Substituição de um caso especifico "Women's para mujeres"
text = re.sub(r'(\b’s\b)\s([a-z]+)', r'\1\n\2', text)
#Desformatação por causa da tabela, metade do termo aparecia depois da tradução
text = re.sub(r'(\bDpt\b.*)\n(.*)\n(.*)', r'\1\3\n\2', text)
#Separação errada depois de ";"
text = re.sub(r'(.*\/.*;\s)\n(.*)', r'\1\2', text)
#Caracter solto "´"
#CASOS ESPECIAIS
text = re.sub(r'`\s\n(.*)', r'\1', text)
text = re.sub(r'(\bAngioplasty\b)\s(.*)', r'\1\n\2', text)
text = re.sub(r'(\bInfeccion\b\s)\n(.*)', r'\1\2', text)
text = re.sub(r'(\brate\b)\s(.*)', r'\1\n\2', text)
text = re.sub(r'(\bInstruments\b)\n.', r'\1', text)
text = re.sub(r'(\()\n(.*)\n(.)', r'\1 \2 \3', text)
text = re.sub(r'\n(\(.*)\n(\(.*)', r' \1 \2', text)
text = re.sub(r'.\n(\))', r'\1', text)
text = re.sub(r'\n(\(.*\),.*)', r'\1', text)
text = re.sub(r'\n(\(.*\)\s\n)', r'\1', text)
text = re.sub(r'(\bMenstrual\b)\s(\bmenstrual\b)', r'\1\n\2', text)
text = re.sub(r'(\n.*\bNeck\b)\n\s\n.*|(\n\bTrunk\b)\n\s\n.*', '', text)
text = re.sub(r'\n\t', '', text)
text = re.sub(r'(\bHomeless\b)\s(.*)', r'\1\n\2', text)
text = re.sub(r'(¿)\n(.*)', r'\1\2', text)
text = re.sub(r'(\n\w+)\s(\barticulac.+\b)', r'\1\n\2', text)
text = re.sub(r'(\n.+)\s(n\s)', r'\1\2', text)

#Junção aos pares
text = re.sub(r'([A-Z].*\n.*\n)', r'\1\n', text)

text = re.sub(r'(<.*>)\n(<.*>)\n+<.*>', r'\n', text)

entries = re.findall(r'\n\n(.+)\n(.*)', text)

# ola = open("alterado.xml", "w" ,encoding="UTF-8")
# ola.write(text)
# ola.close()

dici = {}

#Create the dicionary entries with a for with 2 steps
for term, translation in entries:
    dici[term.strip().lower()]=translation.strip().lower()
    # print(term, " :", translation)

# print(dici)

with open('middle_output/output_1_bilingual.json', 'w', encoding='UTF-8') as output:
    json.dump(dici, output, ensure_ascii=False, indent=4)

output.close()

