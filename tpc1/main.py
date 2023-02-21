#Lista com todas as informações
data = list()

#Lê o ficheiro e guarda as informações
def read_csv(reader: str) -> None:

    reader = open(reader,'r')

    for line in reader:
        
        #Lista com as chaves para cada paciente
        if line.startswith('idade'):
            #Remove os caracteres que não interessam
            k = line.strip('\n').split(',')
        
        else:
            #Remove os caracteres que não interessam
            v = line.strip('\n').split(',')

            #Adiciona a lista geral um dicionario menor com as infos do paciente
            data.append(dict(zip(k,v)))

#Calcula a distribuicao por sexo (M,F)
def sick_by_gender() -> dict:
    res = dict()

    m_total = f_total = 0 #Total de pacientes
    m_sick = f_sick = 0 #Total de doentes
    
    for person in data:
        #Confere o sexo
        if person['sexo'] == 'M':
            #Acrescenta ao total
            m_total += 1

            if person['temDoença'] == '1':
                #Acrescenta aos doentes
                m_sick += 1
        
        #O mesmo procedimento mas para o outro sexo
        elif person['sexo'] == 'F':
            f_total += 1

            if person['temDoença'] == '1':
                f_sick += 1

    res['M'] = (m_sick,m_total)
    res['F'] = (f_sick, f_total)

    #Retorna as porcentagens de doentes no total
    return res

#Calcula a distribuicao por escalao
def sick_by_age() -> dict:
    res = dict()

    #Lista ordenada com a idade e o bool de doença de todos pacientes
    patients = sorted([(int(p['idade']), int(p['temDoença'])) for p in data])

    #Intervalos de idade
    i = 30
    j = 34 

    #Contadores para cada escalao
    aux_sick = aux_total = 0

    for age,sick in patients:  

        #Se passar esta condicao significa que esta no intervalo do escalao
        if age <= j:
            aux_sick += sick #Se estiver doente soma 1, se nao soma 0
            aux_total += 1 
       
        #Se chegar aqui significa que saiu do escalao e atualiza para o novo
        else:
            res[(i,j)] = (aux_sick,aux_total) #Valores do ultimo escalao 
            aux_sick = 0 
            aux_total = 0
            i += 5
            j += 5
    
    res[(i,j)] = (aux_sick,aux_total) #Para garantir que o ultimo sera contado

    return res

#Calcula a distribuicao por nivel de colesterol
def sick_by_col() -> dict:
    res = dict()

    #Calcula o menor colesterol
    minimum = min([int(i['colesterol']) for i in data])

    #Lista ordenada com a idade e o bool de doença de todos pacientes
    patients = sorted([(int(p['colesterol']), int(p['temDoença'])) for p in data])

    #Niveis de colesterol
    i = minimum
    j = minimum + 9

    #Contadores para cada nivel
    aux_sick = aux_total = 0

    for col,sick in patients:  

        #Se passar esta condicao significa que esta no nivel
        if col <= j:
            aux_sick += sick #Se estiver doente soma 1, se nao soma 0
            aux_total += 1 
       
        #Se chegar aqui significa que saiu do nivel e atualiza para o novo
        else:
            res[(i,j)] = (aux_sick,aux_total) #Valores do ultimo nivel            
            aux_sick = 0 
            aux_total = 0
            i += 10
            j += 10

        res[(i,j)] = (aux_sick,aux_total) #Para garantir o ultimo
    
    return res


read_csv('myheart.csv')