import re

file = open('dicionario_medico.txt', encoding='UTF-8')
text = file.read()

# correções necessarias no ficheiro inicial para que o formato seja:
# Designação\n
# Descrição.\n\n
text = re.sub(r'(([^\.])\n\n)\f', r'\2\n', text)
text = re.sub(r'\f', r'', text)
text = re.sub(r'(\.)\n\n([A-Z])', r'\1\n\2', text)

entries = re.findall(r'\n\n(.+)((?:\n.+)+)', text)
# print(entries)

new_entries = []

for designation, description in entries:
    description = description.strip()
    new_entries.append((designation, description))

# outra maneira de fazer a mesma coisa
new_entries = [(designation, description.strip())
               for designation, description in entries]

# print(new_entries)

file.close()

####################################################################
# criação do ficheiro html
html = open('dicionario.html', 'w', encoding='UTF-8')

header = '''<html>
                <head>
                    <meta charset="UTF-8"/>
                    <title>Dicionário Médico</title>
                    <style>
                        body {
                            background-color: #001021;
                            color: black;
                            font-family: "Helvetica", "Arial", sans-serif;
                            font-size: 1em;
                            padding: 0 10%;
                        }
                        table {
                            width: 70%;
                            margin-top: 5%;
                            background: #C5D1D5;
                        }
                        th {
                            background: #84B4C2;
                        }
                        th, td {
                            margin: 0;
                            height: auto;
                            padding: 10px;
                            border-bottom: 1px solid #1481BA;
                        }
                        tr > td:first-child, 
                        tr > th:first-child {
                            border-right: 1px solid #1481BA;
                        }
                        tr:hover{
                            background: #84B4C2;
                        }
                    </style>
                    </head>
                    <body>
                        <h1 style="color: #1481BA;">Dicionário Médico</h1>
                        <table>
                            <thead>
                                <tr>
                                    <th><h2>Designação</h2></th>
                                    <th><h2>Descrição</h2></th>
                                </tr>
                            </thead>
                            <tbody>
'''

body = ''
for designation, description in new_entries:
    body += '<tr><td><h3 style="color: #1481BA;">' + designation + '</h3></td>'
    body += '<td>' + description + '</td></tr>'

footer = '''
                        </tbody>
                    </table>
                </body>
            </html>
'''

html.write(header + body + footer)

html.close()
