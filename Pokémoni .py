# .jason => dostať do pythonu a načítať do rozumnej struktúry
# transformovať na to čo potrebujuem

#URLLIP1,2,3  , requests -> knižnice ktoré dokážu z linku ktorý zadám stiahnuť čo je tam (web scraping)

import requests
import json

data = requests.get("https://raw.githubusercontent.com/yorkcshub/Miscellanous/master/effectiveness.json")
#print(data.text)
data_json = json.loads(data.text)      #decode json
#print(data.json)

#pokemon1 = input("Attacker: ")
#pokemon2 = input("Deffender: ")

slovnik = {"super effective" : 2, "normal effective" : 1, "not very effective" : 0.5, "no effect" : 0}
slovnik2 = {}
def vypočet_sily(pokemon1, pokemon2):
    for k,v in data_json.items():   #python iteration
        #print(k,v)
        if k == "super effective":
            if pokemon1 in v:
                if pokemon2 in v.get(pokemon1):
                    return slovnik.get("super effective")
        elif k == "normal effective":
            if pokemon1 in v:
                if pokemon2 in v.get(pokemon1):
                    return slovnik.get("normal effective")
        elif k == "not very effective":
            if pokemon1 in v:
                if pokemon2 in v.get(pokemon1):
                    return slovnik.get("not very effective")
        elif k == "no effect":
            if pokemon1 in v:
                if pokemon2 in v.get(pokemon1):
                    return slovnik.get("no effect")
#vypočet_sily(pokemon1, pokemon2)

#slovnik2.update({pokemon1:pokemon2})
#print(slovnik2)

#https://dudo.gvpt.sk/

def attack(N1, N2, listpok):
    listpok = listpok.split(",")
    N1list = []
    N2list = []
    m = 0
    #print(listpok)
    while m != N1:
        N1list.append(listpok[m])
        m += 1
    print(N1list)
    o = m
    while o != (N2+m):
        N2list.append(listpok[o])
        o += 1
    print(N2list)
    prvytim = silatimu(N1list, N2list)
    druhytim = silatimu(N2list, N1list)
    if druhytim < prvytim:
        print(prvytim, ":", druhytim, "-", "ME")
    elif prvytim < druhytim:
        print(prvytim, ":", druhytim, "-", "FOE")
    elif prvytim == druhytim:
        print(prvytim, ":", druhytim, "-", "EQUAL")

def silatimu(N1list, N2list):
    spolu = 0
    for i in N1list:
        if " " in i:
            i = i.split(" ")
            for j in N2list:
                if " " in j:
                    j = j.split(" ")
                    spolu += max(vypočet_sily(i[0], j[0]) * vypočet_sily(i[0], j[1]), vypočet_sily(i[1], j[0]) * vypočet_sily(i[1], j[1]))
                else:
                    spolu += max((vypočet_sily(i[0], j), vypočet_sily(i[1], j)))
        else:
            for j in N2list:
                if " " in j:
                    j = j.split(" ")
                    spolu += (vypočet_sily(i, j[0]) * vypočet_sily(i, j[1]))
                else:
                    spolu += (vypočet_sily(i, j))
    return spolu

attack(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug")
