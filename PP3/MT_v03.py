def entradaDados():
    text = eval(input())
    regras = (text['delta'])
    qq = [text['inicial'],text['aceita'],text['rejeita']]
    n = int(input())

    palavras = []
    for i in range(n):
      palavras.append(input())

    return text,regras,qq,n,palavras

def mTuring(regras,digitosP):
    tempD = digitosP
    movCabeca = str('')
    qA = str('0')
    cabecote = 0
    for i in range(len(regras)):
        tempDi = str(regras[i][2])
        qAi = str(regras[i][0])
        if (str(tempD[cabecote]) == tempDi) and  (qA == qAi):
            qA       = str(regras[i][1])
            tempD[cabecote] = str(regras[i][3])
            movCabeca       = str(regras[i][4])
        
            cabecote = MC(movCabeca,cabecote)
        
        while movCabeca != 'P':
            for j in range(len(regras)):
                tempDi = str(regras[j][2])
                qAi = str(regras[j][0])
                if (str(tempD[cabecote]) == tempDi) and  (qA == qAi):
                    qA       = str(regras[j][1])
                    tempD[cabecote] = str(regras[j][3])
                    movCabeca        = str(regras[j][4])

                    cabecote = MC(movCabeca,cabecote)

    return tempDi,qAi,qA,tempD,movCabeca

def MC(movCabeca,cabecote):
    if movCabeca == 'D': 
        cabecote = cabecote + 1
    if movCabeca == 'E': 
        cabecote = cabecote - 1
    return cabecote

def saida(digitosP,qA,qq):
    temp = ''
    for i in digitosP:
        temp = temp + i
    if qA == str(qq[1]):
        temp = temp + ' ' + 'ACEITA'
    if qA == str(qq[2]):
        temp = temp + ' ' + 'REJEITA'
    return temp

#===============================================================================
text,regras,qq,n,palavras = entradaDados()

for i in range(len(palavras)):   
    digitosP = list(palavras[i])
    digitosP.append('b') 

    tempDi,qAi,qA,tempD,movCabeca = mTuring(regras,digitosP)
    
    tempD.pop()
    temp = saida(digitosP,qA,qq)
    print(temp)
