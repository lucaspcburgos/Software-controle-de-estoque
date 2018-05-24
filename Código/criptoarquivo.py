def lerChavePublica():
    arq = open("chavePublica.txt", "r")
    texto = arq.read
    e = ""
    n = ""
    var = True
    for numero in texto:
        if var == True:
            e += numero
            if numero == ";":
                var = False
        else:
            n += numero      
    e = int(e)
    n = int(n)
    return (e,n)

def lerChavePrivada():
    arq = open("chavePublica.txt", "r")
    texto = arq.read
    e = ""
    n = ""
    var = True
    for numero in texto:
        if var == True:
            e += numero
            if numero == ";":
                var = False
        else:
            n += numero      
    d = int(d)
    n = int(n)
    return (d,n)

def criptografa(dicionario,letra):

    chavesDic = dicionario.keys()
    
def descriptografaParaDic(arquivo):
    num1 = lerChavePrivada()[0]
    num2 = lerChavePrivada()[1]
    elementoFinal = ""
    arq = open(arquivo, "r")
    texto = arq.read()
    
    for elemento in texto:
        letra = chr((elemento**num2) % num1)
        elementoFinal += letra







def escreveNoArquivo(dicionario):
 x+1   



