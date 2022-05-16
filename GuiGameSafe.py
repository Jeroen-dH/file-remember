import os,json,time

path = r"C:\Users\Jeroen\Desktop\Projecten\file-remember\AutoSave.json"
exist = os.path.exists(path)
print(exist)
saved = {}
saved["SaveAt"] = 0



def closeSave(path):
    file.close()
    os.remove(path)


def gameover(path):
    print("\n\n----------\nGame over.\n----------")
    file.close()
    os.remove('AutoSave.json')


def begin():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------")
    print("-Welkom bij de adventure/escape room text game!\n-In deze game moet je de juiste keuzes maken om de game to voltooien!\n-Je kan tijdens de game spullen vinden die jou kunnen helpen met de game, Dus let goed op!\n-")
    print("-Ben jij er klaar voor? zo ja,")
    Beginnen = input("-Druk dan op 'Enter' om te beginnen.\n---------------------------------------------------------------------------------------------------------------\n")
    with open (path, "w") as file:
        saved['SaveAt'] = 1
        json.dump(saved, file)
        
    backstory()

def backstory():
    print("\n* Je zit in een vliegtuig over de jungle.\n* Het uitzicht is heel mooi, maar opeens hoor je veel geluid en het vliegtuig verliest balans.")
    print("* Je kijkt naar buiten en ziet dat de motor flink aan het roken is!\n* Je loopt naar voren naar de piloot om te vragen wat er is gebeurd.")
    print("* Jullie hebben een zwerm vogels geraak! Het vliegtuig verliest snel hoogte.\n* De piloot zegt dat je in je stoel moet gaan zitten en je moet voorberieden voor een noodlanding!")
    print("* De onderkant van het vliegtuig raakt de boomtoppen en verliest veel snelheid en jullie storten hard neer!\n* Je raakt bewusteloos door de impact van de crash.")
    print("* Even later kom je weer bij omdat je een hard geluid hoorde. Je blijft even zitten om bij te komen want je voelt je nog niet helemaal lekker.")
    print("* je voelt je al iets beter en gaat kijken in de cockpit. je treft de piloot dood aan. \n* Je hoort weer het geluid waar je wakker van werd. het is buiten het vliegtuig.")
    print("* je ziet een machette liggen in het vliegtuig.")
    with open (path, "w") as file:
        saved['SaveAt'] = 2
        json.dump(saved, file)
    deel1()
def deel1():
    with open (path, "w") as file:
        saved['SaveAt'] = 3
        json.dump(saved, file)
    Uitzoeken = input(">>> Ga je op onderzoek uit om te kijken wat het geluid is?\n ja/nee: ")
    if Uitzoeken == 'ja':
        print("\n* Je gaat op onderzoek uit. je loopt het vliegtuig uit je ziet nog niks op het eerste gezicht.\n* je loopt iets verder en je ziet een leeuw vlak bij het vliegtuig wrak.")
        print("* Je hebt de machette, het beest ziet jou niet dus je kan hem aanvallen zonder dat het het door heeft.")
        deel1_2()
    elif Uitzoeken == 'nee':
        print("\n\n* Je besluit in het vliegtuig te blijven. Dit is een goeie keuze geweest je ziet na een paar minuten dat het er meerdere zijn en niet eentje.")
        print("* Na een paar minuten zie je dat het gevaar weg is")
        print("* Je wilt eigenlijk op pad om te kijken of je de weg uit de jungle kunt vinden")
        print("* je kan ook nog het vliegtuig doorzoeken voor spullen die je kan gebruiken met het onsnappen uit de jungle.")
        deel2()

def deel1_2():
    with open (path, "w") as file:
        saved['SaveAt'] = 4
        json.dump(saved, file)
    aanvallen = input(">>> Wil je de leeuw aanvallen?")
    if aanvallen == 'ja':
        print("\n* Je loopt rustig op de leeuw af, Maar wacht! Het zijn er meer en niet een!\n* Ze hebben jou door en lopen rustig naar jou toe. je probeert terug het vliegtuig in te gaan")
        print("* De leeuwen zijn je te snel af en krijgen jou te pakken.\n* Helaas je word opgegeten door de leeuwen.")
        gameover(path)
    elif aanvallen == 'nee':
        print("\n\n* Je besluit je terug te trekken. je gaat dus terug het vliegtuig in en wacht af todat de leeuwen weg zijn.")
        print("* uit angst wil je hier zo snel mogelijk weg.")
        print("* je rent een random kant het bos in. Je blijft lopen tot dat het schemerig word. je moet een slaap plek vinden.")
        print("* je probeert een goeie slaapplek te vinden. na een tijdje lopen kom je bij een rivier aan je vind dit een handige plek om je bedje te maken.")
        deel1_3()
