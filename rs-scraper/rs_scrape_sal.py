import requests
from bs4 import BeautifulSoup

questItems = open("QuestItemsSal.txt", "w");

page = requests.get("http://runescape.salmoneus.net/quests/").content
questList = BeautifulSoup(page, "html.parser")
itemCount = {}
itemList = {}
masterItemList = []
for quest in questList.findAll("a", {"class" : "quest"}):
    page = requests.get("http://runescape.salmoneus.net/" + quest['href']).content
    soup = BeautifulSoup(page, "html.parser")
    print quest
    for subHeader in soup.findAll("strong"):
        if subHeader.string == "Items:":
            parent = subHeader.findParent()
            #print parent
            parentcontent = str(parent).split("x <a")
            i = 0
            for fstring in parentcontent:
                itemCount[i] = fstring[-1]
                i += 1
            #print itemCount
            items = parent.findAll('a')
            i = 0
            for item in items:
                print item.string
                questItems.write(item.string+": "+itemCount[i]+"\n")
                itemList[item.string] = itemCount[i]
    masterItemList.append(itemList)
print masterItemList
    #try:
    #    items = items.findAll('a')
    #    for item in items:
    #        questItems.write(item.string+"\n")
    #except AttributeError:
    #    pass
