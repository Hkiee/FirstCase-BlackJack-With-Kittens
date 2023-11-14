from packages.Deck import Deck
from packages.Deck import Card

d = Deck()
c = Card()


class Player(): # Пишем возможности игрока в игре
    def __init__(self):
        self.arms = []
        self.card_score_count = []
        self.lucky_count = 0

    def get_card(self, card):
        self.arms.append(card.pop(0))
        return self.arms

    def clear_arm(self):
        self.arms = []

    def card_score(self):
        for el in self.arms:
            if el[0].isalpha():
                self.card_score_count.append(c.value_card[el[0]])
            else:
                self.card_score_count.append(int(el[0:2]))

    def card_score_cleaner(self):
        self.card_score_count = []