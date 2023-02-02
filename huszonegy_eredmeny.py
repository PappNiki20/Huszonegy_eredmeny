# megoldas
def eredmenyek(jlapjai:list, glapjai:list):
     jpontszama = ossz(jlapjai)
     gpontszama = ossz(glapjai)
if eredmenyek.jpontszama == 21 and eredmenyek.gpontszama < 21:
        print("Játékos nyert")

def ossz(lista):
    lapossz = 0
    for i in lista:
        lapossz += i
    return lapossz
# Teszt esetek

# játékos veszt
def jvesztes_nagyobb_mint_huszonegy_teszt():
    
   if eredmenyek.jpontszama > 21:
        print("A jvesztes_nagyobb_mint_huszonegy teszt sikeres")

   else:
        print("A jvesztes_nagyobb_mint_huszonegy teszt sikertelen!")


def jvesztes_kevesebb_mint_a_gep_teszt():
    
   if eredmenyek.jpontszama < eredmenyek.gpontszama:
        print("A jvesztes_kevesebb_mint_a_gep teszt sikeres")

   else:
        print("A jvesztes_kevesebb_mint_a_gep sikertelen!")



def jvesztes_gepkozelebb_huszonegyhez_teszt():
    
   if eredmenyek.gkozelebb < eredmenyek.jkozelebb:
        print("A jvesztes_gepkozelebb_huszonegyhez teszt sikeres")

   else:
        print("A jvesztes_gepkozelebb_huszonegyhez sikertelen!")

# gép veszt

def gvesztes_nagyobb_mint_huszonegy_teszt():
    
   if eredmenyek.gpontszama > 21:
        print("A gvesztes_nagyobb_mint_huszonegy teszt sikeres")

   else:
        print("A gvesztes_nagyobb_mint_huszonegy teszt sikertelen!")


def gvesztes_kevesebb_mint_a_jatekos_teszt():
    
   if eredmenyek.gpontszama < eredmenyek.jpontszama:
        print("A gvesztes_ponthuszonegy teszt sikeres")

   else:
        print("A gvesztes_ponthuszonegy sikertelen!")



def gvesztes_gepkozelebb_huszonegyhez_teszt():
    
   if eredmenyek.jkozelebb < eredmenyek.gkozelebb:
        print("A gvesztes_gepkozelebb_huszonegyhez teszt sikeres")

   else:
        print("A gvesztes_gepkozelebb_huszonegyhez sikertelen!")


# játékos nyert

def jnyert_pont_huszonegy_teszt():
    if eredmenyek.jpontszama == 21:
        print("jnyert_pont_huszonegy_teszt sikeres")
    else:
        print("")