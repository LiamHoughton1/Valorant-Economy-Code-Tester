creds = 0
abilitycredcost = 0
startcost = 0
agent = 0
whatability = 0
howmany = 0
jett = 0
gun = 0
guncost = 0
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
       whatability = int(input("Choose First Ability: 1.Cloudburst 2.Updraft 3.None "))
       if whatability == 1:
              howmany = int(input("How Many? "))
              if howmany == 1:
                     abilitycredcost = int(abilitycredcost) + int(jettabilitycloudburst)
              if howmany == 2:
                     abilitycredcost = int(abilitycredcost) + int(jettabilitycloudburst) + int(jettabilitycloudburst)
                     print(abilitycredcost)
       if whatability == 2:
              howmany = int(input("How Many? "))
              if howmany == 1:
                     abilitycredcost = int(abilitycredcost) + int(jettabilityupdraft)
              if howmany == 2:
                     abilitycredcost = int(abilitycredcost) + int(jettabilityupdraft) + int(jettabilityupdraft)
       #add a whatability for 3 and have it link to the next 

       whatability = int(input('Choose Second Ability: 1.Cloudburst 2.Updraft 3.None '))
       if whatability == 1:
              howmany = int(input("How Many? "))
              if howmany == 1:
                     abilitycredcost = int(abilitycredcost) + int(jettabilitycloudburst)
              if howmany == 2:
                     abilitycredcost = int(abilitycredcost) + int(jettabilitycloudburst) + int(jettabilitycloudburst)
       if whatability == 2:
              howmany = int(input("How Many? "))
              if howmany == 1:
                     abilitycredcost = int(abilitycredcost) + int(jettabilityupdraft)
              if howmany == 2:
                     abilitycredcost = int(abilitycredcost) + int(jettabilityupdraft) + int(jettabilityupdraft)
       #add a whatability for 3 and have it link to the next 


def gun():
       global guncost
       gun = input("What Gun Are You Buying? ")
       if gun == "classic" or "Classic":
              guncost = 0
       if gun == "shorty" or "Shorty":
              guncost = 150




creds = int(input("How many credits do you have? "))
agent = input("Choose an agent ")

if agent == "jett":
       jett()

gun()
print(abilitycredcost)
print(guncost)

#maybe this will work




