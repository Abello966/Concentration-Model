from random import random, shuffle
import sys
import numpy as np
import matplotlib.pyplot as plt

#Simple class for a prob distribution
#Essentialy a dictionary
class Distrib(dict):

    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)

    def normalize(self):
        """
        Normaliza para um
        """
        total = float(sum(self.values()))
        if total == 0: return
        for key in self.keys():
            self[key] = self[key] / total

    def randomChoice(self):
        """
        Escolhe uma opcao aleatoria da distribuicao com peso relativo
        a sua probabilidade
        """
        #normaliza para funcionar
        self.normalize()
        sweetnum = random() #[0, 1)
        tot = 0

        #lista de chaves
        keys = list(self.keys())
        shuffle(keys)

        #Faz escolha
        #Em ordem aleatoria soma as probabilidades e verifica
        #se a soma passa o numero aleatorio gerado. O primeiro
        #que passa o numero aleatorio ganha
        for key in keys:
            tot += self[key]
            if tot > sweetnum:
                return key
        

#trata args
if len(sys.argv) < 2:
    print("Numero insuficiente de argumentos; insira iteracoes e utilidade base")
    exit();

try:
    iters = int(sys.argv[1])
    base_util = float(sys.argv[2])
except:
    print("Erro ao processar argumentos")
    exit()


utilidade = {'OS1': base_util, 'OS2': base_util, 'OS3': base_util, 'OS4': base_util}       

for i in range(iters):
    probs = Distrib(utilidade)
    utilidade[probs.randomChoice()] += 1


result = Distrib(utilidade)
result.normalize()
#texto
#print(result)

#grafico de barra
#cria grafico de barra
ind = np.arange(4)
width = 1
fig, ax = plt.subplots()
values = tuple()
labels = tuple()
for keys, items in result.items():
    values += (items,)
    labels += (keys,)

ax.bar(ind, values, width)
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(labels)
plt.show()





