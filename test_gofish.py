import unittest
import gofish

class TestGoFish(unittest.TestCase):
    # general use test
    def test1_getCard(self):
        deck = _createDeck()
        initlen = len(deck)
        for x in range(0, len(deck)):
            card = gofish.getCard(deck)
            self.assertTrue(card not in deck) # check the correct card got deleted
            self.assertTrue(initlen == len(deck) + x + 1) # check that only one card got deleted
    
    # Test that we get expected cards back (only one type of card)
    def test2_getCard(self):
        deck = _createDeck(rank=[2,2,2,2,2,2], suit=["spades", "spades", "spades", "spades"])
        initlen = len(deck)
        for x in range(0, len(deck)):
            card = gofish.getCard(deck)
            self.assertTrue(card == (2, "spades")) 
            self.assertTrue(initlen == len(deck) + x + 1) 

    # Saturation test to make sure drawCard doesn't go outside the bounds of the deck
    def test3_getCard(self):
        deck = _createDeck()
        initlen = len(deck)
        for x in range(0, 1000000):
            for x in range(0, len(deck)):
                card = gofish.getCard(deck)
                self.assertTrue(card not in deck)
                self.assertTrue(initlen == len(deck) + x + 1)

    # general use test
    def test1_drawCard(self):
        deck = _createDeck()
        players = {"Jim": _createHand(), "Kathy": _createHand(), "Zach": _createHand()}
        for x in range(0, len(deck)):
            for name in players.keys():
                gofish.drawCard(name, deck, players[name])
                for rank in players[name]:
                    self.assertTrue(len(rank) > 0 and len(rank) < 4) # check that no rank has less 0 or 4+ suits  

    # test to make sure the hand doesn't empty at all
    def test2_drawCard(self):
        deck = _createDeck(rank=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
                            suit=["spades", "hearts", "clubs"])
        players = {"Jim": _createHand()}
        for x in range(0, len(deck)):
            for name in players.keys():
                gofish.drawCard(name, deck, players[name])
        self.assertTrue(len(players["Jim"]) == 13)

    # test to make sure the hand empties completely
    def test3_drawCard(self):
        deck = _createDeck(rank=["2", "3", "4"], suit=["spades", "hearts", "clubs", "diamonds"])
        players = {"Jim": _createHand()}
        for x in range(0, len(deck)):
            for name in players.keys():
                gofish.drawCard(name, deck, players[name])
        self.assertTrue(len(players["Jim"]) == 0) 

def _createDeck(rank=[], suit=[]):
    deck = []
    if not rank:
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    if not suit:
        suit = ["spades", "hearts", "diamonds", "clubs"]
    for x in range(0, len(rank)):
        for y in range(0, len(suit)):
            deck.append((rank[x], suit[y]))
    return deck

def _createHand():
    hand = {}
    return hand

if __name__ == '__main__':
    unittest.main()