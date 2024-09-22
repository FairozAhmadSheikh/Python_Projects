# Voting System for 3 MLA Candidates
Database={
    "Falak Jan":[],
    "Babar Shear":[],
    "Fayaz Scorpio":[]
}
Max_Votes=int(input("How Many People will Vote Today ? "))
for i in range(0,Max_Votes):
    vote=input("\n Enter Name Or Number of Candidate You want to Vote for : \n 1 : Falak Jan\n 2 : Babar Shear\n 3 : Fayaz Scorpio : \n")
    if vote=="1" or vote=="falak jan" or vote=="falakjan":
        Database["Falak Jan"].append(vote)
    elif vote=="2" or vote=="babar shear" or vote=="babarshear":
        Database["Babar Shear"].append(vote)
    elif vote=="3" or vote=="fayaz scorpio" or vote=="fayazscorpio":
        Database["Fayaz Scorpio"].append(vote)
    else:
        print("You Did not choose Correct Option! ")
        break
# Calculate Votes Here!
Falak_Votes=len(Database["Falak Jan"])
Babar_Votes=len(Database["Babar Shear"])
Fayaz_Votes=len(Database["Fayaz Scorpio"])

if Falak_Votes>Babar_Votes and Falak_Votes>Fayaz_Votes:
    print("Falak Jan Wins! ")
elif Babar_Votes>Fayaz_Votes:
    print("Babar Wins! ")
elif Fayaz_Votes==Babar_Votes or Fayaz_Votes==Falak_Votes or Babar_Votes==Falak_Votes:
    print("No one could win it was a tie ")
else:
    print("Fayaz Wins ")

"""Danger Ahead !"""
#Complexity Incresase  Ignore till fixed
# #Empty Vote bank condition
# if Falak_Votes==0 and Babar_Votes==0 and Fayaz_Votes==0:
#     print("Vote Bank Empty ! ")
# # """Draw condition creates a flaw so ignore it """
# elif Falak_Votes==Babar_Votes and Babar_Votes==Fayaz_Votes :
#     print("Election Draw (Tied) everyone got same Number of Votes ")
# elif Falak_Votes==Babar_Votes:
#     print("Falak Jan and Babar Shear Got Same Number of Votes ")
# elif Babar_Votes==Fayaz_Votes:
#     print("Babar Shear and Fayaz Scorpio Got Same Number of Votes ")
# elif Fayaz_Votes==Falak_Votes:
#     print("Falak Jan and Fayaz Scorpio Got Same Number of Votes ")

# # Result Decission Goes Here
# else: 
#     if Falak_Votes>=Babar_Votes: # Priority to Ladies in case Equal Votes
#         if Falak_Votes>=Fayaz_Votes:
#             print("Falak Jan Wins! 👧")
#     elif Babar_Votes>=Fayaz_Votes: # Babar Shear priority if same votes between fayaz and him
#         print("Babar Shear Wins! 🐯")
#     elif Falak_Votes<Fayaz_Votes and Babar_Votes<Fayaz_Votes:
#         print("Fayaz Scorpio Wins! 🚔")
#     else:
#         print("It Seems Election Tied")

