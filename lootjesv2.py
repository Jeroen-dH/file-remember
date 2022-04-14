import random, json
check = True
try:
    file = open(r"C:\Users\Jeroen\Desktop\Projecten\file-remember\logs.json","a")
    if check:
        print("File created 'logs.json'.")
        check = False
except:
    with open(r"C:\Users\Jeroen\Desktop\Projecten\file-remember\logs.json", "x") as file:
        print("using 'logs.json'.")

s = 1
namen = []
namencheck = []
lootjes = []
naamDic = {

}


vraag = int(input("Hoeveel deelnemers zijn er?: ")) 
for x in range(vraag):
    vraag2 = input("Wat zijn de namen van de deelnemers?\n: ")
    namen.append(vraag2)
    lootjes.append(vraag2)
    
    print("Naam:",vraag2,", toegevoegd.")
namen = list(set(namen))
lootjes = list(set(lootjes))
print(namen)
 
n = len(namen)
m = 0
temp = []
while m != n:
    x = random.randint(0,n-1)
    y = random.randint(0,n-1)
    if x != y:
        v = 0
        if len(temp) != 0:
            for i in range(len(temp)):
                if str(y) == temp[i][1] or str(x) == temp[i][0]:
                    v += 1
        if v == 0:
            temp.append(str(x) + str(y))
            print(namen[x], "heeft", namen[y])
            m += 1
            naamDic["naam"+str(s)] = namen[x]
            s += 1
            naamDic["naam"+str(s)] = namen[y]
            s += 1
json.dump(naamDic, file)
