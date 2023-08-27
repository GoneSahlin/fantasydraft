import json
import pandas as pd
import os


position_map = {1: "QB", 2: "RB", 3: "WR", 4: "TE", 5: "K", 16: "ST"}
input_filename = os.path.join("data", "input.json")
output_filename = os.path.join("data", "players.csv")


def json_to_list(json_obj):
    players = [x['player'] for x in json_obj['players']]


    rows = []
    for player in players:
        name = player['fullName']
        position_id = player['defaultPositionId']
        points = player['stats'][-1]['appliedTotal']
        rank = player['draftRanksByRankType']['PPR']['rank']

        position = position_map[position_id]

        row = [name, position, points, rank]
        rows.append(row)
    
    return rows


def input_json():
    text =  input("Enter JSON: ")

    json_obj = json.loads(text)

    return json_obj


keep_going = True
rows = []
while keep_going:
    with open(input_filename, 'r') as input_file:
        text = input_file.read()
    
    json_obj = json.loads(text)

    new_rows = json_to_list(json_obj)
    rows.extend(new_rows)

    incorrect_input = True
    while incorrect_input:
        keep_going_input = input("Continue entering players? (y/n)")
        if keep_going_input == "y":
            incorrect_input = False
            continue
        elif keep_going_input == "n":
            incorrect_input = False
            keep_going = False



old_df = pd.read_csv(output_filename)

df = pd.DataFrame(data=rows, columns=['name', 'position', 'points', 'rank'])

df = pd.concat([old_df, df])

df.to_csv(output_filename, index=False)
