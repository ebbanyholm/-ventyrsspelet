from random import randint

class Item():

    def __init__(self, styrka, namn):
        self.styrka = styrka
        self.namn = namn
        
    def skriv(self):
        print(self.namn)
        print(self.styrka)

svärd = Item(4, 'svärd')
pilbåge = Item(2, 'pilbåge')
kniv = Item(3, 'kniv')
yxa = Item(3, 'yxa')
sköld = Item(2, 'sköld')
kofot = Item(4, 'kofot')
glasbit = Item(3, 'glasbit')
sten = Item(1, 'sten')
halsband = Item(2, 'halsband')

class Player():

    def __init__(self):
        self.stark = 9
        self.hp = 100
        self.lvl = 1
        self.inventory = []
    
    def stats(self):
        print("")
        print(f"Du har {self.hp} hp kvar")
        print(f"Din styrka är {self.stark}")
        print(f"Din lvl är {self.lvl}")
        print("")

    def styrke_bonus(self):
        self.stark = 9 + self.lvl

        if svärd in self.inventory:
            self.stark += 4
        
        if pilbåge in self.inventory:
            self.stark += 2

        if kniv in self.inventory:
            self.stark += 3
        
        if yxa in self.inventory:
            self.stark += 3
        
        if sköld in self.inventory:
            self.stark += 2
            
        if kofot in self.inventory:
            self.stark += 4
        
        

    def visa_inventory(self):
        if svärd in self.inventory:
            print("svärd: styrka 4")
        if pilbåge in self.inventory:
            print("pilbåge: styrka 2")
        if kniv in self.inventory:
            print("kniv: styrka 3")
            


