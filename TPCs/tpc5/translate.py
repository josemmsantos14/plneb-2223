import re
import json

file = open("termos_traduzidos.txt", encoding="UTF8")
text = file.read()

dictionary = {}

for line in text.split('\n'):
    match = re.match(r'(\w+)\s@\s(\w+)', line)
    if match:
        #separação do termo da respetiva tradução
        term, translation = match.groups()
        #adição do conjunto como entrada no dicionário
        dictionary[term] = f"en: {translation}"

file.close()

with open('termos_traduzidos.json', 'w', encoding='UTF-8') as output:
    json.dump(dictionary, output, ensure_ascii=False, indent=4)

output.close()
