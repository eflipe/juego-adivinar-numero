def inputNumber(prompt = "Please, enter a four-digit number: >>> "):
    """
       Ask for a specific data.
     """

    user_input = input(prompt)

    try:
        if user_input.isdigit():
            humanNumber = user_input
            humanNumber = checkInput(humanNumber)
            return humanNumber
        else:
            print("\nThe input data is incorrect, only numbers are allowed. Please, try again.\n")
            return inputNumber()


    except ValueError:
        print("\nThe input data is incorrect, only numbers are allowed. Please, try again.\n")
        return inputNumber()


def checkInput(humanNumber):
    """ Checks if the input data is valid and returns
    a 4-digit integer.
    """
    humanNumber = str(humanNumber)

    if len(humanNumber) != 4:
        print("\nSorry, only four digits numbers are valid.\n")
        humanNumber = inputNumber()
        return humanNumber

    elif len(humanNumber) == 4:
        for number in range(len(humanNumber)):
            if humanNumber.count(humanNumber[number]) > 1:
                print("\nSorry, the four digits must be unique.\n")
                humanNumber = inputNumber()
                return humanNumber

        print("\nThe number entered is: {} ".format(humanNumber))

        return humanNumber


def inputSelection(prompt):
    """Checks if the input data is valid and returns the selected option.
     """

    try:

        selection = int(input(prompt))

        while selection != 1 and selection != 2:
            selection = int(input("Please, select one of the options (1 or 2): "))

        print("\nYour option is the number: {}\n".format(selection))

        if selection ==1:
            print("\nTry to guess the number.\n\n")
            return selection

        if selection ==2:
            print("\nThe machine will guess the number.\n")
            return selection

        return selection

    except ValueError:
        print("\nThe input data is incorrect, only numbers are allowed. Please, try again.\n")
        selection = inputSelection("Please, select only one of the options (1 or 2): ")
        return
