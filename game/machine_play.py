from functions.numbers_generator import randomNumberGenerator, humanFriendly
from functions.numbers_comparation import numbersComparation
from functions.numbers_comparation import combinationsFunction

def machinePlay(humanNumber):
    """
    The machine starts with a predefined strategy. For example, first start with the number 0123.
    If the result is G: 1 then save that value in machineNumberGuess_1.
    On the other hand, if it is R: 1, then try different combinations up to get G: 1.
    Then, continue with the other strategies, 4567 and 0189.

    """

    attempts = 0
    regular = 0
    good = 0
    sum = 0
    combinations = 1

    strategy_1 = [0,1,2,3]
    strategy_2 = [4,5,6,7]
    strategy_3 = [0,1,8,9]

    machineNumberGuess_1 = [0, 0, 0 ,0]
    machineNumberGuess_2 = [0, 0, 0 ,0]
    machineNumberGuess_3 = [0, 0, 0 ,0]
    machineNumberGuessTotal = [0, 0, 0 ,0]


    machineNumber = strategy_1 #start with the first strategy: 0123
    print("The machine is playing...{} ".format(humanFriendly(machineNumber)))
    score = numbersComparation(humanNumber, machineNumber)
    regular = score[0]
    good= score[1]
    sum = score[2]
    numero = score[3]
    attempts += 1
    print("R:{}".format(regular))
    print("G:{}".format(good))
    machineNumberGuess_1 = numero #saves the first number
    machineNumberGuessTotal = [machineNumberGuess_1[i] + machineNumberGuess_2[i] + machineNumberGuess_3[i] for i in range(len(machineNumberGuessTotal))]
    if good != 4:
        while good != sum:
            combinations += 1
            machineNumber = combinationsFunction(machineNumber, combinations)
            print("The machine is playing...{} ".format(humanFriendly(machineNumber)))
            score = numbersComparation(humanNumber, machineNumber)
            attempts += 1
            regular = score[0]
            good= score[1]
            sum = score[2]
            numero = score[3]
            print("R:{}".format(regular))
            print("G:{}".format(good))
            machineNumberGuess_1 = numero
            machineNumberGuessTotal = [machineNumberGuess_1[i] + machineNumberGuess_2[i] + machineNumberGuess_3[i] for i in range(len(machineNumberGuessTotal))]

        if sum == 4:
            while good != sum:
                combinations += 1
                machineNumber = combinationsFunction(machineNumber, combinations)
                print("The machine is playing...{} ".format(humanFriendly(machineNumber)))
                score = numbersComparation(humanNumber, machineNumber)
                regular = score[0]
                good= score[1]
                sum = score[2]
                numero = score[3]
                print("R:{}".format(regular))
                print("G:{}".format(good))
                attempts += 1
                machineNumberGuess_1 = numero
                machineNumberGuessTotal = [machineNumberGuess_1[i] + machineNumberGuess_2[i] + machineNumberGuess_3[i] for i in range(len(machineNumberGuessTotal))]

        elif sum != 4 :
            combinations = 1
            machineNumber = strategy_2 #second strategy: 4567
            print("The machine is playing...{} ".format(humanFriendly(machineNumber)))
            score = numbersComparation(humanNumber, machineNumber)
            attempts += 1
            regular = score[0]
            good= score[1]
            sum = score[2]
            numero = score[3]
            print("R:{}".format(regular))
            print("G:{}".format(good))
            machineNumberGuess_2 = numero #saves second number
            machineNumberGuessTotal = [machineNumberGuess_1[i] + machineNumberGuess_2[i] + machineNumberGuess_3[i] for i in range(len(machineNumberGuessTotal))]

            while good != sum:
                combinations += 1
                machineNumber = combinationsFunction(machineNumber, combinations)
                print("The machine is playing...{} ".format(humanFriendly(machineNumber)))
                score = numbersComparation(humanNumber, machineNumber)
                regular = score[0]
                good= score[1]
                sum = score[2]
                numero = score[3]
                print("R:{}".format(regular))
                print("G:{}".format(good))
                attempts += 1
                machineNumberGuess_2 = numero
                machineNumberGuessTotal = [machineNumberGuess_1[i] + machineNumberGuess_2[i] + machineNumberGuess_3[i] for i in range(len(machineNumberGuessTotal))]

            score = numbersComparation(humanNumber, machineNumberGuessTotal)
            good= score[1]

            if good == 2 or good == 3:

                combinations = 1
                machineNumber = strategy_3 #third strategy: 0189
                print("The machine is playing...{} ".format(humanFriendly(machineNumber)))
                score = numbersComparation(humanNumber, machineNumber)
                attempts += 1
                regular = score[0]
                good= score[1]
                sum = score[2]
                numero = score[3]
                print("R:{}".format(regular))
                print("G:{}".format(good))
                machineNumberGuess_3 = numero
                machineNumberGuessTotal = [machineNumberGuess_1[i] + machineNumberGuess_2[i] + machineNumberGuess_3[i] for i in range(len(machineNumberGuessTotal))]
                while good != sum:
                    combinations += 1
                    machineNumber = combinationsFunction(machineNumber, combinations)
                    print("The machine is playing...{} ".format(humanFriendly(machineNumber)))
                    score = numbersComparation(humanNumber, machineNumber)
                    attempts += 1
                    regular = score[0]
                    good= score[1]
                    sum = score[2]
                    numero = score[3]
                    print("R:{}".format(regular))
                    print("G:{}".format(good))
                    for num in range(len(numero)):
                        if numero[num] == 1:
                            numero[num] = 0
                    machineNumberGuess_3 = numero
                    machineNumberGuessTotal = [machineNumberGuess_1[i] + machineNumberGuess_2[i] + machineNumberGuess_3[i] for i in range(len(machineNumberGuessTotal))]


        machineNumberGuessTotal = [machineNumberGuess_1[i] + machineNumberGuess_2[i] + machineNumberGuess_3[i] for i in range(len(machineNumberGuessTotal))]
        score = numbersComparation(humanNumber, machineNumberGuessTotal)
        good= score[1]


    if good == 4:
        print("\nThe machine won.\n")
        print("\nThe number was: {}".format(humanFriendly(machineNumberGuessTotal)))
        print("\nAttempts: {} ".format(attempts))
        print("\nThe game is over.\n")
