import re
import json

"""
Template
----------------
termoPT:
        ES:
        EN:
        Def:

"""

f1 = open("middle_output/output_1_dicionario_termos_medicos.json", encoding="utf-8")
d1 = json.load(f1)

f2 = open("middle_output/output_1_dicionario_medico_enfermagem.json", encoding="UTF-8")
d2 = json.load(f2)

f3 = open("middle_output/output_2_CIH_RU5H.json", encoding="UTF-8")
d3 = json.load(f3)

dici = {}


d1.update(d3)

# print(d1)

# with open('middle_output/last.json', 'w', encoding='UTF-8') as output:
#     json.dump(d1, output, ensure_ascii=False, indent=4)

# output.close()

final_dici = {}
for term, translations in d1.items():
    if d2.get(term)!= None:
        final_dici[term] = {
                                "trad": translations,
                                "desc" : d2.get(term, "Desc. not found.")
                                }
        
with open('final_output/final_dici.json', 'w', encoding='UTF-8') as output:
    json.dump(final_dici, output, ensure_ascii=False, indent=4)

output.close()