from functions.input_number import inputNumber
from functions.numbers_generator import randomNumberGenerator, humanFriendly
from functions.numbers_comparation import numbersComparation



def humanPlay(humanNumber, machineNumber):
    """ Compare the typed number with the random number.
        Define when the game is over.
    """

    attempts = 0

    score = numbersComparation(humanNumber, machineNumber)
    print("R:", score[0], "G:", score[1])
    attempts +=1

    while score[1] != 4:
        humanNumber = inputNumber()
        score = numbersComparation(humanNumber, machineNumber)
        print("R:", score[0], "G:", score[1])
        attempts +=1

    if score[1] == 4:
        print("\nYou won, congratulations!\n\nNumber of attempts used: ", attempts,"\n\nThe game is over.\n")
        print("The number was: ", humanFriendly(machineNumber))


    return humanNumber, machineNumber
