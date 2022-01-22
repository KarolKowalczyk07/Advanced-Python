# Demonstrate how to use dictionary comprehensions


def main():
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]

    # TODO: Use a comprehension to build a dictionary
    tempDict = {t: (t*9/5) + 32 for t in ctemps if t < 100}        # key on left side of :, value on right
    print(tempDict)
    print(tempDict[12])

    # TODO: Merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}

    newTeam = {k: v for team in (team1, team2) for k,v in team.items()}
    # key= k, value = v
    # get keys and values from existing teams and put them into team
    # avoid merging more than 2 dictionaries, otherwise create a function
    print(newTeam)


if __name__ == "__main__":
    main()
