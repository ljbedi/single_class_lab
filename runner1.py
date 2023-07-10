
# class Student:

#     def __init__(self, name, cohort, favourite_language): 
#         self.input_name = name
#         self.input_cohort = cohort 
#         self.input_favourite_language = favourite_language

#     def talk(self): 
#         return "I can talk!" 

#     def say_favourite_language(self, favourite_language):
#         self.favourite = input("What is your favourite language?")
#         print("I love " + self.favourite)

#     def what_cohort(self):
#         self.cohor = input("What cohort are you in?")
#         print("You are in " + self.input_cohort)
        

class Team: 

    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0 

    def add_player(self, new_player): 
        self.players.append(new_player)

    def has_player(self, player_to_find):
        for player in self.players: 
            if player == player_to_find:
                return True
        return False 
    
    def play_game(self, won_game):
        if won_game:
            self.points += 3
        
    

    