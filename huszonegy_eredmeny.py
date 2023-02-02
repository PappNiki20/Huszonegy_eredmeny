# megoldas
def eredmenyek(jlapjai:list, glapjai:list):
     jpontszama = ossz(jlapjai)
     gpontszama = ossz(glapjai)
     gkozelebb = 21-gpontszama
     jkozelebb = 21-jpontszama


def ossz(lista):
    lapossz = 0
    for i in lista:
        lapossz += i
    return lapossz
# Teszt esetek

def jvesztes_ponthuszonegy_teszt():
    
   if eredmenyek.jpontszama == 21:
        print("A jvesztes_ponthuszonegy teszt sikeres")

   else:
        print("A jvesztes_ponthuszonegy sikertelen!")



def jvesztes_gepkozelebb_huszonegyhez_teszt():
    
   if eredmenyek.gkozelebb < eredmenyek.jkozelebb:
        print("A jvesztes_gepkozelebb_huszonegyhez teszt sikeres")

   else:
        print("A jvesztes_gepkozelebb_huszonegyhez sikertelen!")
