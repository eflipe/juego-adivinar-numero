import unittest
from game.machine_play import machinePlay

class TestMachinePlay(unittest.TestCase):

    def test_machine_play_number_1(self):
        """
        Test a machine play.
        """
        print("\nStart test_machine_play test\n")
        print("Testing a machine regular play.\n")



        humanNumber = "0123"

        machinePlay(humanNumber)
    def test_machine_play_number_2(self):
        """
        Test a machine play.
        """

        print("Testing a second machine play.\n")

        humanNumber = 4567

        machinePlay(humanNumber)
    def test_machine_play_number_3(self):
        """
        Test a machine play.
        """
        print("Testing a third machine play.\n")

        humanNumber = 1098

        machinePlay(humanNumber)

        print("\nFinish test_machine_play test\n")
        print("---------------------------\n")
