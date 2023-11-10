import csv  # Import the CSV module

# Task 1: Read Data from CSV
def read_data_from_csv():
    data = []  # Initialize an empty list to store data
    with open('football_results.csv', 'r') as csv_file:  # Open the CSV file for reading
        csv_reader = csv.DictReader(csv_file)  # Create a CSV reader object
        for row in csv_reader:  # Iterate over each row in the CSV file
            data.append(row)  # Append each row (as a dictionary) to the data list
    return data  # Return the collected data

# Task 2: Number of Games Played
def number_of_games_played(data):
    number_of_games = len(data)  # Calculate the number of games played by taking the length of the data list
    print(f'Number of games played: {number_of_games}')  # Print the result

# Task 3: Game with the Biggest Win
def game_with_biggest_win(data):
    # Find the game with the biggest win based on the margin of victory
    #/// I NEED TO FURTHER UNDERSTAND THE BELOW LINE
    biggest_win = max(data, key=lambda x: abs(int(x['Score'].split('-')[0]) - int(x['Score'].split('-')[1])))
    
    # Determine the team that won the biggest win
    if biggest_win['Result'] == 'W':
        team_who_is_biggest_winnah = 'Chelsea'
    else:
        team_who_is_biggest_winnah = 'Arsenal'

    # Print the result
    print(f'''
    Game with the biggest win:
    {biggest_win['Date']} - {team_who_is_biggest_winnah} won {biggest_win['Score']} in the {biggest_win['Competition']}
    ''')

# Task 4: Longest Winning Streak
def longest_winning_streak():
    current_streak = 0  # Initialize the current streak counter
    longest_streak = 0  # Initialize the longest streak counter
    previous_winner = None  # Initialize the variable to store the previous winner
    winning_streak_start_date = None  # Initialize the variable to store the start date of the winning streak
    winning_streak_team = None  # Initialize the variable to store the team of the winning streak
    winning_streak_end_date = None  # Initialize the variable to store the end date of the winning streak

    with open('football_results.csv', 'r') as csvfile:  # Open the CSV file for reading
        reader = csv.DictReader(csvfile)  # Create a CSV reader object

        # Skip the header row if your CSV has one
        next(reader)

        for row in reader:  # Iterate over each row in the CSV file
            date = row['Date']  # Get the date from the current row
            winner = 'Chelsea' if row['Result'] == 'W' else 'Arsenal' if row['Result'] == 'L' else 'Draw'  # Rename the winner for better readability

            if winner == previous_winner:  # If the current winner is the same as the previous one
                current_streak += 1  # Increment the current streak counter
                winning_streak_end_date = date  # Update the end date of the winning streak
            else:
                current_streak = 1  # Otherwise, reset the current streak counter to 1
                winning_streak_start_date = date  # Set the start date of the new streak
                winning_streak_team = winner  # Set the team of the new streak
        
            if current_streak > longest_streak:  # If the current streak is longer than the longest streak
                longest_streak = current_streak  # Update the longest streak counter
                longest_streak_start_date = winning_streak_start_date  # Update the start date of the longest streak
                longest_streak_team = winning_streak_team  # Update the team of the longest streak
                longest_streak_end_date = winning_streak_end_date  # Update the end date of the longest streak

            previous_winner = winner  # Update the previous winner variable

    # Print the result
    print(f'''The longest winning streak was when {longest_streak_team} won {longest_streak} games in a row 
          from {longest_streak_start_date} to {longest_streak_end_date}.
          ''')

# Task 5: Count Wins for Each Club
def how_many_wins(chelsea_outcome, data):
    count_wins = sum(1 for row in data if row['Result'] == chelsea_outcome)  # Count the number of wins for the specified club
    return count_wins  # Return the count of wins

def winningest_team(data):
    chelsea_wins = how_many_wins('W', data)  # Count Chelsea's wins
    arsenal_wins = how_many_wins('L', data)  # Count Arsenal's wins

    winningest_team_name = 'Chelsea' if chelsea_wins > arsenal_wins else 'Arsenal'  # Determine the winningest team
    losingest_team_name = 'Chelsea' if chelsea_wins < arsenal_wins else 'Arsenal' # Determine the losingest team
    print(f'The winningest team is {winningest_team_name} with {max(chelsea_wins, arsenal_wins)} wins\nvs {losingest_team_name}\'s {min(chelsea_wins,arsenal_wins)} wins')  # Print the result

# Task 6: Goal Difference

def main():
    print('''Who is the better team Chelsea or Arsenal?

    We will find out now
    ''')

    # Task 1: Read Data from CSV
    data = read_data_from_csv()

    # Task 2: Number of Games Played
    number_of_games_played(data)

    # Task 3: Game with the Biggest Win
    game_with_biggest_win(data)

    # Task 4: Longest Winning Streak
    longest_winning_streak()

    # Task 5: Count Wins for Each Club
    winningest_team(data)

    # Task 6: Goal Difference

if __name__ == "__main__":
    main()