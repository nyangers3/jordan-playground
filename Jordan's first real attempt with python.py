print('''Who is the better team Chelsea or Arsenal?

We will find out now
    ''')

import csv

data = []

with open('football_results.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

chelsea_vs_arsenal_results = data
# I need to find out number of games, biggest win, longest winning streak, most wins, goal different, competition with most % win for CFC & AFC
number_of_games = len(chelsea_vs_arsenal_results)


print(f'Number of games played : {number_of_games}')

#below was from the help of chat gpt. It finds the instance with the biggest scoreline deficit
def margin_of_victory(game):
    home_score, away_score = map(int, game['Score'].split('-'))
    return abs(home_score - away_score)

biggest_win = max(chelsea_vs_arsenal_results, key=margin_of_victory)

#below I am going to try and adjust the above code so I can just get the team name of the winner

if 'W' in biggest_win['Result']:
    team_who_is_biggest_winnah = 'Chelsea'
else: team_who_is_biggest_winnah = 'Arsenal'


print(f'''
Game with the biggest win:
{biggest_win['Date']} - {team_who_is_biggest_winnah} won {biggest_win['Score']} in the {biggest_win['Competition']}
''')

#code below is from chatgpt (BUT I ADDED END STREAK!)
current_streak = 0
longest_streak = 0
previous_winner = None
winning_streak_start_date = None
winning_streak_team = None
winning_streak_end_date = None #JN adding end date

def winning_streak_user_finction():

    with open('football_results.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
    
    # Skip the header row if your CSV has one
    next(reader)
    
    for row in reader:
        date = row[0] #give the date from column 1
        winner = row[2]  #give the result from column 3
        if winner == 'W': #MY CHANGE TO THE GPT PYTHON CODE TO RENAME THE RESULT TO THE WINNERS NAME
            winner = 'Chelsea'
        elif winner == 'L':
            winner = 'Arsenal'
        else:
            winner = 'Draw'
        
        if winner == previous_winner:
            current_streak += 1 #if the current result is the same as the last one, +1 to current streak
            winning_streak_end_date = date #JN adding end date
        else:
            current_streak = 1 #otherwise current streak is 1
            winning_streak_start_date = date #when a new streak starts, give the date
            winning_streak_team = winner #when a new streak starts, give the result
        
        if current_streak > longest_streak: #if the current streak is bigger than the longest streak then...
            longest_streak = current_streak #make the longest streak = to the current streak
            longest_streak_start_date = winning_streak_start_date #give the longest streak start date the same as the current streak
            longest_streak_team = winning_streak_team #give the longest streak name the result
            longest_streak_end_date = winning_streak_end_date #hoping the end of the streak
        
        previous_winner = winner #the test that has just ran through the row is now upated to be the previous test
        
        print(f'''The longest winning streak was when {longest_streak_team} won {longest_streak} games in a row from {longest_streak_start_date} to {longest_streak_end_date}.
      ''')


def how_many_wins(club_name): #I want to try and use def, and make something that I just have to pass Chelsea or Arsenal into the User defined function
    import csv
    
    data = []

    with open('football_results.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)
        results = data
        #chelsea_vs_arsenal_results = data
        #number_of_games = len(chelsea_vs_arsenal_results)

    if club_name == 'Chelsea': #I need to create a variable that stores a function that changes the club name to either W or L
        count_wins = data.count('W')
    else:
        count_wins = data.count('L')

    return count_wins
        

chelsea_wins = how_many_wins('Chelsea')
arsenal_wins = how_many_wins('Arsenal')

if chelsea_wins > arsenal_wins:
    winningest_team = chelsea_wins
else:
    winningest_team = arsenal_wins

print(winningest_team)