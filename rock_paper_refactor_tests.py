import unittest
from unittest.mock import patch
from rock_paper_refactor import *


hartie = 1 
piatra = 2  
foarfeca = 3

class TestCastigator(unittest.TestCase):
    def test_same_choice(self):
        self.assertEqual(castigator(hartie, hartie), "Egalitate!")
        self.assertEqual(castigator(piatra, piatra), "Egalitate!")
        self.assertEqual(castigator(foarfeca, foarfeca), "Egalitate!")

    def test_player1_wins(self):
        self.assertEqual(castigator(hartie, piatra), "Player 1 a castigat runda aceasta!")
        self.assertEqual(castigator(foarfeca, hartie), "Player 1 a castigat runda aceasta!")
        self.assertEqual(castigator(piatra, foarfeca), "Player 1 a castigat runda aceasta!")

    def test_player2_wins(self):
        self.assertEqual(castigator(piatra, hartie), "Player 2 a castigat runda aceasta!")
        self.assertEqual(castigator(hartie, foarfeca), "Player 2 a castigat runda aceasta!")
        self.assertEqual(castigator(foarfeca, piatra), "Player 2 a castigat runda aceasta!")



class TestAlegere(unittest.TestCase):
    def test_alegere(self):
        self.assertEqual(alegere(1), 'Ai ales hartie')
        self.assertEqual(alegere(2), 'Ai ales piatra')
        self.assertEqual(alegere(3), 'Ai ales foarfeca')

@patch('builtins.input', side_effect=[1, 2, 'nu'])
class TestMain(unittest.TestCase):
    def test_main(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call('Ai ales hartie')
            mock_print.assert_any_call('Ai ales piatra')
            mock_print.assert_any_call('Jucator 1 a castigat cu 1 runde')

if __name__ == '__main__':
    unittest.main()
