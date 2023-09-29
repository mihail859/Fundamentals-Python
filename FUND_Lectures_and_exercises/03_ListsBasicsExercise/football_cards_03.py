# A-1 A-5 A-10 B-2
team_a_sent = []
team_b_sent = []

is_terminated = False
referee_notebook = [card for card in input().split()]
for player in referee_notebook:
    split_info = player.split("-")
    team = split_info[0]
    player_number = int(split_info[1])
    if team == "A" and player_number not in team_a_sent:
        team_a_sent.append(player_number)
        if len(team_a_sent) >= 5:
            is_terminated = True
            break
    if team == "B" and player_number not in team_b_sent:
        team_b_sent.append(player_number)
        if len(team_b_sent) >= 5:
            is_terminated = True
            break
print(f"Team A - {11 - len(team_a_sent)}; Team B - {11- len(team_b_sent)}")
if is_terminated:
    print("Game was terminated")