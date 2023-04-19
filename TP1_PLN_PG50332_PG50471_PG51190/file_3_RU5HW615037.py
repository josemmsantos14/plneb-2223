import re
import json

file = open('data/RU5HW615037.xml', encoding='UTF-8')
text = file.read()

text = re.sub(r'</?page.*>', '', text)

text = re.sub(r'</?(?:text|i|b).*?><\/?(?:i|b|text).*?>', '', text)

entries = re.findall(r'</?text.*?>(.*?-.*?)</text>', text)

dic = {}

# print(entries)

for i in range(len(entries)):
    entries[i].strip()
    if entries[i][-1] == "-":
        entries.remove(entries[i])
    if "-" not in entries[i] and entries[i][-1] != "-":
        entries[i-1] = entries[i-1]+entries[i]

for entry in entries:
    term_en = entry.split(" - ")[0].strip().lower()
    term_pt = entry.split(" - ")[1].strip().lower()
    dic[term_en] = term_pt

# print(dic)

with open('middle_output/output_1_RU5HW615037.json', 'w', encoding='UTF-8') as output:
    json.dump(dic, output, ensure_ascii=False, indent=4)

output.close()