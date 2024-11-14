import unittest
from unittest.mock import patch
class Team:
    def __init__(self, name, wins=0, losses=0):
        self.name = name
        self.wins = wins
        self.losses = losses

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        total_wins = self.wins + self.losses
        return round(self.wins / total_wins, 4)
    # TODO: Define print_standing()
    def print_standing(self):

        print(f'Team: {self.name}')
        print(f'Winning percentage: {self.get_win_percentage()}')


class TestTeam(unittest.TestCase):
    def test_get_win_percentage_Ravens(self):
        team = Team("Ravens", 13, 3)
        self.assertTrue(team.wins == 13)
        self.assertTrue(team.losses == 3)
        self.assertAlmostEqual(team.get_win_percentage(), 0.8125)

    def test_get_win_percentage_Angels(self):
        team = Team("Angels", 80, 82)
        self.assertTrue(team.wins == 80)
        self.assertTrue(team.losses == 82)
        self.assertAlmostEqual(team.get_win_percentage(), 0.4938)

    def test_print_standing_Ravens(self):
        team = Team("Ravens", 13, 3)
        with patch("builtins.print") as mock_print:
            team.print_standing()
            mock_print.assert_any_call("Team: Ravens")
            mock_print.assert_any_call("Winning percentage: 0.8125")
        
    def test_print_standing_Angels(self):
        team = Team("Angels", 80, 82)
        with patch("builtins.print") as mock_print:
            team.print_standing()
            mock_print.assert_any_call("Team: Angels")
            mock_print.assert_any_call("Winning percentage: 0.4938")

    #def test_print_standing(self):
        #self.assertTrue(Team.name == "Ravens")


if __name__ == "__main__":
    #team = Team()
   
    #user_name = input()
    #user_wins = int(input())
    #user_losses = int(input())
    
    #team.name = user_name
    #team.wins = user_wins
    #team.losses = user_losses
    
    #team.print_standing()
    unittest.main()

