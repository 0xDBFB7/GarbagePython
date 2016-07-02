import math
from sets import Set
import string
import random
random.seed()
things = '2.89 2.79 2.85 2.72 2.79 2.79 2.80 2.89 2.70 2.82 2.79 2.79 2.68 2.33'.split(" ")
from multiprocessing.dummy import Pool as ThreadPool 
pool = ThreadPool(7) 
def run(find):
    ent = 0.0
    mainstring = ''
    while(abs(ent-(float(find))) > float(0.003)):
        mainstring = mainstring+random.choice(list(string.ascii_lowercase))
        #mainstring = mainstring+random.choice(list(string.ascii_lowercase))
        stList = list(mainstring)
        alphabet = list(Set(stList)) # list of symbols in the string
        freqList = []
        for symbol in alphabet:
            ctr = 0
            for sym in stList:
                if sym == symbol:
                    ctr += 1
            freqList.append(float(ctr) / len(stList))
        # Shannon entropy
        ent = 0.0
        for freq in freqList:
            ent = ent + freq * math.log(freq, 2)
        ent=-ent
        if(len(mainstring) > 30):
            mainstring = ''
    return mainstring
results = pool.map(run, things)
print(results)




