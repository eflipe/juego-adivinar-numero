import unittest
from functions.numbers_generator import randomNumberGenerator

class TestNumbersGenerator(unittest.TestCase):

    def test_input(self):
        """
        Test random number creation.
        """

        randomNumber_1 = randomNumberGenerator()
        randomNumber_2 = randomNumberGenerator()
        print(randomNumber_1, "is not equal to ",  randomNumber_2)

        self.assertNotEqual(randomNumber_1, randomNumber_2)
