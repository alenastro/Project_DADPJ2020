import json
import csv
import glob
import os
#--------------------------STEP 1->>> SAVE PATHS TO CALENDARS TO A FILE---------------------------------

entry1 = glob.glob(pathname ='/Users/katka/OneDrive/Dokumenty/DA/Projekt/Data 2/cals/*', recursive=True)
output1 = open("cal_paths.csv","w", encoding="utf-8")

for x in entry1:
    output1.write(str(x) + "\n")

output1.close()

#---------------------------STEP 2->>> 

entry2 = open("cal_paths.csv","r", encoding="utf-8") 
output2 = open("kalendare.csv","w", encoding="utf-8")
files_list = [x.strip().replace('\\','/') for x in entry2]

entry2.close()

#---------------------------STEP 3->>> 

header =['Jmeno','Hangout Link', 'ID', 'Random ID', 'Raw Random ID', "Creator", "Start", "End", "Attendees", "Name"]
for m in header:
    output2.write(str(m) + ",")
output2.write("\n")

index = 0

for x in files_list:
    entry_json = open(x, "r", encoding="utf-8")
    b = entry_json.read()
    y=[]
    c = y.append(json.loads(b))
    entry_json.close()
    for b in y:
        for a in b:
            jmeno =os.path.basename(x)[0:-5]
            hangoutLink_adj = '---'
            if 'hangoutLink' in a:
                hangoutLink_adj = a['hangoutLink']

            id_adj = '---'
            if 'id' in a:
                id_adj = a['id']

            randomId_adj = '---'
            if 'randomId' in a:
                randomId_adj = a['randomId']

            rawRandomId_adj = '---'
            if 'rawRandomId' in a:
                rawRandomId_adj = a['rawRandomId']
            
            email_adj = '---'
            if 'email' in a ["creator"]:
                email_adj = a["creator"]['email']
            
            dateTime_start = '---'
            if 'dateTime' in a ["start"]:
                dateTime_start = a["start"]['dateTime']

            dateTime_end = '---'
            if 'dateTime' in a ["end"]:
                dateTime_end = a["end"]['dateTime']

            if "attendees" in a:
                for s in a ["attendees"]:
                    if 'email' in s:
                        attendees_adj = s['email']

                    i = [jmeno, hangoutLink_adj, id_adj, randomId_adj, rawRandomId_adj, email_adj, dateTime_start, dateTime_end, attendees_adj] 
                    for c in i:
                        output2.write(str(c) + ",")
           
                    output2.write("\n")
                    
        index +=1  
output2.close()