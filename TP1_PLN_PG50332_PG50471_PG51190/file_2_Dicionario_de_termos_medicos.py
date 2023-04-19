import re
import json

with open('data/Dicionario_de_termos_medicos_e_de_enfermagem.xml', 'r',encoding="utf-8") as text:
    lines = text.readlines()

with open('middle_output/dicionario_simplificado.xml', 'w', encoding="utf-8") as text:
    for i, line in enumerate(lines):
        if i >= 631:
            text.write(line)

with open('middle_output/dicionario_simplificado.xml', 'r', encoding="utf-8") as file:
    text = file.read()

# view = open('ver.txt',"w", encoding="UTF-8")


def limpa(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip() 

text= re.sub(r'<text top="[0-9]+" left="[0-9]+" width="[0-9]+" height="11" font="(6|20)+">.*</text>',"",text)
text =re.sub(r'<text top="88" left="327" width="83" height="185" font="17"><i>S</i></text>',"",text)
text=re.sub(r'<text top="128" left="294" width="50" height="111" font="18"><i>S</i></text>',"",text)
text = re.sub(r"</?page.*>", "", text)
text = re.sub(r"</?text.*?>", "", text) 
text = re.sub(r"</?fontspec.*?>", "", text) 
text = re.sub(r'Sou Enfermagem - Cadastre-se grátis <a href="https://souenfermagem.com.br">em: https://souenfermagem.com.br</a>',"",text)
text = re.sub(r'<i>([ABCDEFGHIJKLMNOPQRTUVWXZ ]?)</i>',"",text)
text = re.sub(r'<i>'," ",text)
text = re.sub(r'</i>'," ",text)
text = re.sub(r'\n\s+',"\n",text)
text = re.sub(r'\n-\s', " ",text)
text = re.sub(r'-\n',"",text)
text = re.sub(r'-</b>\n<b>',"",text)
text = re.sub(r',</b>\n<b>',",",text)
text= re.sub(r'\s</b>\n<b>'," ", text)
text = re.sub(r'\(</b>\n<b>',"(",text)
text= re.sub(r'<b>(.{0,2}[a-záéíóúàèìòùâêîôûãõçñ]+.*)</b>',r'\1',text)
text = re.sub (r"\n", " ", text)
text = re.sub (r"○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ", "", text)
lista = re.findall(r"<b>(.*?)</b>([^<]*)", text) 
lista = [[designacao.lower(), limpa(descricao)] for designacao, descricao in lista]

dicionario = dict(lista) 
# view.write(text)

out = open ("middle_output/output_1_dicionario_medico_enfermagem.json", "w", encoding="utf-8")
json.dump(dicionario, out, ensure_ascii=False, indent=4)
out.close()
