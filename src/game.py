def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(name, damage=0, defensePower=0):
    return dict(
        name=name,
        score=0,
        damage=damage,
        health=100,
        defensePower=defensePower,
        defense=False,
    )

def addPlayer(Player):
    global PlayerList
    PlayerList.append(Player)

def removePlayer(nama):
    global PlayerList
    
    for i in PlayerList:
        if i["name"]==nama:
            PlayerList.remove(i)
            return
    print("There is no player with that name!")

def setPlayer(player, key, value):
    player[key] = value

def attackPlayer(attacker, target):
    if target["defense"]:
        score = round(attacker["score"] + 1 - (1 / target["defensePower"]), 2)
        health = target["health"] + target["defensePower"] - attacker["damage"]
        setPlayer(target,"defense",False)
    else:
        score = round(attacker["score"] + 1,2) 
        health = target["health"] - attacker["damage"] 
        score = max(0, score)
    

    setPlayer(attacker, "score", score)
    setPlayer(target, "health", health)

def displayMatchResult():
    global PlayerList
    sorted_data = sorted(PlayerList, key=lambda x: (-x["score"], -x["health"]))
    for i in range(len(sorted_data)):
        print(f"Rank {i+1}: {sorted_data[i]["name"]} | Score: {sorted_data[i]["score"]} | Health: {sorted_data[i]["health"]}")