import game

game.initPlayers()

game.addPlayer(game.createNewPlayer("lala", damage=18, defensePower=4))
game.addPlayer(game.createNewPlayer("lulu", damage=12, defensePower=7))
game.addPlayer(game.createNewPlayer("lolo", damage=15, defensePower=8))
game.addPlayer(game.createNewPlayer("lili", damage=21, defensePower=11))
game.addPlayer(game.createNewPlayer("abdu", damage=16, defensePower=13))
game.removePlayer("kiki")

game.attackPlayer(game.PlayerList[0], game.PlayerList[2])
game.attackPlayer(game.PlayerList[3], game.PlayerList[2])
game.attackPlayer(game.PlayerList[3], game.PlayerList[1])
game.attackPlayer(game.PlayerList[2], game.PlayerList[4])
game.attackPlayer(game.PlayerList[1], game.PlayerList[0])

game.displayMatchResult()