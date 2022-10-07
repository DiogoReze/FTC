#lendo primeira linha - funcao de transicao
fTra = input()
fTra = eval(fTra)
rules = (fTra['delta'])
states = [fTra['inicial'],fTra['aceita'],fTra['rejeita']]

#ler numero de palavras
nW = int(input())

#lendo cada palavra
words = []
for i in range(nW):
  words.append(input())

for i in range(len(words)):   #laco para percorrer cada palavra armazenada em words (cada linha é uma palavra)
    c = list(words[i])          #a cada palavra, criamos uma lista composta por cada algarismo da palavra
    c.append('b')               #acrescenta o 'b' ao fim de cada palavra para conseguirmos opera-la de acordo com as regras da funcao de transicao

    cc = c
    i = 1
    w = ''
    x = '0'
    head = 0
    for j in range(len(rules)):
        ci = str(rules[j][2])
        xi = str(rules[j][0])
        #print(j)
        if (str(cc[head]) == ci) and  (x == xi):
            x       = str(rules[j][1])
            cc[head] = str(rules[j][3])
            w       = str(rules[j][4])
        
            if w == 'D': head = head + 1
            if w == 'E': head = head - 1
            #print(c)

        while w != 'P':
            for j in range(len(rules)):
                ci = str(rules[j][2])
                xi = str(rules[j][0])
                if (cc[head] == ci) and  (x == xi):
                    x        = str(rules[j][1])
                    cc[head] = str(rules[j][3])
                    w        = str(rules[j][4])

                    if w == 'D': head = head + 1
                    if w == 'E': head = head - 1
                    #print(c)
    
    temp = ''
    cc.pop()
    for i in c:
        temp = temp + i
    #print(temp,x)
    if x == str(states[1]):
        temp = temp + ' ' + 'ACEITA'
    if x == str(states[2]):
        temp = temp + ' ' + 'REJEITA'
    print(temp)
