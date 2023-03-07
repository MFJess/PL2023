import re
import pprint

# TPC3: Processador de Pessoas listadas nos Róis de Confessados

# Construa agora um ou vários programas Python para processar o texto 'processos.txt' com o intuito de calcular frequências de alguns elementos 
# (a ideia é utilizar arrays associativos, dicionários em Python, para o efeito) conforme solicitado a seguir:

f = open("processos.txt")
lines = f.readlines()
separated_lines = []

for line in lines:
    separated_line = re.split(r"::", line)
    separated_lines.append(separated_line)

nr_lines = len(separated_lines) # 37880

# a) Calcula a frequencia de processos por ano (1º elemento da data)
years = dict()
for line in separated_lines:
    year = re.split(r"-", line[1])[0]
    if(year not in years.keys()):
        years[year] = 1
    else:
        years[year] += 1

for key in years:
    years[key] = round(years[key] * 100 / nr_lines,33)

# pp = pprint.PrettyPrinter(width = 41, compact=True)
# pp.pprint(years)


# b) Calcula a frequencia de nomes proprios (1º usado em cada nome) e apelidos (o ultimo em cada nome) por seculos e apresenta os 5 mais usados
seventeenth_names = dict()
seventeenth_surnames = dict()
eighteenth_names = dict()
eighteenth_surnames = dict()
nineteenth_names = dict()
nineteenth_surnames = dict()
twentieth_names = dict()
twentieth_surnames = dict()
by_year = [seventeenth_names, seventeenth_surnames, eighteenth_names, eighteenth_surnames, nineteenth_names, nineteenth_surnames, twentieth_names, twentieth_surnames]

for line in separated_lines:
    year = re.split(r"-", line[1])[0]
    name = re.split(r" ", line[2])[0]
    surnames = re.split(r" ", line[2])
    surname = surnames[len(surnames)-1]

    if(int(year) < 1701 ):
        if(name not in seventeenth_names):
            seventeenth_names[name] = 1
        else:
            seventeenth_names[name] += 1

        if(name not in seventeenth_surnames):
            seventeenth_surnames[name] = 1
        else:
            seventeenth_surnames[name] += 1  
        
    elif(int(year) < 1801 ):
        if(name not in eighteenth_names):
            eighteenth_names[name] = 1
        else:
            eighteenth_names[name] += 1 

        if(name not in eighteenth_surnames):
            eighteenth_surnames[name] = 1
        else:
            eighteenth_surnames[name] += 1 

    elif(int(year) < 1901 ):
        if(name not in nineteenth_names):
            nineteenth_names[name] = 1
        else:
            nineteenth_names[name] += 1 

        if(name not in nineteenth_surnames):
            nineteenth_surnames[name] = 1
        else:
            nineteenth_surnames[name] += 1  
    
    else:
        if(name not in twentieth_names):
            twentieth_names[name] = 1
        else:
            twentieth_names[name] += 1

        if(name not in twentieth_surnames):
            twentieth_surnames[name] = 1
        else:
            twentieth_surnames[name] += 1 
    

pp = pprint.PrettyPrinter(width = 41, compact=True)
for value in by_year:
    print("\n")
    pp.pprint(value)

        
# c) Calcula a frequencia dos varios tipos de relaçao: irmao, sobrinho, etc..


# d) Converta os 20 primeiros registos num novo ficheiro de output em formato JSON