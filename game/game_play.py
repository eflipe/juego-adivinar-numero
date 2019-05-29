from functions.input_number import inputSelection, inputNumber
from functions.numbers_generator import randomNumberGenerator
from game.human_play import humanPlay
from game.machine_play import machinePlay

def gamePlay():
    
    print("Welcome!")
    prompt = """Please, select one of the options:\n
                \n1) The human guess the number
                \n2) The machine guess the number\n
                \nType the number of your option (1 or 2): >>> """
    selection = inputSelection(prompt)

    if selection == 1:
        machineNumber = randomNumberGenerator()
        humanNumber = inputNumber()

        humanPlay(humanNumber, machineNumber)

    if selection == 2:

        humanNumber = inputNumber("Please, enter a four-digit number for the machine: >>> ")
        machinePlay(humanNumber)

gamePlay()
