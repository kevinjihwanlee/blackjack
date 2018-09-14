import unittest
from card import Card
from main import Player, generateDeck, dealCard

class BlackjackTests(unittest.TestCase):
  def setUp(self):
    self.deck = generateDeck()
    self.playerOne = Player()
    self.normalCard = Card('Three of Hearts', 3)
    self.faceCard = Card('King of Diamonds', 10)
    self.ace = Card('Ace of Spades', [1, 11])

  def test_deckLength(self):
    self.assertEqual(len(self.deck), 52)

  # def test_uniqueDeck(self):
  #   deck = generateDeck()

  def test_deal(self):
    dealtCard = self.deck[-1]
    dealCard(self.deck, self.playerOne)
    self.assertEqual(dealtCard, self.playerOne.hand[0])
    self.assertEqual(len(self.deck), 51)


  # def test_cardValue(self):
  #   self.assertEqual(self.normalCard)

if __name__ == '__main__':
  unittest.main()