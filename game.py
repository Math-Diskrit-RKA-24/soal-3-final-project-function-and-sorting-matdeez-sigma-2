PlayerList = []

# no 1
def initPlayers():
    global PlayerList 
    PlayerList= []

# no 2
def createNewPlayer(name, damage=0, defensePower=0):
    return dict(
        name=name,
        score=0,
        damage=damage,
        health=100,
        defensePower=defensePower,
        defense=False)

# no 3
def addPlayer(player):
    PlayerList.append(player)

# no 4
def removePlayer(name):
    for player in PlayerList:
        if player['name']==name:
            PlayerList.remove(player)
            return
    print("There is no player with that name!")

# no 5
def setPlayer(player, key, value):
    player[key] = value

# no 6
def attackPlayer(attacker:dict, target:dict):
    if target["defense"]:
        setPlayer(attacker, "score", round(attacker.get( "score") +1 - 1/target["defensePower"],2))
        setPlayer(target, "health", target.get("health")-attacker.get("damage")+target.get("defensePower"))
       
    else:
        setPlayer(attacker, "score", attacker.get("score")+ 1)
        setPlayer(target, "health", target.get("health")- attacker.get("damage"))

   
    setPlayer(target, "defense", False)

# no 7    
def displayMatchResult():
    PlayerList.sort(key=lambda y: (-y['score'], -y['health']))
    for rank, player in enumerate(PlayerList, start=1):
        print(f"Rank {rank}: {player['name']} | Score: {player['score']} | Health: {player['health']}")
    
    return PlayerList
