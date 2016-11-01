import random

def CreateLineUp():
    """
    The Purpose of this program is to automate the selection of a Fantasy Football Lineup on FanDuel.com
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
            #Formatting based on FanDuel format for Daily Fantasy Football
            if new_line[0].isalpha():
                pass
            else:
                AddPlayerData(new_line[2].strip('"'), new_line[3].strip('"'), new_line[1].strip('"'),
                              new_line[4].strip('"'), new_line[5].strip('"'), new_line[6].strip('"'),
                              new_line[8].strip('"'), new_line[9].strip('"'), new_line[10].strip('"'),
                              players_data_list)
    #print(players_data_list)
    return players_data_list

def AddPlayerData(fname, lname, position, FPPG, played, salary, team, opponent, injured, players_data_list):
    #The AddPlayerData function will format input arguments and append to player list
    players_data_list.append([lname, fname, position, FPPG, played, salary, team, opponent, injured])

def FilterPlayerData(player_list):
    #FilterPlayerData function will create a new list of players based on filtered data choices:
    #Salary >2100, Not Injured, Played >2 games, FPPG > 2, in starting line-up
    filtered_player_list = []
    for player in player_list:
        if int(player[5])<2100:
            pass
        elif float(player[3])<1:
            pass
        elif int(player[4])<1:
            pass
        elif player[8] != '':
            pass
        else:
            player.append(int(player[5])/float(player[3]))          #Calculate 'Efficiency' value, append to player list
            filtered_player_list.append(player)                 #append filtered list of players
    #filtered_player_list = sorted(filtered_player_list, key=lambda player: player[-1])
    return filtered_player_list

def DraftLineup(filt_player_list):
    salary_cap = 60000
    draft_salary = 0
                                #A List is Created for each position based on filtered players list and other determining factors
    qb_list = []
    rb_list = []
    wr_list = []
    te_list = []
    k_list = []
    d_list = []
    list_of_lineups = []

        #Team Rank is based on MLB Power Rankings and will be used to draft players on high-ranked teams which
        #play low-ranked teams, from ESPN.com Power Ranking, accessed 10/16/2016 updated
        #A Webscraping script will be added to automatically upload Team Ranking from ESPN power ranking

    team_rank = {"NE": 1,
                 "SEA": 2,
                 "PIT": 3,
                 "MIN": 4,
                 "DEN": 5,
                 "GB": 6,
                 "DAL": 7,
                 "KC": 8,
                 "ATL": 9,
                 "PHI": 10,
                 "OAK": 11,
                 "CIN": 12,
                 "BAL": 13,
                 "ARI": 14,
                 "BUF": 15,
                 "HOU": 16,
                 "WAS": 17,
                 "CAR": 18,
                 "SD": 19,
                 "NYG": 20,
                 "IND": 21,
                 "DET": 22,
                 "LA": 23,
                 "NYJ": 24,
                 "TEN": 25,
                 "NO": 26,
                 "JAC": 27,
                 "TB": 28,
                 "MIA":29,
                 "SF": 30,
                 "CHI": 31,
                 "CLE": 32}

    for player in filt_player_list:     #Append to filtered player list the differential between ranking of teams
        home = player[6]                #Players are chosen on teams which are at a significant advantage over their opponent
        opponent = player[7]
        player.append(team_rank[home]-team_rank[opponent])

    for player in filt_player_list:     #Create Line-Up based upon positions and team-rankings
        if player[10]<-4:          #Only Select Players which have a team power ranking difference of greater than 7
            if player[2] == 'QB':
                if int(player[5]) > 7000:
                    qb_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == 'RB':
                rb_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == 'WR':
                wr_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == 'TE':
                te_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == 'K':
                k_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
            elif player[2] == 'D':
                d_list.append([player[0], player[1], player[-1], player[-2], player[3], player[5]])
    #The Following code sorts the original lists of players and only chooses top 50% highest efficiency players
        #Quarterback Lists
    qb_list = sorted(qb_list, key=lambda qb: qb[3])
    end_index_qb = len(qb_list)/2
    qb_list = qb_list[:int(end_index_qb)]
        #Running Back Lists
    rb_list = sorted(rb_list, key=lambda rb: rb[3])
    end_index_rb = len(rb_list)/2
    rb_list = rb_list[:int(end_index_rb)]
        #Wide Receiver Lists
    wr_list = sorted(wr_list, key=lambda wr: wr[3])
    end_index_wr = len(wr_list)/2
    wr_list = wr_list[:int(end_index_wr)]
        #Tight End Lists
    te_list = sorted(te_list, key=lambda te: te[3])
    end_index_te = len(te_list)/2
    te_list = te_list[:int(end_index_te)]
        #Kicker Lists
    k_list = sorted(k_list, key=lambda k: k[3])
    end_index_k = len(k_list)/2
    k_list = k_list[:int(end_index_k)]
        #Defense Lists
    d_list = sorted(d_list, key=lambda d: d[3])
    end_index_d = len(d_list)/2
    d_list = d_list[:int(end_index_d)]

        #Positions are drafted using random choice based upon pre-built/filtered lists for each position
        #One-Hundred LineUps are drafted based upon pre-developed lists of players at each position
    while len(list_of_lineups)<1000:
        qb = random.choice(qb_list)
        rb1 = random.choice(rb_list)
        wr1 = random.choice(wr_list)
        te = random.choice(te_list)
        k = random.choice(k_list)
        d = random.choice(d_list)
        rb2 = random.choice(rb_list)
        wr2 = random.choice(wr_list)
        wr3 = random.choice(wr_list)
        while rb1 == rb2:                      #Ensuring the Wide Receivers and Running Back players are not Duplicated
            rb2 = random.choice(rb_list)
        while wr3 == wr2:
            wr3 = random.choice(wr_list)
        while wr3 == wr1:
            wr3 = random.choice(wr_list)

        lineup_list = [qb, rb1, rb2, wr1, wr2, wr3,
                       te, k, d]
                            #Creates Line-Up from randomly-chosen positions
        draft_salary = 0
        tot_avg_fppg = 0

        for player in lineup_list:                      #Calculates the total salary for each lineup and fppg for the line up
            draft_salary += int(player[-1])             #Efficiency will also be calculated for line-ups
            tot_avg_fppg += float(player[-2])

        lineup_list.append(draft_salary)
        lineup_list.append(tot_avg_fppg)
        lineup_list.append(float(draft_salary/tot_avg_fppg))
        if 59500 < int(draft_salary) < 60100:
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

    print("\nLineup A:\n ")
    lineupA_list = []
    for player in lineupA[:-3]:
        player_name = player[1] + " " + player[0]
        lineupA_list.append(player_name)
    print(lineupA_list, lineupA[-2])

    print("\nLineup B:\n ")
    lineupB_list = []
    for player in lineupB[:-3]:
        player_name = player[1] + " " + player[0]
        lineupB_list.append(player_name)
    print(lineupB_list, lineupB[-2])

def main():
    players_data_list = []
    play_csv = input('What is the name of the daily CSV file?')
    player_list = LoadPlayerData(play_csv, players_data_list)
    filter_player_list = FilterPlayerData(player_list)
    DraftLineup(filter_player_list)

if __name__ == "__main__":
    main()