import unittest
from lib.card import Card 

class TestCard(unittest.TestCase):

  def test_card_attributes(self):
    card = Card("What is the capital of Alaska?", "Juneau", 'Geography')

    assert isinstance(card, Card)
    assert card.question == 'What is the capital of Alaska?'
    assert card.answer == 'Juneau'
    assert card.category == 'Geography'
    
if __name__ == '__main__':
    unittest.main()