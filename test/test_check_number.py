import unittest
from functions.input_number import checkInput

class TestInputNumber(unittest.TestCase):

    def test_input(self):
        """
        Test user input.
        """
        print("\nStart test_input test\n")
        print("Testing different valid user inputs test.\n")

        data = "0123"
        data_1 = "1234"
        data_2 = "5678"
        data_3 = "9012"

        self.assertEqual(checkInput(data), data)
        self.assertEqual(checkInput(data_1), data_1)
        self.assertEqual(checkInput(data_2), data_2)
        self.assertEqual(checkInput(data_3), data_3)

        print("\nFinish test_input test\n")
        print("---------------------------\n")
