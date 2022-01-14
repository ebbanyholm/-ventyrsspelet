# ---------------------------------------------------------- ÄVENTYRSPELET -------------------------------------------------------- #

from random import randint

# ---------------------------------------------------------- KLASSEN PLAYER -------------------------------------------------------- #
class Player():
    def __init__(self):

        """
        Ger spelaren egenskaperna styska, lvl, hp och inventory.
        """
        self.styrka = 9             
        self.hp = 100                 
        self.lvl = 1
        self.inventory = []
    
    def stats(self):
        """
        Skriver ut spelarens stats.
        """
        print("")
        print(f"Du har {self.hp} hp kvar")            
        print(f"Din styrka är {self.styrka}")
        print(f"Din lvl är {self.lvl}")
        print("")

    def styrke_bonus(self):    
        """
        Ger spelaren styrke bonusar beroende på vilken lvl den är i och vad den
        har i sitt inventory.
        """        
        self.styrka = 9 + self.lvl
        if "svärd_4" in self.inventory:
            self.styrka += 4             
        if "pilbåge_2" in self.inventory:
            self.styrka += 2
        if "kniv_3" in self.inventory:
            self.styrka += 3
        if "sköld_2" in self.inventory:
            self.styrka += 2
        if "yxa_3" in self.inventory:
            self.styrka += 3
      
    def visa_inventory(self):
        """
        Skriver ut innehållet i spelarens inventory fint.
        """
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

    # ------------------------------------------------- B A K O M   D Ö R R ------------------------------------------------------- #

    def bakom_dörr(self):    ###################
        """
        Startar alla händelser som sker efter att spelaren har val att gå framåt i slottet.
        """
        val_av_dörr = input("Vilken dörr vill du gå in i? [1],[2] eller[3]? -->")
        print()
        
        if val_av_dörr in {"1","2","3"}:

            dörrens_innehåll =randint(1,3)

            def inventory_fullt(): 
                """
                Frågar spelaren om den vill ersätta något i sitt inventory med de nya föremålet.
                Kommer endast upp då inventoryt är fullt.
                """
                print('''
                Ditt inventory är fullt..")
                Vill du ersätta något?

                ja [w]                              
                nej [d]
                ''')  

            def visa_inventory_kista():
                """
                Skriver ut innehållet i inventoryt när spelaren får ett föremål och om spelaren vill ersätta något.
                """       
                print("föremål_styrka")
                print(self.inventory)

            def ta_bort():  
                """
                Tar bort de föremålet som spelaren vill ersätta med de nya föremålet.
                """ 
                while True:         
                    vilken = input("vilken vill du ersätta? 1,2 eller 3? -->")
                    if vilken == "1":
                        self.inventory.pop(0)
                        break
                    elif vilken == "2":
                        self.inventory.pop(1)
                        break
                    elif vilken == "3":
                        self.inventory.pop(2)
                        break

                    else:
                        print("felaktig input")
                        continue
            
            def redo_för_val():
                """
                Medelar spelaren om att den är redo för sitt nästa val.
                """
                print("Du är nu redo för ditt nästa val.")
     
            # -------------------------------------- skattkista --------------------------------------#
            if dörrens_innehåll == 1:
                print("Yey, en skattkista!!")

                while True:
                        
                    slumpat_föremål = randint(1,5)
                    antal_föremål_inventory = len(self.inventory)
                
                    if slumpat_föremål == 1:
                        if "svärd_4" in self.inventory:
                            continue
                        else:
                            print("Du fick ett svärd ⚔")
                            if antal_föremål_inventory == 3: 
                                inventory_fullt()
                                valet=input("->")
                                if valet == "w":
                                    visa_inventory_kista()
                                    ta_bort()
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
                            print("Du fick en pilbåge 🏹")
                            if antal_föremål_inventory == 3: 
                                inventory_fullt()
                                valet=input("->")
                                if valet == "w":
                                    visa_inventory_kista()
                                    ta_bort()
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
                            print("Du fick en kniv 🔪")
                            if antal_föremål_inventory == 3: 
                                inventory_fullt()
                                valet=input("->")
                                if valet == "w":
                                    visa_inventory_kista()
                                    ta_bort()
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
                            print("Du fick en sköld 🛡")
                            if antal_föremål_inventory == 3: 
                                inventory_fullt()
                                valet=input("->")
                                if valet == "w":
                                    visa_inventory_kista()
                                    ta_bort()
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
                            print("Du fick en yxa 🪓")
                            if antal_föremål_inventory == 3: 
                                inventory_fullt()
                                valet=input("->")
                                if valet == "w":
                                    visa_inventory_kista()
                                    ta_bort()
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
            if dörrens_innehåll == 2:
                i = randint(1, 6)
                
                if i == 1:
                    print('''
                        Du går in i en restaurangen. Ett bord flyger rätt emot dig. 
                    
                        Det blir svart....
                        
                        Du förlorade fyra hälsopoäng.
                    
                        Efter en stund vaknar du upp igen..
                        
                        Resturangen är nu borta..
                    
                        ... tillbaka i korridoren ...
                    
                    ''')
                    
                    self.hp -= 4
                    redo_för_val()

                if i == 2:
                    antal_knivar = randint(1, 5)
                    print(f'''
                        Du gick på en fallucka.
                        Under ditt fall stöter du på {antal_knivar} knivar.
                        
                        Du förlorade {antal_knivar} hälsopoäng.
            
                        Du lander sedan på en madrass och är redo för ditt nästa val.

                        ''')
                    self.hp -= antal_knivar
                
                if i == 3:
                    print('''Du gick in i en glas vägg och fick en lätt hjärnskakning 
                        och bröt din näsa.
                        
                        Du förlorade 2 hälsopoäng.
                        
                    ''')
                    self.hp -= 2
                    redo_för_val()
                    
                if i == 4:
                    print('''
                        Du stöter på en tom dörr...
            
                        På din väg genom dörren stukar du din högra fot och förlorar 1 hälsopoäng.
                        
                    ''')
                    self.hp -= 1  
                    redo_för_val() 

                if i == 5:
                    print('''
                        Du stöter på en tom dörr.
                        
                        På din väg genom dörren stukar du din vänstra fot och förlorar 1 hälsopoäng.

                    ''')
                    self.hp -= 1  
                    redo_för_val() 

                if i == 6:
                    print('''
                        Du sträcker ut din hand redo att öppna dörren framför dig. När din 
                        hud kommer i kontakt med dörrhantaget börjar du SssKKaKka som aldrig för.
                        
                        Du har fått en stöt och du förlorar 1 hälsopoäng!
                
                        Efter en stund av skakande reser du dig, går igenom dörren vars handtag
                        inte längre är strömförande, och är redo för ditt nästa val

                    ''')
                    self.hp -= 1  
 
            # -------------------------------------- monster -------------------------------------- #
            if dörrens_innehåll == 3:
            
                if self.lvl < 5:
                    m_styrka = randint(1, 15)
                    m_hp = randint(1, 15)
                    
                elif self.styrka in {5, 6, 7, 8, 9}:
                    m_styrka = randint(10, 20)
                    m_hp = randint(10, 20)
                    
                else: 
                    m_styrka = randint(25, 35)
                    m_hp = randint(25, 35)
                
                def m_meny():
                    print('''
                    Vad vill du göra?
                    
                        - Slå till                    -> a
                        - Spring!                     -> d
                        - Visa styrka och hälsopoäng  -> q
                        
                        ''')

                while True:
                    print('''
                    Du står öga mot öga med ett monster..👾
                    ''')
                    m_meny()
                    val = input("Ditt val -> ")
                    
                    if val == "a":
                        strid = randint(1, 3)
                        
                        if strid in (1, 2):
                            print('''        
                    Du tar i och svingar ett stort slag mot monstret
                    Monstret kan inte undvika det och tar skada
                            ''')
                            m_hp -= self.styrka   
                          
                        else:
                            print('''
                    Du tar och försöker skada monstret med din styrka
                    Du är för långsam och monstret har bra reflexer
                    Du missade monstret
                    ''')
                            
                    if val == "q":
                        print(f'''
                    Du har {self.styrka} i styrka och {self.hp} hälsopoäng")
                    printMonstret har {m_styrka} i styka och {m_hp} hälsopoäng
                        ''')
                        continue

                    if val == "d":
                        spring = randint(1, 3)

                        if self.styrka <= m_styrka:
                            if spring == 1:
                                print('''
                    Du sprang iväg  
                                ''')
                                redo_för_val() 
                                break
                        
                            else:
                                print('''            
                    Du misslyckades med att springa iväg
                                ''') 
                            
                        if self.styrka > m_styrka:
                            if spring in {1, 2}:
                                print('''      
                    Du sprang iväg
                                ''')
                                redo_för_val()      
                                break

                            else:
                                print('''
                    Du misslyckade med att springa iväg  
                                        ''')


                    if m_hp <= 0: 
                        print('''
                    
                    Monstret blev ledset och sprang iväg
                    Du lvlade upp!
                    ''')                       
                        self.lvl += 1
                        redo_för_val() 
                        break

                    m_slag_resultat = randint(1, 3)
                    print('''
                    Du är utmattad
                    Monstret tar nu sin chans att slå dig
                    Monstert tar i från tårna med ett STORT slag
                    ''')
                    if m_slag_resultat in {1, 2}:
                        print('''  
                    Monstret missade dig
                    ''')
                        input("Klicka 'enter' för att fortsätta")
                        redo_för_val() 

                    elif m_slag_resultat == 3:
                        print(f'''
                    Monstret träffade dig
                    Du förlorade {m_styrka} hälsopoäng
                        ''') 
                        self.hp -= m_styrka
                        input("Klicka 'enter' för att fortsätta")
                        redo_för_val()
                
                    if self.hp <= 0: 
                        break
        
        else:
            print("Felaktig inmating")
    
    #-------------------------------------------------- inte längre bakom dörr ----------------------------------------------------------#
    
    def dö(self): 
        """
        Medelar spelaren om att den har dött och hur långt den kom i spelet.
        """
        print("Du dog då du förlorade alla dina hälsopoäng")
        print(f"Du kom till lvl {self.lvl}")
                
    def vinna(self):
        """
        Medelar spelaren att den har vunnit spelet och hur många hälsopoäng den har kvar.
        """
        print("Wooooooo")     
        print("Du vann!!!!!")
        print(f"{self.hp} hälsopoäng återstår.")

    def fusknapp_vinst(self):
        """
        Gör så att spelaren vinner direkt vid intryckning av rätt knapp.
        """
        self.lvl += 15                   

    def fusknapp_förlust(self):
        """
        Gör så att spelaren dör direkt vid intrycking av rätt knapp.
        """
        self.hp -= 100             
   
