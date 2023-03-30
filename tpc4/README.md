Com recurso ao trabalho realizado anteriormente, era pretendida a união do ficheiro dicionario_medico.json (conteúdo anteriormente manipulado em formato .txt) e o ficheiro LIVRO-Doenças-do-Aparelho-Digestivo.txt.

O resultado pretendido é um ficheiro HTML em que seja apresentado o segundo ficheiro, contudo cada designação do dicionário presente no livro deveria ser uma anchor tag para que assim que intersetada pelo cursor apresenta-se um balão de informação com a respetiva descrição (significado).

Para a construção correta do texto presente no livro, fez-se a leitura de ambos os documentos e procura através do módulo re.findall() de designações que estivessem contidas no texto, assim que encontradas eram rodeadas por uma anchor tag com a respetiva descrição como valor do parâmetro “title”, ou seja, no formato:
<a href=# title={description}>{designation}</a>

Tal como realizado no trabalho anterior, a contrução do ficheiro HTML é feita tendo em conta três partes, o header, o body e o footer, sendo que no body está compreendido o texto do livro processado totalmente. Após a junção das 3 partes procede-se à escrita do ficheiro HTML.
