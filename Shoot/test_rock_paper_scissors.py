import unittest
from unittest.mock import patch
from io import StringIO
import random
from rock_paper_scissors import bot_name, welcome, play, checking_plays, plays


class TestRockPaperScissors(unittest.TestCase):

    def setUp(self):
        random.seed(42)  # Set seed for reproducible results in random choices

    def test_player_wins_rock_vs_scissors(self):
        with patch('builtins.input', side_effect=['ROCK']):
            bot_play = 'SCISSORS'
            captured_output = StringIO()
            with patch('sys.stdout', new=captured_output):
                checking_plays(bot_play, "Bot")
            self.assertIn("Rock beats scissors, you WON!!", captured_output.getvalue().strip())

    def test_player_wins_paper_vs_rock(self):
        with patch('builtins.input', side_effect=['PAPER']):
            bot_play = 'ROCK'
            captured_output = StringIO()
            with patch('sys.stdout', new=captured_output):
                checking_plays(bot_play, "Bot")
            self.assertIn("Paper beats rock, you WON!!", captured_output.getvalue().strip())

    def test_player_wins_scissors_vs_paper(self):
        with patch('builtins.input', side_effect=['SCISSORS']):
            bot_play = 'PAPER'
            captured_output = StringIO()
            with patch('sys.stdout', new=captured_output):
                checking_plays(bot_play, "Bot")
            self.assertIn("Scissors beats paper, you WON!!", captured_output.getvalue().strip())

    def test_bot_wins_paper_vs_scissors(self):
        with patch('builtins.input', side_effect=['PAPER']):
            bot_play = 'SCISSORS'
            captured_output = StringIO()
            with patch('sys.stdout', new=captured_output):
                checking_plays(bot_play, "Bot")
            self.assertIn("Better luck next, time buddy. Bot WON!", captured_output.getvalue().strip())


    def test_invalid_play(self):
        with patch('builtins.input', side_effect=['INVALID', 'ROCK']):
            bot_play = 'PAPER'
            captured_output = StringIO()
            with patch('sys.stdout', new=captured_output):
                checking_plays(bot_play, "Bot")
            self.assertIn("Invalid play, play again", captured_output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
