from random import randint

class Item():

    def __init__(self, styrka, namn):
        self.styrka = styrka
        self.namn = namn

svärd = Item(4, 'svärd')
pilbåge = Item(2)
kniv = Item(3)
flöjt = Item(0) #Tar 3 platser i inventoryt
sköld = Item(2)
yxa = Item(3)
kofot = Item(4)
pall = Item(2)
glasbit = Item(3)
sten = Item(1)
tavelram = Item(1)
halsband= Item(2)
ringar = Item(1)
guldbägare = Item(5)

class player():

    def __init__(self):
        self.stark = 10
        self.hp = 100
        self.lvl = 1
        self.Item = []

    #Def behöver fixas senare
    def inventory(self):
        for i in self.Item:
            print(i.namn)

    
    def stats(self):
        print("")
        print(f"Du har {self.hp} hp kvar")
        print(f"Din styrka är {self.stark}")
        print(f"Din lvl är {self.lvl}")
        print("")

    def skattkista(self):
        print(" ")
        Strengthboost = randint(1,17)
        
        if Strengthboost == 1:
            self.Item.append(svärd)
        elif Strengthboost == 2:
            self.Item.append(pilbåge)
        elif Strengthboost == 3:
            self.Item.append(kniv)
        elif Strengthboost == 4:
            self.Item.append(flöjt)
        elif Strengthboost == 5:
            self.Item.append(sköld)


    #Saker som kanske ska vara i en annan funktion som täcker allt

    def fälla(self):
        i = randint(1, 6)
        antal = randint(1, 5)
        
        if i == 1:
            print("Du går in i en restaurangen")
            print("Ett bord fyliger rätt emot dig")
            print()
            print("Det blir svart")
            print("Du förlorade fyra hälsopoäng")
            self.hp -= 4
            print()
            print("efter en stund vaknar du upp igen")
            print("Resturangen är nu borta")
            print("Du är tillbaka i korridåren igen")
           
            self.hp -= 4

        if i == 2:
            print("Du gick på en fallucka")
            print()
            print(f"Under ditt fall stöter du på {antal} knivar")
            print(f"Du förlorade {antal} hälsopoäng")
            print()
            print("Du lander sedan på en madrass och är redo för ditt nästa val")
            self.hp -= antal
            
        if i == 3:
            print("Du gick in i en glas vägg och fick en ")
            print("lätt hjärnskakning och en bruten näsa")
            print("Du förlorade 2 hälsopoäng")
           
            self.hp -= 2

        if i == 4:
            print("Du stöter på en tom dörr.")
            print("På din väg genom dörren stukar du din högra fot")
            print("och förlorar 1 hälsopoäng")
           
            self.hp -= 1  

        if i == 5:
            print("Du stöter på en tom dörr.")
            print("På din väg genom dörren stukar du din vänstra fot")
            print("och förlorar 1 hälsopoäng")
           
            self.hp -= 1  

        if i == 6:
            print("Du stäcker ut din hand redo att öppna dörren framför dig.")
            print("När din hund kommer i kontakt med dörrhantaget börjar du SssKKaKka som aldirg för.")
            print("Du har fått en stöt och du förlorar 1 hälsopoäng!")
            self.hp -= 1  
            print("Efter en stund av skakande reser du dig upp igen redo för ditt nästa val.")
           
            
        
            

    
    def monster(self):
        
        if self.lvl < 5:
            m_styrka = randint(1, 15)
            
        elif self.stark in {6, 7, 8, 9}:
            m_styrka = randint(10, 20)
            
        else: 
            m_styrka = randint(25, 35)


        if self.stark < m_styrka:
            print("monstret avlivar dig")
            self.hp =- m_styrka
            input("klicka på 'enter' för att fortsätta")
            
            
        elif self.stark == m_styrka:
            print("Ni tittar stelt på varandra")
            
        else:
            print("Monstret bjuder dig på en pinã colada i slottets privata pool")
            self.lvl =+ 1
            input("Klicka på 'enter' för att fortsätta")
        
        
            


    


def meny():
    print("")
    print("Vad vill du göra?")
    print("kolla inventory      -> i")
    print("Kolla stats          -> s")
    print("Gå frammåt i slottet -> d")
    print("")

def dörr_val():
    print("")
    print("Framför dig har du tre dörrar")




random_dude = player()

while True:
    meny()
    val = input("Ditt val -> ")

    if val == "i":
        random_dude.inventory()
        input("för att stänga, klicka på enter")

    if val == "s":
        random_dude.stats()
        input("för att stänga, klicka på enter")

    if val == "d":
        dörr_val()
        input("Vilken dörr vill du gå in i -> ")
        skit = randint(1, 50)

        #Kan hamna i en funktion

        #Monster
        if skit < 25:
            print("Ett monsteeeer!!!")
            random_dude.monster()
        
        #Skattkista
        if skit in {26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40}:
            print("Yay, en skattkista!!")
            random_dude.skattkista()

        #fälla
        if skit > 40:
            print("")
            random_dude.fälla()       