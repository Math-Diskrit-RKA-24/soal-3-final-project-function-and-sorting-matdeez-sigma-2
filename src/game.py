def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(nama, kerusakan=0, kekuatanDefense=0):
    Player = dict(name=nama,
              score=0,
              damage=kerusakan,
              health=100,
              defensePower=kekuatanDefense,
              defense=False)
    return Player

def addPlayer(Player):
    global PlayerList
    PlayerList.append(Player)

def removePlayer(nama):
    global PlayerList
    for i in PlayerList:
        if PlayerList[i]["name"]==nama:
            PlayerList.remove(i)
            return
    print("There is no player with that name!")

def setPlayer(player, key, value):
    for i in PlayerList:
        if PlayerList[i]==player:
            PlayerList[i][key]=value
            return
    print("There is no player with that attribute")

def attackPlayer(attacker, target):
    a = 0
    t = 0
    for i in PlayerList:
        if PlayerList[i]==attacker:
            a = i
            break
    for i in PlayerList:
        if PlayerList[i]==target:
            t = i
            break
    if PlayerList[t]["defense"]:
        if PlayerList[a]["damage"] > PlayerList[t]["defensePower"]:
            PlayerList[a]["score"] += 0.8
            PlayerList[t]["health"] -= abs(PlayerList[a]["damage"] - PlayerList[t]["defensePower"])
        PlayerList[t]["defense"] = False
    else:
        if PlayerList[a]["damage"] > PlayerList[t]["defensePower"]:
            PlayerList[a]["score"] += 1
            PlayerList[t]["health"] -= abs(PlayerList[a]["damage"] - PlayerList[t]["defensePower"])

def displayMatchResult():
    sorted_data = sorted(PlayerList, key=lambda x: (-x["score"], -x["health"]))
    for i in range(len(sorted_data)):
        print(f"Rank {i+1}: {sorted_data[i]["name"]} | Score: {sorted_data[i]["score"]} | Health: {sorted_data[i]["health"]}")