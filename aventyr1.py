from random import randint

class Item():

    def __init__(self, styrka, namn):
        self.styrka = styrka
        self.namn = namn

svärd = Item(4, 'svärd')
pilbåge = Item(2, 'pilbåge')
kniv = Item(3, 'kniv')
yxa = Item(3, 'yxa')
sköld = Item(2, 'sköld')
kofot = Item(4, 'kofot')
glasbit = Item(3, 'glasbit')
sten = Item(1, 'sten')
halsband = Item(2, 'halsband')

class player():

    def __init__(self):
        self.stark = 9
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

    def styrke_bonus(self):
        self.stark = 9 + self.lvl

        if svärd in self.Item:
            self.stark += 4
        
        if pilbåge in self.Item:
            self.stark += 2

        if kniv in self.Item:
            self.stark +=3

        if yxa in self.Item:
            self.stark +=3

        if sköld in self.Item:
            self.strak += 2

        if kofot in self.Item:
            self.stark += 4

        if glasbit in self.Item:
            self.stark += 3
            
        if sten in self.Item:
            self.stark += 1

        if halsband in self.Item:
            self.stark += 2
            
        

    def bakom_dörr(self):
        skit = randint(1, 50) 
        if skit in {26, 40}:
            print("Yay, en skattkista!!")

            while True:
                slumpad_siffra = randint(1,9)
                print("du fick en grej.")
            
                if slumpad_siffra == 1:
                    if svärd in self.Item:
                        continue
                    else:
                        self.Item.append(svärd)
                        break
                
                elif slumpad_siffra == 2:
                    if pilbåge in self.Item:
                        continue
                    else:
                        self.Item.append(pilbåge)
                        break
                        
                elif slumpad_siffra == 3:
                    if kniv in self.Item:
                        continue 
                    else:
                        self.Item.append(kniv)
                        break
                
                elif slumpad_siffra == 4:
                    if yxa in self.Item:
                        continue
                    else:
                        self.Item.append(yxa)
                        break

                elif slumpad_siffra == 5:
                    if sköld in self.Item:
                        continue
                    else:
                        self.Item.append(sköld)
                        break
                
                elif slumpad_siffra == 6:
                    if kofot in self.Item:
                        continue
                    else:
                        self.Item.append(kofot)
                        break
                            
                elif slumpad_siffra == 7:
                    if glasbit in self.Item:
                        continue
                    else:
                        self.Item.append(glasbit)
                        break
                        
                elif slumpad_siffra == 8:
                    if sten in self.Item:
                        continue
                    else:
                        self.Item.append(sten)
                        break
                        
                elif slumpad_siffra == 9:
                    if halsband in self.Item:
                        continue
                    else:
                        self.Item.append(halsband)
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
                
            elif self.stark in {5, 6, 7, 8, 9}:
                m_styrka = randint(10, 20)
                
            else: 
                m_styrka = randint(25, 35)


            if self.stark < m_styrka:
                print("Du slåss mot ett läskigt monster")
                print(f"du förlorar {m_styrka} hälsopoäng")
                self.hp -= m_styrka
                input("klicka på 'enter' för att fortsätta")
                
                
            elif self.stark == m_styrka:
                print("Ni tittar stelt på varandra")
                
            else:
                print("du slår ner monstret och går genom dörren")
                print("du går upp en level")
                self.lvl += 1
                input("Klicka på 'enter' för att fortsätta")
            
            
                


    


def meny():
    print("")
    print("Vad vill du göra?")
    print("kolla inventory      -> i")
    print("Kolla stats          -> s")
    print("Gå frammåt i slottet -> d")
    print("")






random_dude = player()

while True:
    meny()
    random_dude.styrke_bonus()
    val = input("Ditt val -> ")

    if val == "i":
        random_dude.inventory()
        input("för att stänga, klicka på enter")

    if val == "s":
        random_dude.stats()
        input("för att stänga, klicka på enter")

    if val == "d":
       random_dude.bakom_dörr()
              