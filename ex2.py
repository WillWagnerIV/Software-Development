# Will Wagner
# IST 303 
# 9/14/2018


#  Initialize Variables
round_of_16 = [("Russia","Spain") , ("Brazil","Mexico"), ("England","Colombia"), 
    ("Sweden", "Switzerland"), ("Croatia", "Denmark"), ("Belgium","Japan"),
    ("Uruguay","Portugal"), ("France","Argentina")]

quarter_finals = [("Croatia","Russia"), ("Belgium","Brazil"),("England","Sweden"),("France", "Uruguay")]

semi_finals = [("Croatia","England"), ("France","Belgium")]

final = [("France","Croatia")]

world_cup = {"Round of 16" : round_of_16 ,
             "Quarter-Finals" : quarter_finals ,
             "Semi-Finals" : semi_finals ,
             "Final Game" : final }

# Some debugging code:

# print (world_cup["Semi-Finals"][1][1])
# for wcRound in world_cup:
#     print (wcRound)
#     for game in world_cup[wcRound]:
#         print (game)

teams = []

# Main Loop

# Create list of teams from first round
for game in world_cup["Round of 16"]:
    teams.append(game[0])
    teams.append(game[1])

print ("All the teams in Round of 16: ", teams)

# Create the list of teams that lost to France
france = []
for wcRound in world_cup:
    for game in world_cup[wcRound]:
        if "France" in game:
            if game[0] == "France":
                france.append (game[1])
            else:
                france.append (game[0])

print ("Teams that lost to france: ", france)