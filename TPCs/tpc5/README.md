Este trabalho consistia na passagem do ficheiro termos_traduzidos.txt, contendo termos em português com a respetiva tradução, para o formato json tendo em vista o resultado:
“termo em português”: “en: termo em inglês”

O ficheiro inicial foi processado, e através da expressão regular (\w+)\s@\s(\w+) foi possível alcançar o termo em português e a sua tradução em cada grupo de captura.

Estes valores permitiram a formação de um dicionário com o acréscimo do identificador da respetiva língua da tradução “en”. Desta forma, os valores de cada dicionário obtiveram o formato “en: {translation}”.

Após concebido o dicionário, este foi escrito num ficheiro com formato json.
