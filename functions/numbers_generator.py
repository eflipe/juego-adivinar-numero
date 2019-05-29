import random


def randomNumberGenerator():
    """
    Create a random number of four unique digits.

    Return:

    machineRandomNumber: a list with four unique numbers.

    """

    machineRandomNumber = random.sample(range(0,10), k=4) #genera una lista

    return machineRandomNumber

def humanFriendly(number):
    """Improve the display of the numbers. """

    number = ''.join(str(num) for num in number) #put the numbers together

    return number
