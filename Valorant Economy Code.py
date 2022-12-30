creds = 0
abilitycredcost = 0
startcost = 0
agent = 0
whatability = 0
howmany = 0
gun = 0
guncost = 0
shield = 0
shieldcost = 0
totalcost = 0
missingcreds = 0
sparecreds = 0
jettabilitycloudburst = 200
jettabilityupdraft = 150
brimabilitystimbeacon = 200
brimabilityincendiary = 250
brimabilityskysmoke = 100
viperabilitysnakebite = 200
viperabilitypoisoncloud = 200
omenabilityshroudedstep = 100
omenabilityparanoia = 250
omenabilitydarkcover = 150
kjabilitynanoswarm = 200
kjabilityalarmbot = 200
cypherabilitytrapwire = 200
cypherabilitycybercage = 100
sovaabilityowldrone = 400
sovaabilityshockbolt = 150
sageabilitybarrierorb = 400
sageabilitysloworb = 200
pheonixabilityblaze = 150
pheonixabilitycurveball = 250
reynaabilityleer = 250
reynaabilitydevourdismiss = 200
razeabilityboombot = 300
razeabilityblastpack = 200
breachabilityaftershock = 200
breachabilityflashpoint = 250
skyeabilityregrowth = 150
skyeabilitytrailblazer = 300
skyeabilityguidinglight = 250
yoruabilityfakeout = 100
yoruabilityblindside = 250
yoruabilitygatecrash = 150
astraabilitystar = 150
kayoabilityfragment = 200
kayoabilityflashdrive = 250
chamberabilitytrademark = 200
chamberabilityheadhunter = 150
neonabilityfastlane = 300
neonabilityrelaybolt = 200
fadeabilityprowler = 250
fadeabilityseize = 200
harbourabilitycascade = 150
harbourabilitycove = 350

def jett():      
       global abilitycredcost
       global whatability
       while True:
              try:
                     whatability = int(input("Choose First Ability: 1.Cloudburst 2.Updraft 3.None "))
                     if whatability < 1 or whatability > 3:
                            print("Please choose a valid whole number in the range 1-4")
                            print()
                            
                     else:
                            break
              except ValueError:
                     print("That is an invalid input, please try again")
                     print()
                     


       if whatability == 1:
              while True:
                     try:
                            howmany = int(input("How Many? "))
                            if howmany < 1 or howmany > 2:
                                   print("Please choose a valid whole number in the range 1-3")
                                   print()
                            else:
                                   break
                     except ValueError:
                            print("That is an invalid input, please try again")
                            print()
                            
              if howmany == 1:
                     abilitycredcost = int(abilitycredcost) + int(jettabilitycloudburst)
              if howmany == 2:
                     abilitycredcost = int(abilitycredcost) + int(jettabilitycloudburst) + int(jettabilitycloudburst)
       if whatability == 2:
              while True:
                     try:
                            howmany = int(input("How Many? "))
                            if howmany < 1 or howmany > 2:
                                   print("Please choose a valid whole number in the range 1-3")
                                   print()
                            else:
                                   break
                     except ValueError:
                            print("That is an invalid input, please try again")
                            print()
                            
              if howmany == 1:
                     abilitycredcost = int(abilitycredcost) + int(jettabilityupdraft)
              if howmany == 2:
                     abilitycredcost = int(abilitycredcost) + int(jettabilityupdraft) + int(jettabilityupdraft)
       #add a whatability for 3 and have it link to the next 

       while True:
              try:
                     whatability = int(input('Choose Second Ability: 1.Cloudburst 2.Updraft 3.None '))
                     if whatability > 3 or whatability < 1:
                            print("That input isn't valid, try again")
                     else:
                            break
              except:
                     print("That input isn't valid")


       if whatability == 1:
              while True:
                     try:
                            howmany = int(input("How Many? "))
                            if howmany < 1 or howmany > 2:
                                   print("Please choose a valid whole number in the range 1-3")
                                   print()
                            else:
                                   break
                     except ValueError:
                            print("That is an invalid input, please try again")
                            print()
                            
              if howmany == 1:
                     abilitycredcost = int(abilitycredcost) + int(jettabilitycloudburst)
              if howmany == 2:
                     abilitycredcost = int(abilitycredcost) + int(jettabilitycloudburst) + int(jettabilitycloudburst)
       if whatability == 2:
              while True:
                     try:
                            howmany = int(input("How Many? "))
                            if howmany < 1 or howmany > 2:
                                   print("Please choose a valid whole number in the range 1-3")
                                   print()
                            else:
                                   break
                     except ValueError:
                            print("That is an invalid input, please try again")
                            print()
                            
              if howmany == 1:
                     abilitycredcost = int(abilitycredcost) + int(jettabilityupdraft)
              if howmany == 2:
                     abilitycredcost = int(abilitycredcost) + int(jettabilityupdraft) + int(jettabilityupdraft)
       #add a whatability for 3 and have it link to the next 


def whatgun():
       global guncost
       gun = input("What Gun Are You Buying? ")
       if gun == "classic" or "Classic":
              guncost = 0
       if gun == "shorty" or "Shorty":
              guncost = 150
       if gun == "frenzy" or "Frenzy":
              guncost = 450
       if gun == "ghost" or "Ghost":
              guncost = 500

def shields():
       global shieldcost
       while True:
              try:
                     shield = int(input("What Shields? 1.Heavy 2.Light 3.None "))
                     if shield < 1 or shield > 3:
                            print("Please choose a valid whole number in the range 1-4")
                            print()
                            
                     else:
                            break
              except ValueError:
                     print("That is an invalid input, please try again")
                     print()
                     
       
       if shield == 1:
              shieldcost = 1000
       if shield == 2:
              shieldcost = 400

def agentselect():
       agent = input("Choose an agent: ")
       if agent.lower() == "jett":
              jett()
       else:
              print("Please Choose A Valid Valorant Agent")
              agentselect()


creds = int(input("How many credits do you have? "))
agentselect()
whatgun()
shields()

totalcost = abilitycredcost + guncost + shieldcost
print()
print("You Currently Have {} Credits".format(creds))
print("The Total cost of This Loadout is: {} Credits".format(totalcost))

if totalcost > creds:
       missingcreds = totalcost - creds
       print()
       print("You Do Not Have Enough To Afford This Loadout")
       print("You Are Missing {} Credits".format(missingcreds))
if totalcost < creds:
       sparecreds = creds - totalcost
       print()
       print("You Have Enough To Afford This Loadout")
       print("You Will Have {} Credits Left Over".format(sparecreds))


print()
print(abilitycredcost)
print(guncost)
print(shieldcost)
#maybe this will work




