def entradaDados():
    text = eval(input())
    regras = (text['delta'])
    qq = [text['inicial'],text['aceita'],text['rejeita']]
    n = int(input())

    palavras = []
    for i in range(n):
      palavras.append(input())

    return text,regras,qq,n,palavras

def aceitaRejeita(digito,qq):
    saida = ''
    digito.pop()

    for i in digito:
        saida = saida + i
    if x == str(qq[1]):
        saida = saida + ' ' + 'ACEITA'
    if x == str(qq[2]):
        saida = saida + ' ' + 'REJEITA'
    return saida

def movCabecote(d,cabecote):
    if d == 'D': 
        cabecote = cabecote + 1
    if d == 'E': 
        cabecote = cabecote - 1
    return cabecote

def maqTuring(regras,tempD,cabecote,d,x):
    for j in range(len(regras)):
        chari   = str(regras[j][2])
        xi      = str(regras[j][0])
        if (str(tempD[cabecote]) == chari) and  (x == xi):
            x               = str(regras[j][1])
            tempD[cabecote] = str(regras[j][3])
            d               = str(regras[j][4])            
            cabecote = movCabecote(d,cabecote)
    return chari,xi,x,tempD,d,cabecote
#=================================================================================

text, regras, qq, n, palavras = entradaDados()

for i in range(len(palavras)):   
    digito = list(palavras[i])   
    digito.append('b')           

    cabecote = 0; tempD = digito; d = ''; x = '0'
    
    chari,xi,d,tempD,w,cabecote = maqTuring(regras,tempD,cabecote,d,x)
    while d != 'P':
        chari,xi,x,tempD,d,cabecote = maqTuring(regras,tempD,cabecote,d,x)
    
    print(aceitaRejeita(digito,qq))