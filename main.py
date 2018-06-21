exbyes = [1,0,1,0,1,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,0]

def createTeamList(teamlist):
    count = 0
    teamcount = True

    while teamcount:
        if teams > count:
            teamlist.append("Team " + str(count))
            count = count + 1
            teamcount = True
        elif teams <= count:
            teamcount = False
        else:
            continue
    return(teamlist)

def calculatebyes(teams):
    binteams = bin(teams)
    binteams = binteams[2:len(binteams)]

    print("number of teams: " + str(teams))

    short= len(binteams)
    if short <= 2:
        first2 =0
    else:
        first2 = binteams[0:2]

    what = binteams[2:len(binteams)]

    if what:
        remaining = int(what, 2)
    else:
        remaining= teams%2

    p2 = next_power_of_2(teams)

    p2l2 = p2>>2
    p2l1 = p2>>1

    byes = remaining

    if first2 == str(11):
        byes = p2l1 - p2l2 - remaining
    print("Calculated Byes - Opt2: " + str(byes))

    return(byes)



def next_power_of_2(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()

correct=True

for x in range(0,32,1):
    teams = x + 1

    byes = calculatebyes(teams)
    correct=correct and (byes == exbyes[x])
    teamlist = list() # define var teamlist
    createTeamList(teamlist)  #call createTeamList and pass exiting/empty list

    # print(teamlist)  # print list created based on number of teams

    print("Hard Coded Byes: " + str(exbyes[x]))

    print("\n")

print(correct)

# create initial matchups in winners bracket

# modify team names



