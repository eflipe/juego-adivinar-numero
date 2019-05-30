import unittest
from game.human_play import humanPlay

class TestHumanPlay(unittest.TestCase):

    def test_human_play(self):
        """
        Test a human play.
        """
        print("\nStart test_human_play test\n")
        print("Testing a human regular play.\n")


        machineNumber = [8,1,5,9]
        humanNumber = 8159

        humanPlay(humanNumber, machineNumber)

        print("\nFinish test_human_play test\n")
        print("---------------------------\n")
