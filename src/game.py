# Player
Player = dict(name="", score=0, damage=0, health=100, defensePower=0, defense=False)

# 1. initPlayers() :
PlayerList = []


def initPlayers():
    global PlayerList
    PlayerList = []


# 2.createNewPlayer(name, damage=0, defensePower=0) :
def createNewPlayer(name, damage=0, defensePower=0):
    return {
        "name": name,
        "score": 0,
        "damage": damage,
        "health": 100,
        "defensePower": defensePower,
        "defense": False,
    }


# 3. addPlayer(player) :
def addPlayer(player):
    global PlayerList
    PlayerList.append(player)


# removePlayer(name) :
def removePlayer(name):
    global PlayerList

    for player in PlayerList:
        if player["name"] == name:
            PlayerList.remove(player)
            print("Player removed")
            return
    print("There is no player with that name!")


# 5. setPlayer(player, key, value) :
def setPlayer(player, key, value):
    player[key] = value


# 6. attackPlayer(attacker:dict, target:dict) :
def attackPlayer(attacker, target):
    if target["defense"]:
        # Agar tidak ada nilai negatif
        damage = max(0, attacker["damage"] - target["defensePower"])
    else:
        damage = attacker["damage"]

    # Updatenya
    setPlayer(attacker, "score", attacker["score"] + (0.8 if target["defense"] else 1))
    setPlayer(target, "health", target["health"] - damage)
    setPlayer(target, "defense", False)


# 7. displayMatchResult() :
def displayMatchResult():
    global PlayerList
    # Urutkan berdasarkan skor dan kesehatan secara descending
    sorted_players = sorted(
        PlayerList, key=lambda player: (-player["score"], -player["health"])
    )

    for rank, player in enumerate(sorted_players, 1):
        print(
            f"Rank {rank}: {player['name']} | Score: {player['score']} | Health: {player['health']}"
        )