class Player():

    def __init__(self):
        self.stark = 9
        self.hp = 100
        self.lvl = 1
        self.inventory = []
    
    def stats(self):
        print("")
        print(f"Du har {self.hp} hp kvar")
        print(f"Din styrka är {self.stark}")
        print(f"Din lvl är {self.lvl}")
        print("")

    def styrke_bonus(self):
        self.stark = 9 + self.lvl

        if svärd in self.inventory:
            self.stark += 4
        
        if pilbåge in self.inventory:
            self.stark += 2

        if kniv in self.inventory:
            self.stark += 3
   
    def visa_inventory(self):
        if svärd in self.inventory:
            print("svärd: styrka 4")
        if pilbåge in self.inventory:
            print("pilbåge: styrka 2")
        if kniv in self.inventory:
            print("kniv: styrka 3")

                             
        

    def bakom_dörr(self):
       def visa_inventory():
        if svärd in self.inventory:
            print("svärd: styrka 4")
        if pilbåge in self.inventory:
            print("pilbåge: styrka 2")
        if kniv in self.inventory:
            print("kniv: styrka 3")

        def inventory_fullt():
            print("ditt inventory är fullt..")
            print("vill du ersätta något?")
            print("ja [j]")                              
            print("nej [n]")    

        def ersätta():
            vilken = input("vilken vill du ersätta? 1,2 eller 3? -->")
            if vilken == 1:
                self.inventory.pop(0)
            elif vilken == 2:
                self.inventory.pop(1)
            elif vilken == 3:
                self.inventory.pop(2)

            
        skit = randint(1, 9)
        i = 0 
        if skit in {1, 9}:
            
            print("Yey, en skattkista!!")

            while True:
                slumpat_föremål = 1
                        
                if slumpat_föremål == 1:
                    if svärd in self.inventory:
                        continue
                    else:
                        print("Du fick ett svärd")
                        if i == 3: 
                            inventory_fullt()
                            valet=input("->")
                            if valet == "j":
                                visa_inventory()
                                ersätta()
                                self.inventory.append(svärd)
                            elif valet == "n":
                                break
                        else:
                            print("Vill du lägga till den i dit inventory?")
                            print("")
                            print("Det här är ditt inventory just nu:")   #som funktion
                            visa_inventory() #valen


                
                elif slumpat_föremål == 2:
                    if pilbåge in self.inventory:
                        continue
                    else:
                        print("Du fick en pilbåge")
                        print("Vill du lägga till den i dit inventory?")
                        print("")
                        print("Det här är ditt inventory just nu:")
                        #visa_inventory(self)
                        if svärd in self.inventory:
                            print("svärd: styrka 4")
                        if pilbåge in self.inventory:
                            print("pilbåge: styrka 2")
                        if kniv in self.inventory:
                            print("kniv: styrka 3")
                        print("")
                        
                        ditt_val = input("Ja [j] eller Nej [n]? ->")
                        if ditt_val == "j":
                            self.inventory.append(pilbåge)
                            break
                        elif ditt_val == "n":
                            break
                        
                elif slumpat_föremål == 3:
                    if kniv in self.inventory:
                        continue 
                    else:
                        print("Du fick en kniv")
                        print("Vill du lägga till den i dit inventory?")
                        print("")
                        print("Det här är ditt inventory just nu:")
                        #visa_inventory(self)
                        if svärd in self.inventory:
                            print("svärd: styrka 4")
                        if pilbåge in self.inventory:
                            print("pilbåge: styrka 2")
                        if kniv in self.inventory:
                            print("kniv: styrka 3")
                        print("")
                        
                        ditt_val = input("Ja [j] eller Nej [n]? ->")
                        if ditt_val == "j":
                            self.inventory.append(kniv)
                            break
                        elif ditt_val == "n":
                            break
                        
        if skit > 40:
            i = randint(1, 6)
            
            if i == 1:
                print("Du går in i en restaurangen")
                print("Ett bord fyliger rätt emot dig")
                print()
                print("Det blir svart")
                print("Du förlorade fyra hälsopoäng")
                self.hp -= 4
                print()
                print("Efter en stund vaknar du upp igen")
                print()
                print("Resturangen är nu borta")
                print("Du är tillbaka i korridåren igen")

            if i == 2:
                antal_knivar = randint(1, 5)
                print("Du gick på en fallucka")
                print()
                print(f"Under ditt fall stöter du på {antal_knivar} knivar")
                print(f"Du förlorade {antal_knivar} hälsopoäng")
                self.hp -= antal_knivar
                print()
                print("Du lander sedan på en madrass och är redo för ditt nästa val")
            
            if i == 3:
                print("Du gick in i en glas vägg och fick en ")
                print("lätt hjärnskakning och en bruten näsa")
                print("Du förlorade 2 hälsopoäng")
                self.hp -= 2
                print("Du är nu redo för ditt nästa val.")

            if i == 4:
                print("Du stöter på en tom dörr.")
                print("På din väg genom dörren stukar du din högra fot")
                print("och förlorar 1 hälsopoäng")
                self.hp -= 1  
                print("Du är nu redo för ditt nästa val.")

            if i == 5:
                print("Du stöter på en tom dörr.")
                print("På din väg genom dörren stukar du din vänstra fot")
                print("och förlorar 1 hälsopoäng")
                self.hp -= 1  
                print("Du är nu redo för ditt nästa val.")

            if i == 6:
                print("Du stäcker ut din hand redo att öppna dörren framför dig.")
                print("När din hud kommer i kontakt med dörrhantaget börjar du SssKKaKka som aldirg för.")
                print("Du har fått en stöt och du förlorar 1 hälsopoäng!")
                self.hp -= 1  
                print()
                print("Efter en stund av skakande reser du dig, går igenom dörren vars handtag")
                print("inte längre är strömförande, och är redo för dit nästa val")
                   
        if skit < 25:
        
            if self.lvl < 5:
                m_styrka = randint(1, 15)
                m_liv = randint(1, 15)
                
            elif self.stark in {5, 6, 7, 8, 9}:
                m_styrka = randint(10, 20)
                m_liv = randint(10, 20)
                
            else: 
                m_styrka = randint(25, 35)
                m_liv = randint(25, 35)
            
            def m_meny():
                print("")
                print("vad vill du göra?")
                print("")
                print("Slå till             -> a")
                print("Kolla styrka och liv -> i")
                print("Spring!              -> s")

            while True:
                m_meny()
                val = input("-> ")
                
                if val == "a":
                    strid = randint(1, 3)
        
                    if strid in (1, 2):
                        print("träffade monstret")
                        m_liv -= self.stark

                    else:
                        print("missade moonstret")
                
                if val == "i":
                    print("")
                    print(f"Du har {self.stark} i styrka och {self.hp} i liv")
                    print(f"Monstret har {m_styrka} i styka och {m_liv} i liv")
                    print("")
                    continue

                if val == "s":
                    spring = randint(1, 3)
                    if self.stark < m_styrka:
                        if spring == 1:
                            print("Du sprang iväg")
                            print("tillbaka til slottet")
                            break
                    
                        else:
                            print("Du misslyckades med att springa iväg")

                    if self.stark > m_styrka:
                        if spring in {1, 2}:
                            print("Du sprang iväg")
                            print("tillbaka till slottet")
                            break

                        else:
                            print("Du misslyckade med att springa iväg")

                if m_liv <= 0:
                    print("Monstret blev ledset och sprang iväg")
                    print("Du lvlade upp!")
                    self.lvl += 1
                    print("tillbaka till slottet")
                    break

                ont = randint(1, 3)
                if ont in {1, 2}:
                    print("monstret missade")

                elif ont == 3:
                    print("Monstret skadade dig")
                    self.hp -= m_styrka
            
                if self.hp <= 0:
                    break
                    
        def dö(self):
            if self.hp <= 0:
                print("Du dog och förlorade alla dina hälsopoäng")
            
        def vinna(self): 
            if self.lvl >= 15:
                print("Wooooooo")
                print("Du vann!!!!!") 
                          

                


                

           
def meny():
    print("")
    print("")
    print("Vad vill du göra?")
    print("kolla inventory      -> i")
    print("Kolla stats          -> s")
    print("Gå frammåt i slottet -> d")
    print("")

#huvudprogram
random_dude = Player()

while True:
    meny()
    random_dude.styrke_bonus()
    val = input("Ditt val -> ")

    if val == "i":
        random_dude.visa_inventory()
        input("för att stänga, klicka på enter")

    if val == "s":
        random_dude.stats()
        input("för att stänga, klicka på enter")

    if val == "d":
       random_dude.bakom_dörr()
    