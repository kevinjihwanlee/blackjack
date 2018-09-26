import unittest
from card import Card
from main import Player, generateDeck, dealCard

class BlackjackTests(unittest.TestCase):
  def setUp(self):
    self.deck = generateDeck()
    self.dealer = Player('DEALER', True)
    self.playerOne = Player('Kevin', False)
    self.normalCard = Card('Three of Hearts', 3)
    self.faceCard = Card('King of Diamonds', 10)
    self.ace = Card('Ace of Spades', [1, 11])

  def test_deckLength(self):
    self.assertEqual(len(self.deck), 52)

  def test_uniqueDeck(self):
    unique = []
    for card in self.deck:
      self.assertFalse(card in unique)
      unique.append(self.deck.pop())

  def test_deal(self):
    dealtCard = self.deck[-1]
    dealCard(self.deck, self.playerOne)
    self.assertEqual(dealtCard, self.playerOne.hand[0])
    self.assertEqual(len(self.deck), 51)

  def test_cardValue(self):
    self.assertEqual(self.normalCard.value, 3)
    self.assertEqual(self.faceCard.value, 10)
    self.assertTrue(1 or 11 in self.ace.value)
  
  

if __name__ == '__main__':
  unittest.main()