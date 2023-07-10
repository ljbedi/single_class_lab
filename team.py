
from runner1 import Team 

players = ["Player 1", "Player 2", "Player 3"]
team = Team("coding_champs", players, "Bob")

team.add_player(("Player 4"))
print(players)

print(team.has_player("Player 2"))

print(team.points)
team.play_game(True)
print(team.points)