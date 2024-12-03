import game as m


characters = {
    "Jokowi": {"damage": 15, "defensePower": 10},
    "Prabowo": {"damage": 20, "defensePower": 15},
    "Gibran": {"damage": 10, "defensePower": 20},
    "Anies": {"damage": 25, "defensePower": 5},
    "Ganjar": {"damage": 18, "defensePower": 12},
    "Cak Imin": {"damage": 12, "defensePower": 18},
    "Mahfud MD": {"damage": 22, "defensePower": 8},
    "Megawati": {"damage": 10, "defensePower": 25},
    "Ahok": {"damage": 23, "defensePower": 7},
    "Erick Thohir": {"damage": 19, "defensePower": 11},
}

# Jumlah pemain minimum dan maksimum
num_players = int(input(f"Enter the number of players (2-{len(characters)}): "))
if num_players < 1 or num_players > len(characters):
    print(
        f"Invalid number of players! Please enter a number between 2 and {len(characters)}."
    )
    exit()

# Pemain memilih karakter
print("\nChoose your character:")
available_characters = list(characters.keys())
for i, name in enumerate(available_characters, 1):
    stats = characters[name]
    print(f"{i}. {name} (Damage: {stats['damage']}, Defense: {stats['defensePower']})")

for i in range(num_players):
    while True:
        choice = int(input(f"Player {i+1}, choose your character (1-{len(available_characters)}): "))
        if 1 <= choice <= len(available_characters):
            chosen_name = available_characters.pop(choice - 1)
            stats = characters[chosen_name]
            player = m.createNewPlayer(chosen_name, damage=stats["damage"], defensePower=stats["defensePower"])
            defense_choice = input(f"Player {i+1}, enable defense? (yes/no): ").lower() == "yes"
            m.setPlayer(player, "defense", defense_choice)
            m.addPlayer(player)
            print(f"Player {i+1} chose {chosen_name} with {'defense enabled' if defense_choice else 'no defense'}.\n")
            break
        else:
            print("Invalid choice. Please try again.")


# Status awal pemain
print("\n Battle Starts! Players:")
for player in m.PlayerList:
    print(
        f"{player['name']} | Damage: {player['damage']} | Defense: {'ON' if player['defense'] else 'OFF'} | Health: {player['health']}"
    )

# Pertarungan 3 ronde
for round_number in range(1, 4):
    if len(m.PlayerList) <= 1:
        break
    print(f"\n ROUND {round_number}:")
    for attacker in m.PlayerList:
        target_index = (m.PlayerList.index(attacker) + 1) % len(m.PlayerList)
        target = (m.PlayerList[target_index])

        print(f"{attacker['name']} attacks {target['name']}!")
        m.attackPlayer(attacker, target)
        print(f"{target['name']} Health: {target['health']}")

        if target["health"] <= 0:
            print(f"{target['name']} has been disqualified!")
            m.removePlayer(target["name"])

# Hasil akhir
print("\nFinal Results:")
if m.PlayerList:
    winner = m.PlayerList[0]
    print(
        f"The winner is {winner['name']} with {winner['health']} health remaining!"
    )
else:
    print("All players have been disqualified. No winner!")
