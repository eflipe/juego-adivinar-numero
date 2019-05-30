import unittest
from functions.numbers_comparation import numbersComparation

class TestNumbersComparation(unittest.TestCase):

    def test_numbers_comparation(self):
        """
        Test numbers comparation.
        """

        print("\nStart test_numbers_comparation test\n")
        print("Testing different numbers that produce different outputs.\n")

        number_1 = 8951
        number_2 = [1,9,5,8]
        number_3 = 8951
        number_4 = [1,5,9,8]
        number_5 = 8951
        number_6 = [8,9,5,1]
        result_1 = numbersComparation(number_1, number_2)
        result_2 = numbersComparation(number_3, number_4)
        result_3 = numbersComparation(number_5, number_6)

        print("R: ", result_1[0], "G:", result_1[1], "Sum:", result_1[2], "Partial Number: ", result_1[3])
        print("R: ", result_2[0], "G:", result_2[1], "Sum:", result_2[2], "Partial Number: ", result_2[3])
        print("R: ", result_3[0], "G:", result_3[1], "Sum:", result_3[2], "Partial Number: ", result_3[3])

        print("\nFinish test_numbers_comparation test\n")
        print("---------------------------\n")
