nome = input("Digite o nome do time: ")
time1 = int(input("Quantidade de gols do time: "))
nomi = input("Digite o nome do segundo time: ")
time2 = int(input("Quantidade de gols do time: "))

if time1 > time2:
    print (f"O time {nome} ganhou com {time1}! Com diferença de",(time1-time2),"ponto.")
elif time2 > time1:
    print (f"O time {nomi} ganhou com {time2}! Com diferença de",(time2-time1),"ponto.")
elif time1 == time2:
    print ("O jogo acabou em empate.")