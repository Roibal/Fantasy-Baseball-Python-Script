import random

def CreateLineUp():
    """
    The Purpose of this program is to automate the selection of a Fantasy Baseball Lineup on FanDuel.com
    to win GPP and Head-To-Head Contests. 
    Download .csv from FanDuel.com, place in folder and run program to output a Fantasy Baseball lineup. 
    For use in 50/50 or Head to Head matchups.
    Future Changes: An algorithm which determines 'efficiency' of a player based on FPPG and salary.
    """

def LoadPlayerData(player_data_csv, players_data_list):
    #This Function Will Load Player Data from a CSV file and send to AddPlayerData Function to create a list of dicts
    with open(player_data_csv, 'r') as player_file:
        for line in player_file:
            new_line = line.split(',')
            #Formatting based on FanDuel format
            if new_line[13] == '0\n':
                pass
            else:
                AddPlayerData(new_line[2].strip('"'), new_line[3].strip('"'), new_line[1].strip('"'),
                              new_line[4].strip('"'), new_line[5].strip('"'), new_line[6].strip('"'),
                              new_line[8].strip('"'), new_line[9].strip('"'), new_line[10].strip('"'),
                              players_data_list)
    return players_data_list

def AddPlayerData(fname, lname, position, FPPG, played, salary, team, opponent, injured, players_data_list):
    #The AddPlayerData function will format input arguments and append to player list
    players_data_list.append([lname, fname, position, FPPG, played, salary, team, opponent, injured])

def FilterPlayerData(player_list):
    #FilterPlayerData function will create a new list of players based on filtered data choices:
    #Salary >2100, Not Injured, Played >2 games, FPPG > 2, in starting line-up
    filtered_player_list = []
    for player in player_list[1:]:
        if int(player[5])<2100:
            pass
        elif float(player[3])<2:
            pass
        elif int(player[4])<2:
            pass
        elif player[8] != '':
            pass
        else:
            player.append(int(player[5])/float(player[3]))          #Calculate 'Efficiency' value, append to player list
            filtered_player_list.append(player)                 #append filtered list of players
    return filtered_player_list

def DraftLineup(filt_player_list):
    salary_cap = 35000
    draft_salary = 0
                                #A List is Created for each position based on filtered players list and other determining factors
    pitcher_list = []
    catch_list = []
    first_b_list = []
    second_b_list = []
    third_b_list = []
    ss_list = []
    of_list = []
    list_of_lineups = []

        #Team Rank is based on MLB Power Rankings and will be used to draft players on high-ranked teams which
        #play low-ranked teams, from ESPN.com Power Ranking, accessed 5/31/2016
        #A Webscraping script will be added to automatically upload Team Ranking from ESPN power ranking
        
    team_rank = {"CHC": 1,
                 "BOS": 2,
                 "WAS": 3,
                 "SFG": 4,
                 "BAL": 5,
                 "CWS": 6,
                 "SEA": 7,
                 "NYM": 8,
                 "CLE": 9,
                 "STL": 10,
                 "PIT": 11,
                 "TEX": 12,
                 "KAN": 13,
                 "PHI": 14,
                 "LOS": 15,
                 "TAM": 16,
                 "MIA": 17,
                 "TOR": 18,
                 "DET": 19,
                 "NYY": 20,
                 "COL": 21,
                 "LAA": 22,
                 "ARI": 23,
                 "OAK": 24,
                 "HOU": 25,
                 "ATL": 30,
                 "MIN": 29,
                 "CIN": 28,
                 "SDP": 27,
                 "MIL": 26}

    for player in filt_player_list:     #Append to filtered player list the differential between ranking of teams
        home = player[6]                #Players are chosen on teams which are at a significant advantage over their opponent
        opponent = player[7]
        player.append(team_rank[home]-team_rank[opponent])

    for player in filt_player_list:     #Create Line-Up based upon positions and team-rankings
        if player[10]<-4:          #Only Select Players which have a team power ranking difference of greater than 7
            if player[2] == 'P':
                if int(player[5]) > 7000:
                    pitcher_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == 'C':
                catch_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == '1B':
                first_b_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == '2B':
                second_b_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == '3B':
                third_b_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == 'SS':
                ss_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == 'OF':
                of_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])

        #Positions are drafted using random choice based upon pre-built/filtered lists for each position
        #Ten LineUps are drafted based upon pre-developed lists of players at each position
    while len(list_of_lineups) < 10 :
        pitcher = random.choice(pitcher_list)
        catcher = random.choice(catch_list)
        first_base = random.choice(first_b_list)
        second_base = random.choice(second_b_list)
        third_base = random.choice(third_b_list)
        short_stop = random.choice(ss_list)
        outfield1 = random.choice(of_list)
        outfield2 = random.choice(of_list)
        if outfield1 == outfield2:                      #Ensuring the outfield players are not Duplicated
            outfield2 = random.choice(of_list)
        outfield3 = random.choice(of_list)
        while outfield3 == outfield2:
            outfield3 = random.choice(of_list)
        while outfield3 == outfield1:
            outfield3 = random.choice(of_list)

        lineup_list = [pitcher, catcher, first_base, second_base, third_base, short_stop,
                       outfield1, outfield2, outfield3]
                            #Creates Line-Up from randomly-chosen positions
        draft_salary = 0
        tot_avg_fppg = 0

        for player in lineup_list:                      #Calculates the total salary for each lineup and fppg for the line up
            draft_salary += int(player[-1])             #Efficiency will also be calculated for line-ups
            tot_avg_fppg += float(player[-2])

        lineup_list.append(draft_salary)
        lineup_list.append(tot_avg_fppg)
        lineup_list.append(float(draft_salary/tot_avg_fppg))
        if 34500 < int(draft_salary) < 35100:
            list_of_lineups.append(lineup_list)         #Includes Efficiency for comparison among various lineups
    min_efficiency = 1000
    for lineups in list_of_lineups:
        print(lineups)
        if lineups[-1]<min_efficiency:
            min_efficiency=lineups[-1]
    print(min_efficiency)
    ABTest(list_of_lineups)

def ABTest(lineup_list):
    """
    The purpose of this function is to perform A/B Testing on Lineups.
    The lineup with lowest Projected Points will be lineup 'B'.
    The lineup with highest Project Points will be lineup 'A'.
    Each lineup will be entered in 50/50 lineups, with all data recorded in separate excel spreadsheet.
    :param lineup_list:
    :return:
    """
    lineupA = lineup_list[0]
    lineupB = lineup_list[1]
    for lineup in lineup_list:
        if lineup[-2]>lineupA[-2]:
            lineupA=lineup
        if lineup[-2]<lineupB[-2]:
            lineupB = lineup
    print("Lineup A: ", lineupA)
    print("Lineup B: ", lineupB)
    
def main():
    players_data_list = []
    play_csv = input('What is the name of the daily CSV file?')
    player_list = LoadPlayerData(play_csv, players_data_list)
    filter_player_list = FilterPlayerData(player_list)
    DraftLineup(filter_player_list)

if __name__ == "__main__":
    main()
