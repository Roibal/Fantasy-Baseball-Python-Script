import random

def CreateLineUp():
    """
    The Purpose of this program is to automate the selection of a Fantasy Baseball Lineup on FanDuel.com
    to win GPP and Head-To-Head Contests.
    An algorithm has been developed which determines 'efficiency' of a player based on FPPG and salary.
    :param DailyRoster:
    :return:
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
    pitcher_list = []
    catch_list = []
    first_b_list = []
    second_b_list = []
    third_b_list = []
    ss_list = []
    of_list = []
    list_of_lineups = []

    lineup = {"P": None,
              "C": None,
              "1B": None,
              "2B": None,
              "3B": None,
              "SS": None,
              "OF": [None, None, None],
              "Draft Salary": None}

        #Team Rank is based on MLB Power Rankings and will be used to draft players on high-ranked teams which
        #play low-ranked teams, from ESPN.com Power Ranking, accessed 5/31/2016
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
        home = player[6]
        opponent = player[7]
        player.append(team_rank[home]-team_rank[opponent])

    for player in filt_player_list:     #Create Line-Up based upon positions and team-rankings
        if player[10]<-4:          #Only Select Players which have a team power ranking difference of greater than 7
            #print(player)
            #for position in lineup.keys():

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

    """
            if player[2] == 'OF':
                if of_i < 3:
                    lineup[player[2]][of_i] = player[1] + " " + player[0]
                    of_i += 1
            else:
                lineup[player[2]] = player[1] + " " + player[0]
    """
            #Positions are drafted using random choice based upon pre-built/filtered lists for each position
            #While Statement continues to draft lineups until draft salary is less than Salary Cap

    for i in range(10):
        pitcher = random.choice(pitcher_list)
        catcher = random.choice(catch_list)
        first_base = random.choice(first_b_list)
        second_base = random.choice(second_b_list)
        third_base = random.choice(third_b_list)
        short_stop = random.choice(ss_list)
        outfield1 = random.choice(of_list)
        outfield2 = random.choice(of_list)
        if outfield1 == outfield2:
            outfield2 = random.choice(of_list)
        outfield3 = random.choice(of_list)
        if outfield3 == (outfield2 or outfield1):
            outfield3 = random.choice(of_list)

        lineup_list = [pitcher, catcher, first_base, second_base, third_base, short_stop,
                       outfield1, outfield2, outfield3]
        draft_salary = 0
        tot_avg_fppg = 0

        for player in lineup_list:
            draft_salary += int(player[-1])
            tot_avg_fppg += float(player[-2])
    """    if draft_salary < 33500:
            for player in of_list:
                if int(outfield3[-1])<int(player[-1]):
                    lineup_list.pop()
                    lineup_list.append(player)

            draft_salary = 0
            tot_avg_fppg = 0
            for player in lineup_list:
                draft_salary += int(player[-1])
                tot_avg_fppg += float(player[-2])
    """
        lineup_list.append(draft_salary)
        lineup_list.append(tot_avg_fppg)
        if 33500 < int(draft_salary) < 35100:
            list_of_lineups.append(lineup_list)


    """
    lineup["P"] = pitcher[1] + " " + pitcher[0]
    lineup["C"] = catcher[1] + " " + catcher[0]
    lineup["1B"] = first_base[1] + " " + first_base[0]
    lineup["2B"] = second_base[1] + " " + second_base[0]
    lineup["3B"] = third_base[1] + " " + third_base[0]
    lineup["SS"] = short_stop[1] + " " + short_stop[0]
    lineup["OF"][0] = outfield1[1] + " " + outfield1[0]
    lineup["OF"][1] = outfield2[1] + " " + outfield2[0]
    lineup["OF"][2] = outfield3[1] + " " + outfield3[0]
    lineup["Draft Salary"] = draft_salary

    print(lineup)
    print("alternative outfielders list", of_list)
    print("first base", first_b_list)
    print(second_b_list)
    print(third_b_list)
    print(ss_list)
    print("Pitcher List", pitcher_list)
    """
    for lineups in list_of_lineups:
        print(lineups)

def main():
    players_data_list = []
    play_csv = input('What is the name of the daily CSV file?')
    player_list = LoadPlayerData(play_csv, players_data_list)
    filter_player_list = FilterPlayerData(player_list)
    print("Original Number of Players: {}".format(len(player_list)))
    print("Filtered Number of Players: {}".format(len(filter_player_list)))

    DraftLineup(filter_player_list)

if __name__ == "__main__":
    main()