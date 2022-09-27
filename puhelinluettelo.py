class Henkilo:

    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__osoite = ""
        self.__numerot = []
    
    def nimi(self):
        return self.__nimi
    
    def numerot(self):
        return self.__numerot
    
    def osoite(self):
        if self.__osoite == "":
            return None
        return self.__osoite
    
    def lisaa_numero(self, numero: str):
        self.__numerot.append(numero)
    
    def lisaa_osoite(self, __osoite: str):
        self.__osoite = __osoite
    


class Puhelinluettelo:

    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_numero(numero)
    
    def lisaa_osoite(self, nimi: str, osoite: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_osoite(osoite)

    def hae_tiedot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi].numerot(), self.__henkilot[nimi].osoite()

    def kaikki_tiedot(self):
        return self.__henkilot



class PuhelinluetteloSovellus:
    
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")

    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)
    
    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        osoite = input("Osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

    def haku(self):
        nimi = input("nimi: ")
        tiedot = self.__luettelo.hae_tiedot(nimi)
        if tiedot == None:
            print("numero ei tiedossa")
            print("osoite ei tiedossa") 
            return 
        if tiedot[0] == []:
            print("numero ei tiedossa")
        else:
            for numero in tiedot[0]:
                print(numero)
        if tiedot[1] == None:
            print("osoite ei tiedossa")
        else:
            print(tiedot[1])

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()

sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
