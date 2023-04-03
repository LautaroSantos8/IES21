import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
def actividad2():
    URL='http://127.0.0.1:5500/ia.html'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    tags=soup.find('table')
    for item in tags.find_all('tr')[1:]:
        semestre= item.find_all('td')
        if (semestre[2].text == '3') or (semestre[2].text == '4') :
            print('codigo:',semestre[0].text,'Nombre:',semestre[1].text)
        

def actividad3():
    expresion = '(( |")(\d{2})-(\d{8})-(\d{1})( |"))'
    with open("data.json") as datos:
        for linea in datos:
            res = re.findall(expresion, linea)
            if res:
                print(linea)
print(actividad2())
