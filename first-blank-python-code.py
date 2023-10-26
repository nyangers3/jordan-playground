
print ('hello world')

jordan = 'legend'

import csv

data = []

with open('football_results.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

chelsea_vs_arsenal_results = data
## I need to find out number of games, biggest win, longest winning streak, most wins, goal different, competition with most % win for CFC & AFC
number_of_games = len(chelsea_vs_arsenal_results)

#below was from the help of chat gpt
def margin_of_victory(game):
    home_score, away_score = map(int, game['Score'].split('-'))
    return abs(home_score - away_score)

biggest_win = max(chelsea_vs_arsenal_results, key=margin_of_victory)

#below I am going to try and adjust the above code so I can just get the team name of the winner

if 'W' in biggest_win['Result']:
    team_who_is_biggest_winnah = 'Chelsea'
else: team_who_is_biggest_winnah = 'Arsenal'


##below everything will be printed
print('''Who is the better team Chelsea or Arsenal?

We will find out now
    ''')
print(f'Number of games played : {number_of_games}')

print(f'''
Game with the biggest win:
{biggest_win['Date']} - {team_who_is_biggest_winnah} won {biggest_win['Score']} in the {biggest_win['Competition']}''')

