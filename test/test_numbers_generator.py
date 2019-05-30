import unittest
from functions.numbers_generator import randomNumberGenerator

class TestNumbersGenerator(unittest.TestCase):

    def test_number_generator(self):
        """
        Test random number creation.
        """
        print("\nStart test_numbers_generator test\n")
        print("Generates two randoms numbers and compares them.\n")

        randomNumber_1 = randomNumberGenerator()
        randomNumber_2 = randomNumberGenerator()
        print(randomNumber_1, "is not equal to ",  randomNumber_2)

        self.assertNotEqual(randomNumber_1, randomNumber_2)

        print("\nFinish test_number_generator test\n")
        print("---------------------------\n")
