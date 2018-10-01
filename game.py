from random import shuffle, seed, choice
from card import Card
from player import Player

class Game(object):
  def __init__(self):
    self.deck = []
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
    staticNames = ['Jihwan', 'Jaesook', 'Seungho']
    for x in range(0, n):
      self.players.append(Player(staticNames[x], False, True))
    dealer = Player('DEALER', True, False)
    self.players.append(dealer)

  def dealCard(self, player):
    if not self.deck:
      raise Exception('ERROR - the deck is empty')
    else:
      player.hand.append(self.deck.pop())
    
  def hit(self, player):
    self.dealCard(player)
    handValue = player.checkHand()
    if player.bust and not player.isAI:
      print '*** You bust with a hand value of {0}. ***'.format(handValue)
  def stand(self, player):
    player.done = True

  def awardWin(self, player, bj):
    if bj:
      print '*** BLACKJACK! {0} has automatically won! ***'.format(player.name)
    else:
      print '*** {0} wins! ***'.format(player.name)
  
  def start(self):
    seed()
    name = raw_input('Enter your name: ')
    self.players.append(Player(name, False, False))
    numPlayers = input('Enter the number of other players (up to 3): ')
    if numPlayers < 1 or numPlayers > 4:
      print '*** Please enter a valid number of players (1 to 3). ***'
      self.start()
    self.generatePlayers(numPlayers)
    self.generateDeck()
    # initial deal
    for x in range(0, 2):
      for player in self.players:
          self.dealCard(player)
    # check initial deal for a blackjack winner
    print '*** INTIIAL DEAL ***'
    for player in self.players:
      player.displayHand()
      handValue = player.checkHand()
      if handValue == 21 and not player.isDealer:
        self.awardWin(player, True)
        return
    # game loop
    gameActive = True
    print '*** GAME START ***'
    while gameActive:
      activePlayers = 0
      for player in self.players:
        if not player.isDealer:
          handValue = player.checkHand()
          if not player.done and not player.bust:
            if player.isAI:
              decisions = [self.hit, self.stand]
              randomDecision = choice(decisions)(player)
            else:
              while True:
                decision = raw_input('Would you like to HIT or STAND? ')
                if decision.lower() == 'hit':
                  self.hit(player)
                  break
                elif decision.lower() == 'stand':
                  self.stand(player)
                  break
                else:
                  print 'Please type a valid action.'
              print '******************'
            if not player.done and not player.bust:
              activePlayers += 1
        player.displayHand()
      print '******************'
      if activePlayers == 0:
        break
    print '*** DEALING ENDS ***'
    dealer = self.players.pop()
    remainingPlayers = []
    for player in self.players:
      if not player.bust:
        remainingPlayers.append(player)
    dealerValue = dealer.checkHand()
    while dealerValue <= 17:
      self.dealCard(dealer)
      dealerValue = dealer.checkHand()
    dealer.isDealer = False
    dealer.displayHand()
    if dealerValue > 21:
      print '*** Dealer bust! ***'
      for player in remainingPlayers:
        print '*** {0} wins! ***'.format(player.name)
    else:
      for player in remainingPlayers:
        playerValue = player.checkHand()
        if playerValue > dealerValue:
          self.awardWin(player, False)
        elif playerValue == dealerValue:
          print '*** {0} ties against DEALER, {1} vs {2}. ***'.format(player.name, playerValue, dealerValue)
        else:
          print '*** {0} loses against DEALER, {1} vs {2}. ***'.format(player.name, playerValue, dealerValue)

      
     
