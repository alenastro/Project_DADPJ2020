import json
import glob
import pandas
import csv

# ---------------------------------- FIRST STEP ----------------------------------

entry1 = glob.glob(pathname ='/Users/Alena Stroková/OneDrive/Dokumenty/Czechitas/Akademie/Zaverecna_prace/Data_od_klienta/Data_7_akt/*/*', recursive=True)
output1 = open("list_od_paths.csv","w", encoding="utf-8")

for x in entry1:
    output1.write(str(x) + "\n")

output1.close()

# ---------------------------------- SECOND STEP ----------------------------------

entry2 = open("list_od_paths.csv","r", encoding="utf-8") 
output2 = open("temporary_file.json","w", encoding="utf-8") # We only created a help/temporary json file.

a = [x.strip().replace('\\','/') for x in entry2]

entry2.close()

output2.write("[" + "\n")
for x in a:
    entry_json = open(x, "r", encoding="utf-8")
    b = entry_json.read()
    c = json.loads(b)
    entry_json.close()
    json.dump(c, output2, indent=4)
    output2.write("," + "\n")

output2.write(str(0) + "]") # The last element of the entire json file is zero. I'll get rid of it below, a desperate time demands desperate actions.

output2.close()

# ---------------------------------- THIRD STEP ----------------------------------

entry3 = open("temporary_file.json", "r", encoding="utf-8") 
output3 = open("final_file.json","w", encoding="utf-8") 

d = entry3.read()
e = json.loads(d)

entry3.close()

e.pop(-1) # I deleted the above-mentioned zero.

index = 0
for x in e:
    for y in e[index]:
        y.update({'date': str(a[index][-15:-5])})
    index += 1

json.dump(e, output3, indent=4)

output3.close()

# ---------------------------------- FOURTH STEP ----------------------------------
# We create one table with every data.

entry4 = open("final_file.json", "r", encoding="utf-8") 
output4 = open("final_file.csv","w", encoding="utf-8") 

f = entry4.read()
g = json.loads(f)

entry4.close()

header = ["type_upg",
          "subtype",
          "ts",
          "user",
          "date",
          "inviter",
          "client_msg_id",
          "team",
          "user_team",
          "source_team",
          "files_upload",
          "text_users"]

for x in header:
    output4.write(str(x) + ";")

output4.write("\n")

index = 0
for x in g:
    for y in g[index]:
        type_upg = '---' # Only one element (no list).
        if "type" in y:
            type_upg = y["type"]

        subtype = '---' # Only one element (no list).
        if "subtype" in y:
            subtype = y["subtype"]

        ts = '---' # Only one element (no list).
        if "ts" in y:
            ts = y["ts"]

        user = '---' # Only one element (no list).
        if "user" in y:
            user = y["user"]

        date = '---' # Only one element (no list).
        if "date" in y:
            date = y["date"]

        inviter = '---' # Only one element (no list).
        if "inviter" in y:
            inviter = y["inviter"]

        client_msg_id = '---' # Only one element (no list).
        if "client_msg_id" in y:
            client_msg_id = y["client_msg_id"]

        team = '---' # Only one element (no list).
        if "team" in y:
            team = y["team"]

        user_team = '---' # Only one element (no list).
        if "user_team" in y:
            user_team = y["user_team"]

        source_team = '---' # Only one element (no list).
        if "source_team" in y:
            source_team = y["source_team"]

        files_upload = '---' # Only one element (no list).
        if "upload" in y:
            files_upload = y["upload"]

        text_users = '---' # More elements (no list). That's why we divide the columns by ";".
        if "users" in y["text"]:
            text_users = y["text"]["users"]

        h = [
              type_upg,
              subtype,
              ts,
              user,
              date,
              inviter,
              client_msg_id,
              team,
              user_team,
              source_team,
              files_upload,
              text_users
            ]

        for z in h:
            output4.write(str(z) + ";")

        output4.write("\n")

    index += 1

output4.close()

