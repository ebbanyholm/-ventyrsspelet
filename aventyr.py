# ---------------------------------------------------------- ÄVENTYRSPELET -------------------------------------------------------- #

from random import randint

# ---------------------------------------------------------- KLASSEN PLAYER -------------------------------------------------------- #

class Player():
    def __init__(self):
        self.stark = 9
        self.hp = 100                 #kopplar spelaren med dess styrka, lvl, hp och inventory
        self.lvl = 1
        self.inventory = []
    
    def stats(self):
        print("")
        print(f"Du har {self.hp} hp kvar")
        print(f"Din styrka är {self.stark}")
        print(f"Din lvl är {self.lvl}")
        print("")

    def styrke_bonus(self):                 #ger spelaren styrke bonus beroende på inventoryt
        self.stark = 9 + self.lvl
        if "svärd_4" in self.inventory:
            self.stark += 4
        if "pilbåge_2" in self.inventory:
            self.stark += 2
        if "kniv_3" in self.inventory:
            self.stark += 3
        if "sköld_2" in self.inventory:
            self.stark += 2
        if "yxa_3" in self.inventory:
            self.stark += 3
      
    def visa_inventory(self):
        if "svärd_4" in self.inventory:
            print("svärd: styrka 4")
        if "pilbåge_2" in self.inventory:
            print("pilbåge: styrka 2")
        if "kniv_3" in self.inventory:
            print("kniv: styrka 3")
        if "sköld_2" in self.inventory:
            print("sköld: styrka 2")
        if "yxa_3" in self.inventory:
            print("yxa: styrka 3")

    # ------------------------------------------------------- BAKOM DÖRR ------------------------------------------------------- #

    def bakom_dörr(self):    
        
        val_av_dörr = input("Vilken dörr vill du gå in i? [1],[2] eller[3]? -->")
        print()
        
        if val_av_dörr in {"1","2","3"}:

            dörrens_innehåll =randint(1,9)

            def inventory_fullt():
                print("ditt inventory är fullt..")
                print("vill du ersätta något?")
                print("ja [w]")                              
                print("nej [d]")    

            def ersätta():
                while True:
                    vilken = int(input("vilken vill du ersätta? 1,2 eller 3? -->"))
                    if vilken == 1:
                        self.inventory.pop(0)
                        break
                    elif vilken == 2:
                        self.inventory.pop(1)
                        break
                    elif vilken == 3:
                        self.inventory.pop(2)
                        break

                    else:
                        print("felaktig input")
                        continue
            
            def visa_inventory_kista():
                print("FÖREMÅL_STYRKA")
                print(self.inventory)
                
            

            
            # -------------------------------------- skattkista --------------------------------------#
            if dörrens_innehåll in {1,2,3}:
                print("Yey, en skattkista!!")

                while True:
                        
                    slumpat_föremål = randint(1,5)
                    antal_föremål_inventory = len(self.inventory)
                
                    if slumpat_föremål == 1:
                        if "svärd_4" in self.inventory:
                            continue
                        else:
                            print("Du fick ett svärd")
                            if antal_föremål_inventory == 3: 
                                inventory_fullt()
                                valet=input("->")
                                if valet == "w":
                                    visa_inventory_kista()
                                    ersätta()
                                    self.inventory.append("svärd_4")
                                    break
                                elif valet == "d":
                                    break
                            else:
                                print("Vill du lägga till det i ditt inventory?")
                                print("")
                                print("Det här är ditt inventory just nu:") 
                                visa_inventory_kista()
                                valet=input("ja [w], Nej [d]->")
                                if valet == "w":
                                    self.inventory.append("svärd_4")
                                elif valet == "d":
                                    break   
                                break

                    if slumpat_föremål == 2:
                        if "pilbåge_2" in self.inventory:

                            continue
                        else:
                            print("Du fick en pilbåge")
                            if antal_föremål_inventory == 3: 
                                inventory_fullt()
                                valet=input("->")
                                if valet == "w":
                                    visa_inventory_kista()
                                    ersätta()
                                    self.inventory.append("pilbåge_2")
                                    break
                                elif valet == "d":
                                    break
                            else:
                                print("Vill du lägga till den i ditt inventory?")
                                print("")
                                print("Det här är ditt inventory just nu:") 
                                visa_inventory_kista()
                                valet=input("ja [w], Nej [d]->")
                                if valet == "w":
                                    self.inventory.append("svärd_2")
                                elif valet == "d":
                                    break   
                                break
                            
                    if slumpat_föremål == 3:
                        if "kniv_3" in self.inventory:
                            continue
                        else:
                            print("Du fick en kniv")
                            if antal_föremål_inventory == 3: 
                                inventory_fullt()
                                valet=input("->")
                                if valet == "w":
                                    visa_inventory_kista()
                                    ersätta()
                                    self.inventory.append("kniv_3")
                                    break
                                elif valet == "d":
                                    break
                            else:
                                print("Vill du lägga till den i ditt inventory?")
                                print("")
                                print("Det här är ditt inventory just nu:") 
                                visa_inventory_kista()
                                valet=input("ja [w], Nej [d]->")
                                if valet == "w":
                                    self.inventory.append("kniv_3")
                                elif valet == "d":
                                    break   
                                break
                            
                    if slumpat_föremål == 4:
                        if "sköld_2" in self.inventory:
                            continue
                        else:
                            print("Du fick en sköld")
                            if antal_föremål_inventory == 3: 
                                inventory_fullt()
                                valet=input("->")
                                if valet == "w":
                                    visa_inventory_kista()
                                    ersätta()
                                    self.inventory.append("sköld_2")
                                    break
                                elif valet == "d":
                                    break
                            else:
                                print("Vill du lägga till den i ditt inventory?")
                                print("")
                                print("Det här är ditt inventory just nu:") 
                                visa_inventory_kista()
                                valet=input("ja [w], Nej [d]->")
                                if valet == "w":
                                    self.inventory.append("sköld_2")
                                elif valet == "d":
                                    break   
                                break
                            
                    if slumpat_föremål == 5:
                        if "yxa_3" in self.inventory:
                            continue
                        else:
                            print("Du fick en yxa")
                            if antal_föremål_inventory == 3: 
                                inventory_fullt()
                                valet=input("->")
                                if valet == "w":
                                    visa_inventory_kista()
                                    ersätta()
                                    self.inventory.append("yxa_3")
                                    break
                                elif valet == "d":
                                    break
                            else:
                                print("Vill du lägga till den i ditt inventory?")
                                print("")
                                print("Det här är ditt inventory just nu:") 
                                visa_inventory_kista()
                                valet=input("ja [w], Nej [d]->")
                                if valet == "w":
                                    self.inventory.append("yxa_3")
                                elif valet == "d":
                                    break   
                                break
                            
                    if slumpat_föremål == 6:
                        hp_bonus = randint(5, 40)
                        print("Du hittade lite liv!")
                        self.hp += hp_bonus
                        print(f"Du känner dig {hp_bonus} hälsopoäng friskare ")
                        break
                    

                



            # ------------------------------------------ fälla ---------------------------------------#                
            if dörrens_innehåll in {4,5,6}:
                i = randint(1, 6)
                
                if i == 1:
                    print("Du går in i en restaurangen")
                    print("Ett bord flyger rätt emot dig")
                    print()
                    print("Det blir svart")
                    print("Du förlorade fyra hälsopoäng")
                    self.hp -= 4
                    print()
                    print("Efter en stund vaknar du upp igen")
                    print()
                    print("Resturangen är nu borta")
                    print("Du är tillbaka i korridoren igen")

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
                    print("Du sträcker ut din hand redo att öppna dörren framför dig.")
                    print("När din hud kommer i kontakt med dörrhantaget börjar du SssKKaKka som aldrig för.")
                    print("Du har fått en stöt och du förlorar 1 hälsopoäng!")
                    self.hp -= 1  
                    print()
                    print("Efter en stund av skakande reser du dig, går igenom dörren vars handtag")
                    print("inte längre är strömförande, och är redo för ditt nästa val")
                    

                    
            # -------------------------------------- monster -------------------------------------- #
            if dörrens_innehåll in {7,8,9}:
            
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
                    print("Vad vill du göra?")
                    print("")
                    print("Slå till                   -> a")
                    print("Spring!                    -> d")
                    print("Visa styrka och hälsopoäng -> q")

                while True:
                    m_meny()
                    val = input("-> ")
                    
                    if val == "a":
                        strid = randint(1, 3)
            
                        if strid in (1, 2):
                            print()
                            print("träffade monstret")
                            m_liv -= self.stark

                        else:
                            print()
                            print("missade monstret")
                    
                    if val == "q":
                        print("")
                        print(f"Du har {self.stark} i styrka och {self.hp} i liv")
                        print(f"Monstret har {m_styrka} i styka och {m_liv} i liv")
                        print("")
                        continue

                    if val == "d":
                        spring = randint(1, 3)
                        if self.stark < m_styrka:
                            if spring == 1:
                                print()
                                print("Du sprang iväg")
                                print("Du är nu redo för ditt nästa val")
                                break
                        
                            else:
                                print()
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

                    m_slag_resultat = randint(1, 3)
                    if m_slag_resultat in {1, 2}:
                        print("monstret missade")

                    elif m_slag_resultat == 3:
                        print("Monstret skadade dig")
                        self.hp -= m_styrka
                
                    if self.hp <= 0:
                        break
        
        else:
            print("Felaktig inmating")
            
                   
    def dö(self):
        print("Du dog och förlorade alla dina hälsopoäng")
        print(f"Du kom till lvl {self.lvl}")
                
            
    def vinna(self):
        print("Wooooooo")
        print("Du vann!!!!!")
        print(f"{self.lvl} hälsopoäng återstår.")

    def fusknapp(self):
        self.lvl += 15

    def fusknapp_2(self):
        self.hp -= 100                          

                
def meny():
    print("")
    print("")
    print("Vad vill du göra?")
    print("Gå frammåt i slottet -> w")
    print("Kolla stats          -> q")
    print("kolla inventory      -> e")
    print("")

#huvudprogram
random_dude = Player()

while True:
    meny()
    random_dude.styrke_bonus()
    val = input("Ditt val -> ")

    if val == "e":
        random_dude.visa_inventory()
        input("för att stänga, klicka på enter")

    if val == "q":
        random_dude.stats()
        input("för att stänga, klicka på enter")
        
    if val == "w":
       random_dude.bakom_dörr()

    if val == "p":
        random_dude.fusknapp()
        
    if val == "å":
        random_dude.fusknapp_2()

    if random_dude.hp <= 0:
        random_dude.dö()
        break

    if random_dude.lvl >= 15:
        random_dude.vinna()
        break