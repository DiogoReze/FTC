import re

try:
  entrada = str(input())

  palavra = entrada.split(' ')

  #palavra = entrada.split(' ')

  #testes extras

  #verificar o caso de entrada vazia
  if (len(palavra) == 7):
    status00 = True
  elif entrada == "" or entrada == " ":
    status00 = False
  else:
    status00 = False

  #status00 = False if t == 1 else True

  #verifica sem há 7 entradas
  #status0 = True if (len(palavra) == 7) else False
  #print(status00)

  if status00:
    # teste autor
    char_0 = re.match('\d',palavra[0])

    n_letras = re.findall('[a-zA-Z]', palavra[0])
    n_numeros = re.findall('[0-9]', palavra[0])
    n_especiais = re.findall('[^a-zA-Z0-9]',palavra[0])

    status1 = False if ((char_0) or (len(n_letras) <= len(n_numeros)) or n_especiais) else True

    #print(status1)

    # teste senha

    senhaT = palavra[1].split('.')
    status20 = []

    if len(senhaT) == 4:
      status20.append(True)
      for i in range(len(senhaT)):
        if re.findall('(([A-F]\d)|(\d[A-F])|(\d\d))',senhaT[i]) and (len(senhaT[i]) == 2):
          status20.append(True)
          #print(senhaT[i],"Ok")
        else:
          status20.append(False) 
          #print(senhaT[i],"Not Ok")

      for i in senhaT:                                            #################      
        if re.findall('[0-9][0-9]',i):
          #print(i)
          n1 = int(int(i)/10)
          n2 = int(i)-int(int(i)/10)*10
          if n1 != n2:
            status20.append(True) 
          else:
            status20.append(False)                                #################
    elif senhaT == "":
      status20.append(False)
    else:
      status20.append(False)

    status2 = True
    for i in range(len(status20)):
      if status20[i] == False:
        status2 = False

    #print(status20,status2)
    #print(status2)

    # IP do autor

    IPT = palavra[2].split('.')
    
    status30 = []

    padraoLetra = r'([^0-9])'
    padrao1 = r'([0][0-9])' #00,01,02,03,04,05,06,07,08,09
    padrao2 = r'([0][0][0-9])' #000,001,002,003,004-009
    padrao3 = r'([0][0-9][0-9])' #000,099


    if len(IPT) == 4:
      status30.append(True)
      for i in IPT:
        #print(i)
        if re.findall(padraoLetra,i):
          status30.append(False)
          #print("Tem caracter que nao é numero")
        else:
          status30.append(True) if (1 <= len(i) <= 3) and (0 <= int(i) <= 255) else status30.append(False)
          status30.append(False) if (0 <= int(i) < 10) and ((re.findall(padrao1,i))or(re.findall(padrao2,i))) else status30.append(True)
          status30.append(False) if (10 <= int(i) < 100) and (re.findall(padrao3,i)) else status30.append(True)
          #print(int(i), int(int(i)/100), int((int(i)%100)%100/10), int(i)%10  )

    elif IPT == "":
      status30.append(False)
    else:
      status30.append(False)

    status3 = True
    for i in status30:
      if i == False:
        status3 = False
    
    #print(status30)
    #print(status3)

    #Email

    status40 = []

    email = palavra[3]

    padraoArroba = r'@'
    arroba = re.findall(padraoArroba, email)
    status40.append(True) if (len(arroba) == 1) else status40.append(False)

    cont = 0
    for i in email:
      if re.match(padraoArroba,i):
        t = cont
      cont = cont + 1

    status40.append(True) if t > 0 else status40.append(False)

    padraoE1 = r'[a-zA-Z]'
    status40.append(True) if re.match(padraoE1,email) else status40.append(False)

    status40.append(True) if re.findall('\.', email[t:cont]) else status40.append(False)
    status40.append(False) if email=="" else status40.append(True)

    status4 = True
    for i in status40:
      if i == False:
        status4 = False

    #print(status4)

    # transacao

    transacao = palavra[4]

    tipoTran = ("pull push stash fork pop").split(' ')

    #print(tipoTran)

    status50 = []
    for i in tipoTran:
      status50.append(True) if re.fullmatch(i,transacao) else status50.append(False)
    
    status5 = False
    for i in status50:
      if i == True:
        status5 = True
    
    #print(status50)
    #print(status5)

    #repositorio

    repos = palavra[5]

    padraoRepo = r'([^a-z0-9_])'
    padraoRepo1 = r'([\s])'

    status60 = []
    status60.append(False) if re.findall(padraoRepo, repos) else status60.append(True)
    status60.append(True) if not re.findall(padraoRepo1, repos) else status60.append(False)
    status60.append(False) if repos == "" else status60.append(True)

    status6 = True
    for i in status60:
      if i == False:
        status6 = False

    #print(re.findall(padraoRepo, repos))
    #print(repos)
    #print(status5)

    # Hash

    hash = palavra[6]

    padraoHash = r'([^0-9a-f])'

    status70 = []
    status70.append(True) if len(hash) == 32 else status70.append(False)
    status70.append(False) if re.findall(padraoHash,hash) else status70.append(True)

    status7 = True
    for i in status70:
      if i == False:
        status7 = False

    #print(status60, status6)
    #print(status7)

    if status00 and status1 and status2 and status3 and status4 and status5 and status6 and status7:
      status = True
    else:
      status = False

    print(status)
  else:
    print(status00)

except EOFError:
  print(False)