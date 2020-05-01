import unittest
from lib.card import Card 
from lib.deck import Deck

class TestDeck(unittest.TestCase):
  def test_deck(self):
    card_1 = Card("What is the capital of Alaska?", "Juneau", 'Geography')
    card_2 = Card("What is the square root of 169?", "13", 'STEM')
    card_3 = Card("What is the power house of the freaking cell?", "Mitochondria", 'STEM')

    cards = [card_1, card_2, card_3]

    deck = Deck(cards)

    assert deck.cards == [card_1, card_2, card_3]

    assert deck.count() == 3

    assert deck.cards_in_category('Geography') == [card_1]
    assert deck.cards_in_category('STEM') == [card_2, card_3]
    assert deck.cards_in_category('pop culture') == []

if __name__ == '__main__':
    unittest.main()