from random import shuffle
from card import Card

class Player(object):
  def __init__(self, name, isDealer):
    self.name = name
    self.isDealer = isDealer
    self.hand = [] 
  
# class Game(object):
#   def __init__(self):
#     self.players = []

def generateDeck():
  deck = []
  for suit in ['Diamonds', 'Clubs', 'Hearts', 'Spades']:
    for sym in ['Ace', 'Jack', 'Queen', 'King']:
      name = sym + ' of ' + suit
      value = 10 if sym != 'Ace' else [1, 11]
      deck.append(Card(name, value))
    for num in range(2, 11):
      name = str(num) + ' of ' + suit
      value = num
      deck.append(Card(name, value))
  shuffle(deck)
  return deck

def dealCard(deck, player):
  player.hand.append(deck.pop())

def displayHand(player):
  if player.isDealer:
    print 'Dealer\'s hand: {0} HIDDEN'.format(player.hand[0].name)
  else:
    display = '{0}\'s hand: '.format(player.name)
    for x in range(0, len(player.hand)):
      display += player.hand[x].name
      if x != len(player.hand)-1:
        display += ', '
    print display

if __name__ == '__main__':
  deck = generateDeck()
  dealer = Player('John', True)
  playerOne = Player('Kevin', False)

  players = []
  players.append(dealer)
  players.append(playerOne)
  for x in range(0, 2):
    for player in players:
      dealCard(deck, player)
  displayHand(dealer)
  displayHand(playerOne)
  







  