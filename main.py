import requests
import json
from bs4 import BeautifulSoup

res = requests.get("https://digitalinnovation.one/")
res.encoding = 'utf-8'


soup = BeautifulSoup(res.text, 'html.parser')

profs = soup.find_all(class_="col-md-3")


all_prof = []


for prof in profs:
    if not prof.find('h4'):
        break
    else:
        nome = prof.img['alt']
        cargo = prof.h4.text
        empresa = prof.h5.text
        all_prof.append({'Instrutor': nome, 'Profissão': cargo, 'Empresa': empresa})

print(all_prof)
with open('professores.json', 'w') as json_file:
    json.dump(all_prof, json_file, indent=3, ensure_ascii=False)
