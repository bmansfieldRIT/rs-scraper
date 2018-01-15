import requests
from bs4 import BeautifulSoup

questItems = open("QuestItems.txt", "w");
questReqs = open("QuestReqs.txt", "w");

page = requests.get("http://www.runehq.com/quest").content
questListSoup = BeautifulSoup(page, "html.parser")

for link in questListSoup.find_all('a'):
    #print link['href'][0:24]
    if (link['href'][0:25] == "/guide.php?type=quest&id="):
        page = requests.get("http://www.runehq.com/guide.php?"+link['href'].split("?")[1]).content
        questSoup = BeautifulSoup(page, "html.parser")
        for subHeader in questSoup.findAll("div", {"class" : "undersubheader"}):
            if (subHeader.string == "Items Needed at Quest Start:"):
                items = subHeader.findNext("div")
                if (str(items.string) != "None"):
                    if (str(items.string) != "None."):
                        questItems.write(items.string+"\n")
                try:
                    items = items.findAll('a')
                    for item in items:
                        questItems.write(item.string+"\n")
                except AttributeError:
                    pass
            elif (subHeader.string == "Items Needed to Complete Quest:"):
                items = subHeader.findNext("div")
                if (str(items.string) != "None"):
                    if (str(items.string) != "None."):
                        questItems.write(items.string+"\n")
                try:
                    items = items.findAll('a')
                    for item in items:
                        questItems.write(item.string+"\n")
                except AttributeError:
                    pass
            if (subHeader.string == "Length:"):
                length = subHeader.findNext("div")
                questSubHeader = length.findNext("div")
                quests = questSubHeader.findNext("div")
                if (str(quests.string) != "None"):
                    if (str(quests.string) != "None."):
                        questReqs.write(quests.string+"\n")
                try:
                    quests = quests.findAll('a')
                    for quest in quests:
                        questReqs.write(quest.string+"\n")
                except AttributeError:
                    pass

#for x in range(0,2):
#print table
questItems.close()
questReqs.close()
