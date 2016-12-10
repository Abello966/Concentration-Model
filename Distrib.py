from random import random, shuffle

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
        

    

base_util = 1
utilidade = {'OS1': base_util, 'OS2': base_util, 'OS3': base_util, 'OS4': base_util}       

for i in range(100):
    probs = Distrib(utilidade)
    utilidade[probs.randomChoice()] += 1


result = Distrib(utilidade)
result.normalize()
print(result)
