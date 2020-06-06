import csv
import json

inputFile = open("users.json", encoding = "utf-8") #open json file
outputFile = open("users.csv", 'w',encoding = "utf-8") #load csv file
x = inputFile.read()
y = json.loads(x)
inputFile.close()

header =["ID", "Team_ID", "Email", "Team"]

for m in header:
    outputFile.write(str(m) + ",")
outputFile.write("\n")
for a in y:
    id_adj = '---'
    if "id" in a:
        id_adj = a["id"]

    team_id_adj = '---'
    if "team_id" in a:
        team_id_adj = a["team_id"]

    email_adj = '---'
    if "email" in a ["profile"]:
        email_adj = a["profile"]["email"]

    team_adj = '---'
    if "team" in a ["profile"]:
        team_adj = a["profile"]["team"]

    i = [id_adj, team_id_adj,email_adj, team_adj] 
    for b in i:
        outputFile.write(str(b) + ",")
        
    outputFile.write("\n")
    
outputFile.close()
