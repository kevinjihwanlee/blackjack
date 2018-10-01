class Player(object):
  def __init__(self, name, isDealer):
    self.name = name
    self.isDealer = isDealer
    self.hand = []
  
  def displayHand(self):
    if self.isDealer:
      print 'Dealer\'s hand: {0} HIDDEN'.format(self.hand[0].name)
    else:
      display = '{0}\'s hand: '.format(self.name)
      for x in range(0, len(self.hand)):
        display += self.hand[x].name
        if x != len(self.hand)-1:
          display += ', '
      print display
  
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