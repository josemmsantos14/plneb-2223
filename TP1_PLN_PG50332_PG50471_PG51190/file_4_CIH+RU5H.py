import re
import json

"""
Template
----------------
termoPT:
        ES:
        EN:
"""

f1 = open("middle_output/output_1_RU5HW615037.json", encoding="UTF-8")
d1 = json.load(f1)

f2 = open("middle_output/output_1_bilingual.json", encoding="UTF-8")
d2 = json.load(f2)

dici = {}

for key, value in d2.items():
    print(key)
    if d1.get(key) != None:
        dici[d1[key]] = {
                            "en": key,
                            "es": value
                        } 

with open('middle_output/output_2_CIH_RU5H.json', 'w', encoding='UTF-8') as output:
    json.dump(dici, output, ensure_ascii=False, indent=4)

output.close()