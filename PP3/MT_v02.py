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

text,regras,qq,n,palavras = entradaDados()

for i in range(len(palavras)):   #laco para percorrer cada palavra armazenada em words (cada linha é uma palavra)
    digitosP = list(palavras[i])          #a cada palavra, criamos uma lista composta por cada algarismo da palavra
    digitosP.append('b')               #acrescenta o 'b' ao fim de cada palavra para conseguirmos opera-la de acordo com as regras da funcao de transicao

    #movCabeca = ''
    #qA = '0'
    #cabecote = 0
    #tempD = digitosP
    tempDi,qAi,qA,tempD,movCabeca = mTuring(regras,digitosP)
    #for j in range(len(regras)):
    #    tempDi = str(regras[j][2])
    #    qAi = str(regras[j][0])
    #    if (str(tempD[cabecote]) == tempDi) and  (qA == qAi):
    #        qA       = str(regras[j][1])
    #        tempD[cabecote] = str(regras[j][3])
    #        movCabeca       = str(regras[j][4])
    #    
    #        if movCabeca == 'D': 
    #            cabecote = cabecote + 1
    #        if movCabeca == 'E': 
    #            cabecote = cabecote - 1

    #    while movCabeca != 'P':
    #        for j in range(len(regras)):
    #            tempDi = str(regras[j][2])
    #            qAi = str(regras[j][0])
    #            if (str(tempD[cabecote]) == tempDi) and  (qA == qAi):
    #                qA       = str(regras[j][1])
    #                tempD[cabecote] = str(regras[j][3])
    #                movCabeca        = str(regras[j][4])

    #                if movCabeca == 'D': 
    #                    cabecote = cabecote + 1
    #                if movCabeca == 'E': 
    #                    cabecote = cabecote - 1
                    #print(c)
    
    temp = ''
    tempD.pop()
    for i in digitosP:
        temp = temp + i
    #print(temp,x)
    if qA == str(qq[1]):
        temp = temp + ' ' + 'ACEITA'
    if qA == str(qq[2]):
        temp = temp + ' ' + 'REJEITA'
    print(temp)
