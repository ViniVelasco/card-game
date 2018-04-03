from random import shuffle
class Card:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, value, suit):
        if value not in Card.values:
            raise ValueError(f"You can't have a {value} card!")
        if suit not in Card.suits:
            raise ValueError(f"You can't have a {suit} card!")
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        self.cards = [Card(value, suit) for suit in suits for value in values]
    
    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"
    
    def _deal(self, number):
        current_cards = self.count()
        actual = min([current_cards, number])

        if current_cards == 0:
            raise ValueError("All cards have been dealt")

        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    
    def shuffle(self):
        if(self.count() != 52):
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self.cards

    def deal_card(self):
        card = self._deal(1)[0]
        return card
    
    def deal_hand(self, number):
        hand = self._deal(number)
        return hand


c = Card("A", "Hearts")
d = Deck()

print(len(d.cards))
print(d.cards[26])
#print(d._deal(52))
print(d.count())
print(d.shuffle())
print(d.deal_card())
print(d.count())
print(d.deal_hand(5))
#print(d._deal(1))