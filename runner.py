from lib.card import Card
from lib.turn import Turn
from lib.deck import Deck
from lib.round import Round

card_1 = Card("In what state is Greendale Community College?", "colorado", 'Community Trivia')
card_2 = Card("What is the first name of the character that wins Dungeons and Dragons in the first D&D episode?", "pierce", 'Community Trivia')
card_3 = Card("What is the slogan of the STD fair?", "catch knowledge", 'Community Trivia')
card_4 = Card('According to Greek mythology, who was the first woman on Earth?', 'pandora', 'Random Trivia')
card_5 = Card('Two US States dont recognize daylight savings. Hawaii is one. What is the other?', 'arizona', 'Random Trivia')
card_6 = Card('The ____ is the loudest animal on Earth.', 'sperm whale', 'Random Trivia')

cards = [card_1, card_2, card_3, card_4, card_5, card_6]
deck = Deck(cards)
round = Round(deck)
total_cards = len(cards)
categories = deck.all_categories()

intro = "Welcome to Flashcards! You are playing with %s cards" % total_cards
print(intro)

while len(cards) > 0:
  print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
  print('This is card number %s out of %s' % (total_cards - len(cards) + 1, total_cards))
  print('Question: %s' % round.current_card().question)

  guess = input('>>').lower()
  
  guess = round.take_turn(guess)
  answer = guess.card.answer

  print("%s" % round.turns[-1].feedback())


  if guess.correct() == False:
    print('The answer is %s' % answer)

print("****** Game over! ******")
print("Here is how you did overall:")
print('You had %s guesses correct out of %s questions for an overall score of %s' % (round.number_correct(), total_cards, round.percent_correct()))
print('------------------------------')
print('Here is how you did by category:')

for category in categories:
  print('%s: %s' % (category, round.percent_correct_by_category(category)))