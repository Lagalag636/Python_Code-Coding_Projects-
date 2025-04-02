import unittest
from Winning_team_percentage import Team

'''Ravens
13
3 
where Ravens is the team's name, 13 is the number of team wins, and 3 is the number of team losses, the output is:

Win percentage: 0.81
Congratulations, Team Ravens has a winning average!
Ex: If the input is:

Angels
80
82
the output is:

Win percentage: 0.49
Team Angels has a losing average.
'''

class TestTeam(unittest.TestCase):
    def test_get_win_percentage(self):
        team = Team()
        team.wins = 8
        team.losses = 2
        self.assertAlmostEqual(team.get_win_percentage(), 0.8)

    def test_print_standing(self):
        team = Team()
        team.name = "Test Team"
        team.wins = 8
        team.losses = 2
        with self.assertLogs(level='INFO') as log:
            team.print_standing()
            self.assertIn('Team: Test Team', log.output[0])
            self.assertIn('Winning percentage: 0.8', log.output[0])

if __name__ == '__main__':
    unittest.main()
