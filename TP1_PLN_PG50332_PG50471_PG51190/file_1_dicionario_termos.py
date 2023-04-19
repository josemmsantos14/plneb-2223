import re, json

file = open('data/dicionario_termos_medicos_pt_es_en.xml', encoding='utf-8')
text = file.read()

text = re.sub(r'</?page.*>', '', text)
text = re.sub(r'</?text.*?>', '', text)
text = re.sub(r'</?i.*>', '', text)
text = re.sub(r'^.*?<b>português – inglês – espanhol</b>\n<b>português</b>\n<b>–</b>\n<b>inglês</b>\n<b>–</b>\n<b>espanhol</b>\n\n\n', '', text, flags=re.DOTALL | re.MULTILINE) #apagar todas as linhas acima do inicio do dicionario que queremos
text = re.sub(r'<b>português</b>\n<b>–</b>\n<b>inglês</b>\n<b>–</b>\n<b>espanhol</b>', '', text)
text = re.sub(r'<b>[0-9]{3}</b>\n<b>.*\n\n', '', text) #remover numero da página e termo que aparece em destaque no canto IMPARES (palavra depois do número)
text = re.sub(r'<b>.*\n<b>[0-9]{3}.*\n\n', '', text) #remover numero da página e termo que aparece em destaque no canto PARES (palavra antes do numero)
text = re.sub(r'<b>.*\n.*\n<b>[0-9]{3}.*\n\n', '', text) #exceção palavra com - no cabeçalho bloqueador-beta
text = re.sub(r'<fontspec.*', '', text) #limpar linha fontspec
text = re.sub(r'<b>[A-Z]{1}</b>', '', text) #apagar cada letra inicial do alfabeto
text = re.sub(r"\n+", r"\n", text) #uniformizar os parágrafos para ficar tudo com o mesmo espaçamento

text = re.sub(r'<b>(.*?)</b>\n<b>(.*?)</b>\n<b>(.*?)</b>\n<b>(.*?)</b>\n<b>(.*?)</b>\n<b>(.*?)</b>', r'<b>\1 \2 \3 \4 \5 \6</b>', text) #crise
text = re.sub(r'<b>(.*?)</b>\n<b>(.*?)</b>\n<b>(.*?)</b>\n<b>(.*?)</b>\n<b>(.*?)</b>', r'<b>\1 \2 \3 \4 \5', text)
text = re.sub(r'<b>(.*?)</b>\n<b>(.*?)</b>\n<b>(.*?)</b>\n<b>(.*?)</b>', r'<b>\1 \2 \3 \4</b>', text)
text = re.sub(r'<b>(.*?)</b>\n<b>(.*?)</b>\n<b>(.*?)</b>', r'<b>\1 \2 \3</b>', text)
text = re.sub(r'<b>(.*?)</b>\n<b>(.*?)</b>', r'<b>\1 \2</b>', text)
#TERMOS TODOS NA MESMA LINHA

text = re.sub(r'U\n(.*?)\n(.*?)\n(.*?)\n(.*?)\nE\n', r'U\n\1 \2 \3 \4\nE\n', text)
text = re.sub(r'U\n(.*?)\n(.*?)\n(.*?)\nE\n', r'U\n\1 \2 \3\nE\n', text)
text = re.sub(r'U\n(.*?)\n(.*?)\nE\n', r'U\n\1 \2\nE\n', text)
#TRADUÇÃO INGLES TODA NA MESMA LINHA

text = re.sub(r'\nE\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n<b>', r'\nE\n\1 \2 \3 \4 \5\n<b>', text)
text = re.sub(r'\nE\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n<b>', r'\nE\n\1 \2 \3 \4\n<b>', text)
text = re.sub(r'\nE\n(.*?)\n(.*?)\n(.*?)\n<b>', r'\nE\n\1 \2 \3\n<b>', text)
text = re.sub(r'\nE\n(.*?)\n(.*?)\n<b>', r'\nE\n\1 \2\n<b>', text)
#TRADUÇÃO ESPANHOL TODA NA MESMA LINHA

text = re.sub(r'(.*?)-\s(.*?)', r'\1\2', text) #juntar traduções que estavam separadas por - por estarem em linhas diferentes
text = re.sub(r'<b>(.*?)</b>\s(\)?)\n<b>(.*?)</b>', r'\n<b>\1\2\3</b>', text) #palato e cisto são exceções
text = re.sub(r'ante-braço\s', '', text) #exceção - ante-braço não tem traduções
text = re.sub(r'<b>anemia\s\(aplástica\/\shemolítica\/\shipercrómica\/\smacrocítica\/\smegaloblástica\/\smicrocítica\/\snormocítica\/\sperniciosa\)', r'<b>anemia (aplástica/ hemolítica/ hipercrómica/ macrocítica/ megaloblástica/ microcítica/ normocítica/ perniciosa)</b>', text) #exceção anemia faltava </b> no fim
text = re.sub(r'<b>dor\s\(em martelada\/\sem picada\/\sinsuportável\/\sviolenta\/\sem queimadura\/\ssurda\/\scompressiva\/\sdiffusa\/\sespasmódica\)', r'<b>dor (em martelada/ em picada/ insuportável/ violenta/ em queimadura/ surda/ compressiva/ diffusa/ espasmódica)</b>', text)
text = re.sub(r'<b>bloqueador-</b>\nβ', r'<b>bloqueador-β</b>', text) #exceção bloqueador beta

termos = re.findall(r'<b>(.*?)</b>', text)
en = re.findall(r'\nU\n(.*?)\n', text)
es = re.findall(r'\nE\n(.*?)\n', text)

dici={}
for i in range(len(termos)):
    dici[termos[i]] = {
        "en": en[i],
        "es": es[i]
    }

out = open ("middle_output/output_1_dicionario_termos_medicos.json", "w", encoding="utf-8")
json.dump(dici, out, ensure_ascii=False, indent=4)
out.close()