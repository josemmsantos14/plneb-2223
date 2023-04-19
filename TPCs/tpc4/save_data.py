import json
import re

# abertura do ficheiro json criado em dicionario_xml.py
file = open('dicionario_medico.json', encoding='UTF-8')

# para ler um ficheiro json
entries = json.load(file)
# print(entries)
# print(entries.items())


# FICHEIRO A TRABALHAR
fileB = open('LIVRO-Doenças-do-Aparelho-Digestivo.txt', encoding='UTF-8')
text = fileB.read()
# print(text)

text = re.sub(r'\f', '<hr>', text)
text = re.sub(r'\n', '<br>', text)

print("in loop...")
for designation,description in entries.items():
    matches = re.findall(designation, text, re.I)
    matches = [*set(matches)]
    for match in matches:
        text = text.replace(match, f'<a href=# title="definition">{match}</a>')
print("out loop...")

file.close()
fileB.close()

####################################################################
# criação do ficheiro html
html = open('AparelhoDigestivo.html', 'w', encoding='UTF-8')

header = '''<html>
                <head>
                    <meta charset="UTF-8"/>
                    <title>Aparelho Digestivo</title>
                    <style>
                        a{
                            color: red;
                        }
                    </style>
                    </head>
                    <body>
'''

body = text
# body = ''
# for designation, description in new_entries:
#     body += '<tr><td><h3 style="color: #1481BA;">' + designation + '</h3></td>'
#     body += '<td>' + description + '</td></tr>'

footer = '''
                </body>
            </html>
'''

html.write(header + body + footer)

html.close()
