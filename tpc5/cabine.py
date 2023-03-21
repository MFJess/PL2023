import re 

# simulador de cabine telefonica
# operacoes:
# 1 LEVANTAR - inicio de uma interacao
# 2 POUSAR - fim de interacao, é indicado o montante a ser devolvido
# 3 MOEDA <LISTA DE VALORES> - insercao de moedas 
    # (testa se moedas sao validas, se houver pelo menos 1, dá mensagem de erro)
# 4 T=numero - disca o nr (se nao tiver 9 algarismos e nao comecar por "00" dá erro)
    # comeca por "601" ou "641" -> bloqueia a chamada
    # comeca por "800" (verdes) -> custo = 0€
    # comeca por "808" (azuis) -> custo 0,10€   
    # comeca por "2" (nacionais) -> saldo minimo e custo = 0,25€
    # comeca por "00" (internacionais) -> o saldo deve ser >= 1,5€;
        # se saldo suficiente -> custo = 1,5€
        # senão -> máquina volta ao estado de introduzir moedas
# 5 ABORTAR - interrompe a interacao. Maquina devolve as moedas

# le o input e define a operacao a executar
def define_status(input : str) -> int:
    if(re.match(r"LEVANTAR", string) is not None): 
        return 1
    elif(re.match(r"POUSAR", string) is not None):
        return 2
    elif(re.match(r"MOEDAS ", string) is not None):
        print("deu crl, atualizei o status")
        return 3
    elif(re.match(r"T=", string) is not None):
        return 4
    elif(re.match(r"ABORTAR", string) is not None):
        return 5
    else:
        return 0

# recebe a string das moedas para depositar e transforma num valor somavel ao saldo
def trata_moedas(moedas : str) -> float:
    global saldo
    valor = 0
    print("before",moedas)
    moedas = re.sub(r"5c","0.05",moedas)
    moedas = re.sub(r"10c","0.10",moedas)
    moedas = re.sub(r"20c","0.20",moedas)
    moedas = re.sub(r"50c","0.50",moedas)
    moedas = re.sub(r"1e","1.00",moedas)
    moedas = re.sub(r"2e","2.00",moedas)
    print("after substituicoes",moedas)
    moedas = re.findall(r"(?i)0.05|0.10|0.20|0.50|1.00|2.00",moedas)
    print("moedas: ",moedas) 
    for i in moedas:
        valor += float(i)
    print(valor)
    return valor

def deposita(deposito : float) -> None:
    global saldo
    saldo += deposito
    print_saldo_atual()

def gasta(gasto : float) -> None:
    global saldo
    saldo -= gasto
    print_saldo_atual()

def valor_tostring(valor : float) -> str:
    valor_str = str(valor)
    string = re.sub(r"\.","e",valor_str) + "c"
    return string

def print_saldo_atual() -> None:
    global saldo
    print("Saldo atual:", valor_tostring(saldo), "\n")

def define_preco(input: str) -> None:
    global saldo

    numero = (re.findall(r"[0-9]", input))

    if(len(numero) != 9):
        if (int(numero[0]) != 0 or int(numero[1]) != 0):
            print("Numero invalido")
        else:
            if(saldo < 1.5):
                print("Saldo insuficiente.\n")
                STATUS = 1
            else:
                print("Custo da chamada = 1.5\n")
                gasta(1.5)

    elif(re.search(r"^T=641",input)) is not None:
        print("Este numero não é permitido. Por favor insira outro.")
   
    elif(re.search(r"^T=800",input)) is not None:
        print("Chamada gratuita")
   
    elif(re.search(r"^T=808",input)) is not None:
        print("Custo da chamada = 0.10")
        gasta(0.10)
   
    elif(re.search(r"^T=2",input)) is not None:
        if(saldo < 0.25):
            print("Saldo insuficiente")
            STATUS = 1
        else:
            print("Custo da chamada = 0.25")
            gasta(0.25)
    else:
        print("Numero invalido")
            

moedas = []
saldo = 0
numero = ""
STATUS = 1

print("Escolha uma opção:\nLEVANTAR: Iniciar uma chamada\nMOEDAS #e ##c ...: Deposite as suas moedas\nT=#########: Insira um numero de telefone\nABORTAR: Cancele a chamada\nPOUSAR: Finalizar o processo\n\n")
while(STATUS != 2):
    string = input()
    STATUS = define_status(string)

    if(STATUS == 1):
        moedas = input("Introduza moedas.\nExemplo: MOEDAS #e ##c #e ##c:")
        STATUS = 3

    elif(STATUS == 3):
        deposita(trata_moedas(string))
        print(saldo)
        STATUS = 4

    elif(STATUS == 4):
        numero = define_preco(string)
    
    elif(STATUS == 5): 
        STATUS = 2

    elif(STATUS == 2):
        break

    else:
        print("Operaçao invalida.\n")
        STATUS = 2

print("troco=", valor_tostring(saldo), "; Volte sempre!")

