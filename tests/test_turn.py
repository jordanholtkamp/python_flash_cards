import unittest
from lib.card import Card 
from lib.turn import Turn

class TestTurn(unittest.TestCase):

  def test_turn(self):
    card = Card("What is the capital of Alaska?", "Juneau", 'Geography')

    turn = Turn('Juneau', card)

    assert turn.card == card
    assert turn.guess == 'Juneau'
    assert turn.correct() == True
    assert turn.feedback() == 'Correct!'

  def test_incorrect_guess(self):
    card = Card("What is the capital of Alaska?", "Juneau", 'Geography')
    turn = Turn('Juno', card)

    assert turn.correct() == False
    assert turn.feedback() == 'Incorrect.'

if __name__ == '__main__':
  unittest.main()