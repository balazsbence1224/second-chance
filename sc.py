def keresesEsFrissites(x, tomb, sc, keretszam):
	
    for i in range(keretszam):
        if tomb[i] == x:
            sc[i] = True
            return True

    return False
    
def hellyetesitesEsFrissites(x, tomb, sc, keretszam, mutato, kerettomb):
    
    while(True):
        if not sc[mutato]:
            tomb[mutato] = x
            kerettomb.append(mutato)
            return (mutato+1)%keretszam
            
        sc[mutato] = False
        mutato = (mutato + 1) % keretszam

def kiiras(be_tomb):

    mutato = 0
    laphibak = 0
    keretszam = 3
    tomb = [0]*keretszam
    kerettomb = []
    
    for j in range(keretszam):
    	tomb[j] = -1
		
    sc = [False]*keretszam
    be_adat = be_tomb
    l = len(be_adat)
	
    for i in range(l):
        x = be_adat[i]
        if not keresesEsFrissites(x, tomb, sc, keretszam):
            mutato = hellyetesitesEsFrissites(x, tomb, sc, keretszam, mutato, kerettomb)
            laphibak += 1
        else:
            kerettomb.append("-")

    
    kitomb = []
    for i in kerettomb:
        if(i == 0):
            kitomb.append("A")
        elif(i == 1):
            kitomb.append("B")
        elif(i == 2):
            kitomb.append("C")
        elif(i == "-"):
            kitomb.append("-")
            
    k = 0
    while(k < len(kitomb)):
        if(k == len(kitomb)-1):
            print(kitomb[k])
        else:
            print(kitomb[k],end="")
        k += 1
            
    print(laphibak)

    
    
def main():
    example = input()
    be_tomb = example.split(",")

    kiiras(be_tomb)

if __name__=="__main__":
    main()