def deel1_3():
    with open (path, "w") as file:
        saved['SaveAt'] = 5
        json.dump(saved, file)
    Materiaal = input(">>> Van welk materiaal wil je het bed maken? \n\n-Op de grond met grotte bladeren waar je op kan liggen (Type 'grond')\n\n-van de grond af op takken (een soort boomhut maar dan alleen de vloer). (type 'van de grond')")
    if Materiaal == 'van de grond':
        print("\n\n* Je gaat takken verzamelen, wat groote bladeren en wat lianen dat je kan gebruiken als touw")
        print("* je zet het boomhutje in elkaar. je bent net optijd klaar voordat het helemaal donker is.")
        print("* Je gaat rustig slapen. maar ineens breekt midden in de nacht jou constructie af.")
        print("* Je beland met je hoofd vol op een steen en raakt bewusteloos met een groot gat in je hoofd. \n* Voordat je weer bij komt ben je al dood gebloedt.")
        gameover(path)
    elif Materiaal == 'grond':
        print("\n\n* Je besluit op de grond gaat slapen. je gaat grote bladeren verzamellen die je kan gebruiken als deken je gaat slapen. ")
        print("* Je word midden in de nacht aangevallen door een leeuw. Je gebruikt je machtte om hem te proberen van je af te krijgen maar helaas je red het niet\n* Je word opgeeten door de leew")
        gameover(path)

def deel2():
    with open (path, "w") as file:
        saved['SaveAt'] = 10
        json.dump(saved, file)
    vliegtuig_doorzoeken = input(">>> Wil je het vliegtuig doorzoeken? ")
    if vliegtuig_doorzoeken == 'ja':
        print("\n\n* Je gaat het vliegtuig doorzoeken. je vind de telefoon van de piloot, maar helaas het hij is leeg.\n* je zoekt verder en vind de 1ste hulp doos. ")
        print("* je verzorgt al je wonden die je hebt van de crash. Je gaat verder zoeken. je vind eten in blik dit neem je me voor onderweg zodat je toch iets te eten heb.")
        print("* je vind ook nog een verrekijker. die kan handig zijn als je ergens boven op een berg staat of een hoog punt.\n je stopt alles in een tas die je hebt gevonden.")
        print("* je wilt op pad gaan maar je vind nog een informatie boekje. er staan wat handige dingen in die je kan gebruiken, je neemt het boekje mee. ")
        print("* je wilt dus op pad gaan maar het word al schemerig. \n* Je kan kiezen om in het vliegtuig te blijven of om de nacht door te brengen in het vliegtuig waar het veilig is.")
        deel2_2()
    elif vliegtuig_doorzoeken == 'nee':
        print("\n\n* Je gaat op onderzoek uit. je loopt een kant uit maar weet niet welke kan. je komt uiteindelijk op een pad uit.\n* Het pad splits in 3 wegen. Je moet nu een keuze gaan maken welke kant je op gaat")
        print("* Ga je pad 1,2 of 3 op? ")
        deel2_1()
def deel2_1():
    with open (path, "w") as file:
        saved['SaveAt'] = 11
        json.dump(saved, file)
    Keuze_pad = input(">>> Uw keuze: ")
    if Keuze_pad == '1':
        print("\n\n* je loopt pad 1 op. Het is een lang pad. je komt uit eindelijk bij de uitgang, altans daar lijkt het op.")
        print("* Maar helaas het is een val. Je valt in een diep gat met geen uitweg.")
        print("* Je blijft vast zitten in het gat voor een paar dagen en verhongerd.\n Je gaat uiteindelijk dood\n\n------------\nGame over\n------------")
    elif Keuze_pad >= '2':
        print("\n\n* Je gaat pad " + Keuze_pad + " op. Je loopt het pad af en ziet dat pad 2 en 3 op hetzelfde eind put aankomt.")
        print(" ")
        print("* je komt een val tegen en je moet 2x een 2 cijferige code invullen. ")
        a = int(input("eerste cijfer: "))
        b = int(input("tweede cijfer: "))
        if a > b:
            print("\n\n* Je mag door")
            print("* Of nee toch niet het is een val en gaat dood")
            gameover(path)
        elif b < a:
            print("\n\n* je hebt de val geactiveerd en je word beschoten met pijlen. een raankt jou in je hoofd en je gaat dood")
            gameover(path)
    else:
        print("het is een val! je bent dood")
        gameover(path)   
            
def deel2_2():
    with open (path, "w") as file:
        saved['SaveAt'] = 12
        json.dump(saved, file)
    Blijven_vliegtuig = input(">>> Blijf je in het vliegtuig?: ")
    if Blijven_vliegtuig == 'ja':
        print("\n\n* Je blijft voor de nacht nog in het vliegtuig. Het is hier nog een beetje veilig.")
        print("* De volgende ochtend ga je op pad je bent goed voor bereid en hebt alle spullen nog die je heb verzammeled.\n*Je staat op het punt om te gaan en je ziet nog een kompas liggen. Je weet dat je naar het oosten aan het vliegen was.")
        print("* voor zover je weet was je pas een paar killometer over de jungle aan het vliegen. Je gaat dus lopen naar het westen. ")
        print("* je begint met lopen en je ziet overal nog stukken liggen van het vliegtuig.\n* Je loopt door en komt uiteindelijk een blauwe veer tegen.")
        print("* Je weet niet van welk dier het kan zijn. Je loopt dus door.")
        print("* Het blijkt dus een stam te zijn 'de blauw veren' die in de jungle wonen. je komt hun kamp tegen. op het eerste gezicht lijken ze aardig.")
        print("* Ze willen jou helpen met terug te komen naar bewoond gebied waar je terug naar huis kan.")
        deel2_3()
    elif Blijven_vliegtuig == 'nee':
        print("\n\n* Je besluit dus op pad gaan in het donker. je loopt het bos in en komt op een kleun pad. je blijft lopen en en het word ineens een hobbelig pad")
        print("* Je loopt rustig door maar ineens val je in een gat. je komt niet uit het gat. je hebt nog eten in je tas maar het is niet genoeg om te blijven leven.")
        gameover(path)

