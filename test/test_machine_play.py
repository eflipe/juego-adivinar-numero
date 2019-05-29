import unittest
from game.machine_play import machinePlay

class TestMachinePlay(unittest.TestCase):

    def test_machine_play_number_1(self):
        """
        Test a machine play.
        """
        humanNumber = "0123"

        machinePlay(humanNumber)
    def test_machine_play_number_2(self):
        """
        Test a machine play.
        """
        humanNumber = 4567

        machinePlay(humanNumber)
    def test_machine_play_number_3(self):
        """
        Test a machine play.
        """
        humanNumber = 1098

        machinePlay(humanNumber)