def intro_text():
    print('''
    Välkommen till äventyrsspelet!

    I detta spelet kommet du att utforska ett gammalt slott, när du öppnar dörrar 
    kan du antingen hamna i en fälla, hitta en kista, vars innehåll ger bonusar, 
    eller träffa på ett monster. Under spelets gång kommer du få göra val som påverkar 
    ditt resultat.
    
    Vid start börjar du med 100 hälsopoäng (hp), 10 styrkepoäng och du befinner dig 
    i level (lvl) 1.

    För att vinna behöver du komma till lvl 15. 
    Om dinna hp tar slut innan dess dör du och spelet är slut.

    Lycka till!!
    ''')  
    input("för att stänga, klicka på enter")
    
def meny(): 
    """
    Skriver ut huvudmenyn.
    """
    print('''
    Vad vill du göra?                
        
    - Gå frammåt i slottet -> w
    - Kolla stats          -> q
    - kolla inventory      -> e

    ''')

def avslutande_text():
    print('''
    Tack för att du spelade detta spel!
    Hoppas du hade lite kul i alla fall.
    
    Skapat av: Julia, Ebba och Emilia Te20c
    ''')
#---------------------------------------- H U V U D P R O G R A M -----------------------------------#
random_dude = Player()
intro_text()
while True:
    meny()
    random_dude.styrke_bonus()
    val = input("Ditt val -> ")

    if val == "e":
        random_dude.visa_inventory()
        input("för att stänga, klicka på enter") 

    elif val == "q":
        random_dude.stats()
        input("för att stänga, klicka på enter")
        
    elif val == "w":
       random_dude.bakom_dörr()

    elif val == "p":
        random_dude.fusknapp_vinst()
        
    elif val == "å":
        random_dude.fusknapp_förlust()

    else:
        print('''
        Livet är ett misstag
        Klicka på å för att veta varför

        Pankakor är även najs
        ''')
        continue

    if random_dude.hp <= 0:
        random_dude.dö()
        break

    if random_dude.lvl >= 15:
        random_dude.vinna()
        break
avslutande_text()
