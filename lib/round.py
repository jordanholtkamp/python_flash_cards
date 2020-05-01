from lib.turn import Turn

class Round:
  def __init__(self, deck):
    self.deck = deck
    self.turns = []

  def current_card(self):
    cards = self.deck.cards
    return cards[0]

  def take_turn(self, guess):
    turn = Turn(guess, self.current_card())
    self.deck.cards.pop(0)
    self.turns.append(turn)
    return turn
    
  def number_correct(self):
    return len(self.correct_turns())

  def correct_turns(self):
    correct_turn_builder = []
    for turn in self.turns:
      if turn.correct() == True:
        correct_turn_builder.append(turn)
    
    return correct_turn_builder

  def total_turns(self):
    return len(self.turns)

  def number_correct_by_category(self, category):
    counter = 0
    for turn in self.turns:
      if turn.card.category == category and turn.correct():
        counter += 1
    
    return counter
  
  def number_of_turns_by_category(self, category):
    counter = 0
    for turn in self.turns:
      if turn.card.category == category:
        counter += 1
    
    return counter

  def percent_correct(self):
    decimal_value = self.number_correct()/self.total_turns()
    return round(decimal_value * 100, 1)

  def percent_correct_by_category(self, category):
    decimal_value = self.number_correct_by_category(category)/self.number_of_turns_by_category(category)
    return round(decimal_value * 100, 1)