def deel2_3():
    with open (path, "w") as file:
        saved['SaveAt'] = 13
        json.dump(saved, file)
    vertrouw = input(">>>Vertrouw je de blauw veren?: ")
    if vertrouw == 'ja':
        print("\n\n* Je vertrouwt de blauw veren. ze geven je eten en bieden kleren aan. het is dus een goeie keuze geweest ze te vertrouwen.")
        print("* De blauw veren kennen een groot gebied van de jungle. ze willen jou de volgende dag naar bewoond gebied brengen. dus eerst even een nachie tukken.")
        print("\n*De volgende dag ga je op pad met de blauw veren. ze weten heel de route door de jungle.")
        print("* Opeens gaan de blauw veren in defense mode staan. Zie zien de zwarte veren! dat is de andere stam die in de jungle woont.")
        print("* zij zijn niet aardig. ze vragen aan jou of je ze wil aanvallen of ze ontwijken")
        deel2_4()
    elif vertrouw == 'nee':
        print("\n\n* je hoeft de hulp niet van de blauw veren. dat is een domme keuze de blauw veren kunnen heel agressief zijn. ze nemen jou gevangen.")
        print("* Zij houden jou vast en maken je daarna af")
        gameover(path)                        
def deel2_4():
    with open (path, "w") as file:
        saved['SaveAt'] = 14
        json.dump(saved, file)
    zwart_veren = input(">>>Wil je ze aanvallen?: ")
    if zwart_veren == 'ja':
        print("* \nJullie vallen ze aan maar jullie zijn in de minderheid. Jullie verliezen het gevecht en gaan dood")
        gameover(path)
    elif zwart_veren == 'nee':
        print("\n* Jullie trekken je terug en lopen met een groote boog om hun heen. jullie lopen weer rustig door")
        print("* Je gaat door en jullie krijgen honger. gelukkig heb jij nog het eten in blik van het vliegtuig, maar jullie weten niet hoelang het nog lopen is")
        deel2_5()
def deel2_5():
    with open (path, "w") as file:
        saved['SaveAt'] = 15
        json.dump(saved, file)
    eten = input(">>>Willen jullie nu het eten op eten of bewaren?(Type 'eten' of 'bewaren'): ")
    if eten == 'bewaren':
        print("\n\n* Jullie gaan door zonder te eten. bijna iedereen klaagt maar jullie gaan toch door.")
        print("* tijdens het lopen horen jullie wat geritsel in de bosjes. Iedereen trekt zijn wapen en ineens komen er leeuwen uit de bosjes.")
        print("* jij word aangevallen door een leeuw je probeert het van je af te krijgen. de leeuw haalt zijn klauw door jou tas heen en alles valt er uit.")
        print("* je verliest bijna al je spullen en ook je eten. je moet dus zo snel mogelijk naar de bewoonde wereld.")
        print("* Jullie halen het niet omdat jullie uithongeren.")
        gameover(path)
    elif eten == 'eten':
        closeSave(path)
        print("\n\n* jullie gaan eten. jullie gaan ergens zitten en jullie zijn op je pad een group leeuwen lopen. die hebben jullie dus net optijd ontwijkt.")
        print("* Na het eten lopen jullie door en jullie halen uitendelijk een dorpje. ")
        print("\n\n\n\n\n---------------------------\nGEHAALD!\nJe bent ontsnapt uit de jungle, je kan nu naar huis!\n---------------------------")

if exist:
    with open (path, "r+") as file:
        data = json.load(file)
        print(data)
    if data == {'SaveAt': 1}:
        begin()
    elif data == {'SaveAt': 2}:
        backstory()
    elif data == {'SaveAt': 3}:
        deel1()
    elif data == {'SaveAt': 4}:
        deel1_2()
    elif data == {'SaveAt': 5}:
        deel1_3()
    elif data == {'SaveAt': 10}:
        deel2()
    elif data == {'SaveAt': 11}:
        deel2_1()
    elif data == {'SaveAt': 12}:
        deel2_2()
    elif data == {'SaveAt': 13}:
        deel2_3()
    elif data == {'SaveAt': 14}:
        deel2_4()
    elif data == {'SaveAt': 15}:
        deel2_5    
else:
    try:
        with open(path, "r+") as file:
            json.dump(saved,file)
    except:
        with open(path, "x") as file:
            print()
    begin()
