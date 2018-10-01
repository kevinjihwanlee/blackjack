from random import shuffle
from card import Card
from player import Player

class Game(object):
  def __init__(self):
    self.deck = None
    self.players = []
  
  def generateDeck(self):
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
    self.deck = deck
  
  def generatePlayers(self, n):
    staticNames = ['Kevin', 'Jihwan', 'Jaesook', 'Seungho']
    dealer = Player('DEALER', True)
    self.players.append(dealer)
    for x in range(0, n):
      print staticNames[x]
      self.players.append(Player(staticNames[x], False))

  def dealCard(self, player):
    player.hand.append(self.deck.pop())
    # todo - edge case of deck being empty
  
  def start(self):
    numPlayers = input('Enter the number of players (including yourself) from 1 to 4: ')
    if numPlayers < 1 or numPlayers > 4:
      print '*** Please enter a valid number of players (1 to 4). ***'
      self.start()
    self.generatePlayers(numPlayers)
    self.generateDeck()
    # initial deal
    for x in range(0, 2):
      for player in self.players:
          self.dealCard(player)
    # game loop
    while True:
      for player in self.players:
        player.displayHand()
      decision = input('Do you ')

    # self.displayHand(self.players[2])