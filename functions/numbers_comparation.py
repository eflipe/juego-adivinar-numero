def numbersComparation(humanNumber, machineNumber):
    """ Loop over the typed number and the random number.

        Returns:
        Good = the numbers are equal and are in the same position.
        Regular = the numbers are in the wrong position.
        Sum = the sum of regular plus good.
        Number = a number that contains the correct digits when the machine plays.

    """

    good = 0
    regular = 0
    sum = 0

    number = [0,0,0,0]


    humanNumber = str(humanNumber)


    humanNumber = [int(number) for number in humanNumber]


    for numberH in range(len(humanNumber)):

        for numberM in range(len(machineNumber)):

            if numberH == numberM and humanNumber[numberH] == machineNumber[numberM]:
               good  +=1
               number[numberM] = machineNumber[numberM]

            elif humanNumber[numberH] == machineNumber[numberM]:
              regular += 1
    sum = regular + good

    return regular, good, sum, number

def combinationsFunction(machineNumber, combinations):
    """ Machine strategy that generates different combinations from a given number.

    Returns:

    machineNumber: The given number but mixed one position

    """
    if combinations == 2:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 3:
        machineNumber[1], machineNumber[2] = machineNumber[2], machineNumber[1]


    elif combinations == 4:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 5:
        machineNumber[1], machineNumber[2] = machineNumber[2], machineNumber[1]


    elif combinations == 6:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 7:

        machineNumber[1], machineNumber[2] = machineNumber[2], machineNumber[1]

    elif combinations == 8:
        machineNumber[0], machineNumber[1] = machineNumber[1], machineNumber[0]


    elif combinations == 9:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 10:
        machineNumber[1], machineNumber[2] = machineNumber[2], machineNumber[1]


    elif combinations == 11:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 12:
        machineNumber[1], machineNumber[2] = machineNumber[2], machineNumber[1]


    elif combinations == 13:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 14:
        machineNumber[0], machineNumber[1] = machineNumber[1], machineNumber[0]


    elif combinations == 15:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 16:
        machineNumber[1], machineNumber[2] = machineNumber[2], machineNumber[1]


    elif combinations == 17:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 18:
        machineNumber[1], machineNumber[2] = machineNumber[2], machineNumber[1]


    elif combinations == 19:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 20:
        machineNumber[0], machineNumber[3] = machineNumber[3], machineNumber[0]


    elif combinations == 21:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 22:
        machineNumber[1], machineNumber[2] = machineNumber[2], machineNumber[1]


    elif combinations == 23:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    elif combinations == 24:
        machineNumber[1], machineNumber[2] = machineNumber[2], machineNumber[1]


    elif combinations == 25:
        machineNumber[2], machineNumber[3] = machineNumber[3], machineNumber[2]


    return machineNumber
