def lerChaveDoArquivo():
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

def criptografa(letra):

    chavesDic = dicionario.keys()
    for i
def descriptografaParaDic():
    x+1


def escreveNoArquivo(dicionario):
    for palavra in dic:


"""
pegar as chaves do dicionario e adicionar na string  seguido de ';' e depois cada elemento da tupla
separados por '?' e uma '!' no final da ultima.
depois é so escrever essa string criptografada no arquivo

para usar no dicionario cria uma funçao que le o arquivo e depois de descriptografado, cria a mesma string 
da funçao anterior toda vez que encontra um ';'
cria a chave do dicionario e quando encontra '?' adiciona elementos na tupla 
 -> problema: tuplas sao imutavei <- 
quando encontrar '!' recomeça adicionando como chave ate o ';'
"""



