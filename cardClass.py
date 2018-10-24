class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    VALS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, vals=0):
        self.suit = suit
        self.vals = vals

    def __str__(self):
        """
          >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.VALS[self.vals],
                                   Card.SUITS[self.suit])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
