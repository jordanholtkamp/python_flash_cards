class Deck:
  def __init__(self, cards):
    self.cards = cards

  def count(self):
    return len(self.cards)

  def cards_in_category(self, category):
    card_list = []
    for card in self.cards:
      if card.category == category:
        card_list.append(card)
    
    return card_list

  def all_categories(self):
    categories = []
    for card in self.cards:
      if card.category not in categories:
        categories.append(card.category)
    
    return categories