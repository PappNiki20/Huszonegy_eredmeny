# megoldas
def osszpontszam(lapok):
    pontok: int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]

    return pontok


def eredmeny(geplap, jatekoslap):
    jatekospontok: int = osszpontszam(jatekoslap)
    geppontok: int = osszpontszam(geplap)
    teszteredmeny = ""

#dontetlen
    if jatekospontok > 21 and geppontok > 21:
        teszteredmeny = "Mindkét oldalon több lap, mint 21"

    elif jatekospontok == geppontok:
        teszteredmeny = "döntetlen"

    elif jatekospontok < 21 and geppontok < 21 and len(jatekoslap) == len(geplap):
        teszteredmeny = "kevesebb mint 21 mindkettő, de ugyanannyi lapszám"


#jatekos veszt
    elif jatekospontok > 21:
        teszteredmeny = "több lap mint 21: játékos vesztett"

    elif jatekospontok == 19 and len(jatekoslap) > len(geplap):
        teszteredmeny = "19 pont, de több lap teszt: játékos vesztett"

    elif jatekospontok == 19 and len(jatekoslap) < len(geplap):
        teszteredmeny = "19 pont, de kevesebb lap teszt: játékos vesztett"
    
#jatekos nyer
    elif jatekospontok == 21:
        teszteredmeny = "pont 21 a lapok összege: játékos nyert"

    elif jatekospontok == 19 and len(jatekoslap) > len(geplap):
        teszteredmeny = "19 pont, de több lap teszt: játékos nyert"

    elif jatekospontok == 19 and len(jatekoslap) < len(geplap):
        teszteredmeny = "19 pont, de kevesebb lap teszt: játékos nyert"

    elif jatekospontok > geppontok:
        teszteredmeny = "kevesebb mint 21: játékos nyert"

#gep veszt
    elif geppontok > 21:
        teszteredmeny = "több mint 21: gép vesztett"

    elif geppontok == 19 and len(geplap) > len(jatekoslap):
        teszteredmeny = "19 pont, de több lap teszt: gép vesztett"

    elif geppontok == 19 and len(geplap) < len(jatekoslap):
        teszteredmeny = "19 pont, de kevesebb lap teszt: gép vesztett"
   
#gep nyer
    elif geppontok == 21:
        teszteredmeny = "pont 21: gép nyert"
    
    elif geppontok == 19 and len(geplap) > len(jatekoslap):
        teszteredmeny = "19 pont, de több lap teszt: gép nyert"

    elif geppontok == 19 and len(geplap) < len(jatekoslap):
        teszteredmeny = "19 pont, de kevesebb lap teszt: gép nyert"
    
    elif geppontok > jatekospontok:
        teszteredmeny = "kisebb mint 21: gép nyert"



    return teszteredmeny

#tesztek
def tesztek():
    dontetlen_21_ponttal()
    dontetlen_egyenlo_lap()
    dontetlen_tobbmint21()


    vesztes_jatekos_tobb_lap_mint_21()
    vesztes_jatekos_egyenlo_pont_tobb_lap()
    vesztes_jatekos_egyenlo_pont_kevesebb_lap()


    vesztes_gep_tobb_lap_mint_21()
    vesztes_gep_egyenlo_pont_tobb_lap()
    vesztes_gep_egyenlo_pont_kevesebb_lap()

    nyert_jatekos_pont_21()
    nyert_jatekos_pont_19_lap_tobb()
    nyert_jatekos_pont_19_lap_kevesebb()


    nyert_gep_pont_21()
    nyert_gep_pont_19_lap_tobb()
    nyert_gep_pont_19_lap_kevesebb()




#dontetlen
def dontetlen_21_ponttal():
    gep = [10, 10, 1]
    jatekos = [10, 5, 6]
    vart_eredmeny = "döntetlen"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("döntetlen, pont 21 pont teszt: sikeres")
    else:
        print("döntetlen, pont 21 pont teszt: sikertelen")


def dontetlen_tobbmint21():
    gep = [10, 10, 5]
    jatekos = [10, 10, 3]
    vart_eredmeny = "mindenkinek több, mint 21"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("mindenkinek több, mint 21 teszt: sikeres")
    else:
        print("mindenkinek több, mint 21 teszt: sikertelen")


