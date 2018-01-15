## rs_file_counter.py
## opens file, counts number of items within it, creates another file with results

questItems = open("QuestItems.txt", "r");
#questReqs = open("QuestReqs.txt", "r");

questsCount = dict()
line = questItems.readline()
while (line):
    line = line.split(",")
    if (line[0] in questsCount):
        questsCount[line[0]] += 1
    else:
        questsCount[line[0]] = 1
    line = questItems.readline()

questReqCounts = open("QuestItemsResults.txt", "w");
questReqCountsOrdered = dict()
for quest in questsCount:
    print questsCount[quest]
    #questReqCounts.write(quest + ": " + str(questsCount[quest])+"\n")
    if (questsCount[quest] not in questReqCountsOrdered):
        questReqCountsOrdered[questsCount[quest]] = quest
    else:
        questReqCountsOrdered[questsCount[quest]] += ", " + quest

for questNums in questReqCountsOrdered:
    questReqCounts.write(str(questNums) + ": " + questReqCountsOrdered[questNums]+"\n")
