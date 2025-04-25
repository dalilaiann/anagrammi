from time import time
from functools import lru_cache
import copy

from database.DAO import DAO

class Model:

    def __init__(self):
        self.set_soluzioni_corrette=set()
        self.set_soluzioni_sbagliate = set()

    def calcola_anagrammi(self,  parola: str):      #rappresenta entry point della funzione ricorsiva per evitare di accumulare i risultati di successivi anagrammi
        self.set_soluzioni=set()  #RICORDARSI di resettare il risultato
        self._ricorsione([], parola)
        #invece di "dog" abbiamo ['d','o','g']
        return self.set_soluzioni_corrette, self.set_soluzioni_sbagliate


    def _ricorsione(self, parziale, rimanenti):
        if len(rimanenti)==0:
            #self.lista_soluzioni.append(parziale)
            #print(parziale)
            #verifico che la soluzione sia nel dizionario
            if DAO.check_parola("".join(parziale))==True:
                self.set_soluzioni_corrette.add(copy.deepcopy("".join(parziale)))
            else:
                self.set_soluzioni_sbagliate.add(copy.deepcopy("".join(parziale)))
        else:
            for i in range(len(rimanenti)):
                #if DAO.check_prefisso("".join(parziale)+rimanenti[i])==True:
                    parziale.append(rimanenti[i])
                    #chiamare ricorsione con parziale e tutte le lettere rimanenti - lettera
                    nuove_rimanenti=rimanenti[:i]+rimanenti[i+1:]
                    #ora parziale contiene una lettera in più e nuove_rimanenti una in meno
                    self._ricorsione(parziale,nuove_rimanenti)
                    #devo fare BACKTRACKING per evitare che le nuove soluzioni siano calcolate in base alle ultime calcolate
                    parziale.pop() #considero tutte tranne l'ultima messa alla fine degli anagrammi calcolati con la stessa


if __name__ == "__main__":
    model = Model()
    start_time=time()
    risultato=model.calcola_anagrammi("dog")
    end_time=time()
    print(f"Elapsed time: {end_time-start_time}")
    print(risultato)
