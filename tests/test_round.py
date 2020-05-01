import unittest
from lib.card import Card 
from lib.turn import Turn
from lib.deck import Deck
from lib.round import Round

class TestRound(unittest.TestCase):
  def test_round(self):
    card_1 = Card("What is the capital of Alaska?", "Juneau", 'Geography')
    card_2 = Card("What is the square root of 169?", "13", 'STEM')
    card_3 = Card("What is the power house of the freaking cell?", "Mitochondria", 'STEM')

    cards = [card_1, card_2, card_3]

    deck = Deck(cards)

    round = Round(deck)

    assert round.deck == deck

    assert round.turns == []

    assert round.current_card() == card_1

    new_turn = round.take_turn('Juneau')

    assert isinstance(new_turn, Turn)

    assert new_turn.correct() == True

    assert round.turns == [new_turn]

    assert round.number_correct() == 1

    assert round.current_card() == card_2

    newer_turn = round.take_turn('12')

    assert len(round.turns) == 2
    assert (round.total_turns()) == 2

    assert newer_turn.correct() == False

    assert newer_turn.feedback() == 'Incorrect.'

    assert round.number_correct() == 1

    assert round.number_correct_by_category('Geography') == 1
    assert round.number_correct_by_category('STEM') == 0

    assert round.percent_correct() == 50.0

    assert round.percent_correct_by_category('Geography') == 100.0
    assert round.percent_correct_by_category('STEM') == 0.0

    assert round.current_card() == card_3

if __name__ == '__main__':
    unittest.main()