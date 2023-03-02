import json
print('hello')
try:
    f = open("score-sheet.json", 'r')
    score_sheet = json.loads(f.read())
    f.close
except:
    score_sheet = {}
print(score_sheet)
usr_name = input("user name:").upper()
if score_sheet.get(usr_name) is None:
    new_score = {
        usr_name : {
        "loss" : 0,
        "win" : 1
        }
    }
    score_sheet.update(new_score)
else:
    score_sheet[usr_name]["win"] += 1
print(score_sheet)
f = open("score-sheet.json", 'w')
f.write(json.dumps(score_sheet))
f.close()
