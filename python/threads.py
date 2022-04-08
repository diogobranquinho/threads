from threading import Thread
import random

def soma(amostra, origem):
    #print("Amostra " + origem + " " + str(amostra))
    s = 0
    for n in amostra:
        s = s + n
    print("Soma: " + origem + " " + str(s)) 

amostraA = random.sample(range(1000000),100000)
amostraB = random.sample(range(1000000),10)

#Primeira rodada
print("Primeira rodada de processamento, threads livres")
tA = Thread(target=soma, args=(amostraA,"A",))
tB = Thread(target=soma, args=(amostraB,"B",))
tA.start()
tB.start()

#Segunda rodada
print("Segunda rodada de processamento, join limitará a exec")
tA = Thread(target=soma, args=(amostraA,"A",))
tB = Thread(target=soma, args=(amostraB,"B",))
tA.start()
tB.start()
tA.join()
tB.join()