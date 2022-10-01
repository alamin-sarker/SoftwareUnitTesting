"""Software Unit Testing Report
Scissor Paper Rock game using Test Driven Development"""

import unittest
from unittest import mock
from rock_paper_scissor import RockPaperScissor


class GameTestCase(unittest.TestCase):
    '''Unit testing class'''
    game = RockPaperScissor()

    def test_computer_select(self):
        '''Testing computer randomly picks one of the options'''
        self.assertIn(self.game.computer_select(), ["rock", "paper", "scissor"],  # noqa: E501
                      msg="Invalid option choose by computer.")

    def test_user_choice(self):
        '''Testing player's input'''
        with mock.patch('builtins.input', return_value="rock"):
            assert self.game.user_choice() in ["rock", "paper", "scissor", "q", "rs"]  # noqa: E501

    def test_add_point_to_winner(self):
        '''Testing tne point is given to the winner'''
        self.assertEqual(3, self.game.add_point_to_winner(2),
                         msg="Incorrect point addition.")

    def test_check_winner(self):
        '''Testing first to get five points wins the game'''
        self.assertFalse(self.game.check_winner(3))
        self.assertTrue(self.game.check_winner(5))

    def test_determine_winner(self):
        '''Testing compare selections and determine who the winner is'''
        self.assertEqual("computer", self.game.determine_winner("rock", "paper"), msg="Invalid winner")  # pylint: disable=line-too-long  # noqa: E501
        self.assertEqual("user", self.game.determine_winner("rock", "scissor"), msg="Invalid winner")  # pylint: disable=line-too-long  # noqa: E501
        self.assertEqual("computer", self.game.determine_winner("paper", "scissor"), msg="Invalid winner")  # pylint: disable=C0301  # noqa: E501
        self.assertEqual("user", self.game.determine_winner("paper", "rock"), msg="Invalid winner")  # pylint: disable=C0301  # noqa: E501
        self.assertEqual("tie", self.game.determine_winner("rock", "rock"), msg="Invalid winner")  # pylint: disable=C0301  # noqa: E501
        self.assertEqual("tie", self.game.determine_winner("paper", "paper"), msg="Invalid winner")  # pylint: disable=C0301  # noqa: E501


if __name__ == '__main__':
    unittest.main()
