class Player(object):
  def __init__(self, name, isDealer, isAI):
    self.name = name
    self.isDealer = isDealer
    self.isAI = isAI
    self.hand = []
    self.handValue = 0
    self.done = False
    self.bust = False
  
  def displayHand(self):
    # todo - add status information
    if self.isDealer:
      print 'Dealer\'s hand: {0} HIDDEN'.format(self.hand[0].name)
    else:
      display = '{0}\'s hand: '.format(self.name)
      for x in range(0, len(self.hand)):
        display += self.hand[x].name
        if x != len(self.hand)-1:
          display += ', '
      handValue = self.checkHand()
      display += ' (Max value: {0}) '.format(handValue)
      if self.done:
        display += '(DONE)'
      elif self.bust:
        display += '(BUST)'
      print display
    
  def checkHand(self):
    handValue = 0
    for card in self.hand:
      # assume maximum value of ace first
      if isinstance(card.value, (list,)):
        handValue += card.value[1]
      else:
        handValue += card.value
      if handValue > 21:
        # see if hand value can be lower than 21 with previous aces treated as 1
        for a in self.hand:
          if a.name == 'Ace':
            handValue -= 10
            if handValue <= 21:
              break
        # check if hand value still too large after ace readjustment
        if handValue > 21:
          self.bust = True
    return handValue

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    self._name = name

  @property
  def isDealer(self):
    return self._isDealer 
  
  @isDealer.setter
  def isDealer(self, isDealer):
    self._isDealer = isDealer

  @property
  def bust(self):
    return self._bust

  @bust.setter
  def bust(self, bust):
    self._bust = bust
  
  @property
  def done(self):
    return self._done
  
  @done.setter
  def done(self, done):
    self._done = done