# ---------------------------------- FIFTH STEP ----------------------------------
# We create one table with data only about "sh_room_created".

entry5 = open("final_file.json", "r", encoding="utf-8") 
output5 = open("final_file_room.csv","w", encoding="utf-8") 

i = entry5.read()
j = json.loads(i)

entry5.close()

header_room = [
          "subtype",
          "type_upg",
          "ts",
          "user",
          "date",
          #"inviter",
          #"client_msg_id",
          "team",
          #"user_team",
          #"source_team",
          #"files_upload",
          #"text_users",
          "channel",
          "room_id",
          "room_created_by",
          "room_date_start",
          "room_date_end",
          #"room_participants",
          "room_participant_history"
          #"channels"
          ]

for x in header_room:
    output5.write(str(x) + ",")

output5.write("\n")

index = 0
for x in j:
    for y in j[index]:

        if "subtype" in y:
            if y["subtype"] == "sh_room_created":

                subtype = '---' # Only one element (no list).
                if "subtype" in y:
                    subtype = y["subtype"]

                type_upg = '---' # Only one element (no list).
                if "type" in y:
                    type_upg = y["type"]

                ts = '---' # Only one element (no list).
                if "ts" in y:
                    ts = y["ts"]

                user = '---' # Only one element (no list).
                if "user" in y:
                    user = y["user"]

                date = '---' # Only one element (no list).
                if "date" in y:
                    date = y["date"]

                #inviter = '---' # Only one element (no list).
                #if "inviter" in y:
                #    inviter = y["inviter"]

                #client_msg_id = '---' # Only one element (no list).
                #if "client_msg_id" in y:
                #    client_msg_id = y["client_msg_id"]

                team = '---' # Only one element (no list).
                if "team" in y:
                    team = y["team"]

                #user_team = '---' # Only one element (no list).
                #if "user_team" in y:
                #    user_team = y["user_team"]

                #source_team = '---' # Only one element (no list).
                #if "source_team" in y:
                #    source_team = y["source_team"]

                #files_upload = '---' # Only one element (no list).
                #if "upload" in y:
                #    files_upload = y["upload"]

                #text_users = '---' # More elements (no list). That's why we divide the columns by ";".
                #if "users" in y["text"]:
                #    text_users = y["text"]["users"]

                channel = '---' # Only one element (no list).
                if "channel" in y:
                    channel = y["channel"] 

                room_id = '---' # Only one element (no list).
                if "id" in y["room"]:
                    room_id = y["room"]["id"]

                room_created_by = '---' # Only one element (no list).
                if "created_by" in y["room"]:
                    room_created_by = y["room"]["created_by"]

                room_date_start = '---' # Only one element (no list).
                if "date_start" in y["room"]:
                    room_date_start = y["room"]["date_start"]

                room_date_end = '---' # Only one element (no list).
                if "date_end" in y["room"]:
                    room_date_end = y["room"]["date_end"]

                #room_participants = '---' # More elements (no list). That's why we divide the columns by ";".
                #if "participants" in y["room"]:
                #    room_participants = y["room"]["participants"]

                #channels = '---' # More elements (no list). That's why we divide the columns by ";".
                #if "channels" in y["room"]:
                #    channels = y["room"]["channels"]

                room_participant_history = '---' # More elements (no list). That's why we divide the columns by ";".
                if "participant_history" in y["room"]:
                    for z in y["room"]["participant_history"]:
                        room_participant_history = z
                        
                        k = [
                              subtype,
                              type_upg,
                              ts,
                              user,
                              date,
                              #inviter,
                              #client_msg_id,
                              team,
                              #user_team,
                              #source_team,
                              #files_upload,
                              #text_users,
                              channel,
                              room_id,
                              room_created_by,
                              room_date_start,
                              room_date_end,
                              #room_participants,
                              room_participant_history,
                              #channels
                            ]

                        for w in k:
                            output5.write(str(w) + ",")

                        output5.write("\n")

    index += 1

output5.close()