def dontetlen_egyenlo_lap():
    jatekos = [10, 5]
    gep = [8, 7]
    vart_eredmeny = "kevesebb mint 21 mindkettő, de ugyanannyi lapból"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("kevesebb mint 21 mindkettő, de ugyanannyi lapból teszt: sikeres")
    else:
        print("kevesebb mint 21 mindkettő, de ugyanannyi lapból teszt: sikertelen")

#jatekos veszt
def vesztes_jatekos_tobb_lap_mint_21():
    gep = [10, 6]
    jatekos = [10, 10, 3]
    vart_eredmeny = "több lap mint 21: a játékos vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("több mint 21 játékos vesztett teszt: sikeres")
    else:
        print("több mint 21 játékos vesztett teszt: sikertelen")

def vesztes_jatekos_egyenlo_pont_tobb_lap():
    gep = [10, 5]
    jatekos = [10, 5, 4]
    vart_eredmeny = "19 pont, több lap teszt: játékos vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de több lap teszt játékos veszt: sikeres")
    else:
        print("19 pont, de több lap teszt játékos veszt: sikertelen")



def vesztes_jatekos_egyenlo_pont_kevesebb_lap():
    gep = [10, 5, 4]
    jatekos = [10, 9]
    vart_eredmeny = "19 pont, kevesebb lap teszt: játékos vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de kevesebb lap teszt játékos veszt: sikeres")
    else:
        print("19 pont, de kevesebb lap teszt játékos veszt: sikertelen")


#gep veszt
def vesztes_gep_tobb_lap_mint_21():
    gep = [10, 10, 2]
    jatekos = [10, 6]
    vart_eredmeny = "több mint 21: gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("több mint 21 gép vesztett teszt: sikeres")
    else:
        print("több mint 21 gép vesztett teszt: siertelen")


def vesztes_gep_egyenlo_pont_tobb_lap():
    gep = [10, 5, 4]
    jatekos = [10, 4]
    vart_eredmeny = "19 pont,de több lap teszt: gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19pont, de több lap teszt gép veszt: sikeres")
    else:
        print("19 pont, de több lap teszt gép veszt: sikertelen")

def vesztes_gep_egyenlo_pont_kevesebb_lap():
    gep = [10, 9]
    jatekos = [10, 5]
    vart_eredmeny = "19 pont,de kevesebb lap teszt: gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de kevesebb lap teszt gép veszt: sikeres")
    else:
        print("19 pont, de kevesebb lap teszt gép veszt: sikertelen")



#jatekos nyert
def nyert_jatekos_pont_21():
    gep = [10, 10]
    jatekos = [10, 10, 1]
    vart_eredmeny = "pont 21: játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("pont21 játékos nyer teszt: sikeres")
    else:
        print("pont21 játékos nyer teszt: sikertelen")

def nyert_jatekos_pont_19_lap_tobb():
    gep = [10, 1]
    jatekos = [10, 5, 4]
    vart_eredmeny = "19 pont, de több lap teszt: játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de több lap teszt játékos nyer: sikeres")
    else:
        print("19 pont, de több lap teszt játékos nyer: sikertelen")

def nyert_jatekos_pont_19_lap_kevesebb():
    gep = [10, 4, 3]
    jatekos = [10, 9]
    vart_eredmeny = "19 pont, de kevesebb lap teszt: játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de kevesebb lap teszt játékos nyer: sikeres")
    else:
        print("19 pont, de kevesebb lap teszt játékos nyer: sikertelen")


#nyert gep
def  nyert_gep_pont_21():
    gep = [10, 10, 1]
    jatekos = [10, 10]
    vart_eredmeny = "pont21: gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("pont 21 gép nyer teszt: sikeres")
    else:
        print("pont 21 gép nyer teszt: sikertelen")


def nyert_gep_pont_19_lap_tobb():
    gep = [10, 1, 8]
    jatekos = [10, 8]
    vart_eredmeny = "19 pont, de több lap teszt: gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de több lap teszt gép nyer: sikeres")
    else:
        print("19 pont, de több lap teszt gép nyer: sikertelen")



def nyert_gep_pont_19_lap_kevesebb():
    gep = [10, 9]
    jatekos = [10, 3, 4]
    vart_eredmeny = "19 pont, de kevesebb lap teszt: gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de kevesebb lap teszt gép nyer: sikeres")
    else:
        print("19 pont, de kevesebb lap teszt gép nyer: sikertelen")


tesztek()

