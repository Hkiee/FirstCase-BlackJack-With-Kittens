from random import shuffle

class Card: # Пишем свойства карт
    def __init__(self):
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
        self.suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
        self.value_card = {"A": 11, "K": 4, "Q": 3, "J": 2}

class Deck: # Пишем логику колоды и работу с ней
    def __init__(self): # Обозначение колоды, изначально он пуста
        self.all_cards = []

    def cards_to_deck(self, arm): # Функция возврата карта в колоду
        for el in arm:
            self.all_cards.append(arm.pop(el))

    def deck_builder(self, ranks, suits): # Функция которая сформирует нам колоду, вызывается 1 раз
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(f"{rank} of {suit}")
        return self.all_cards

    def shuffle_deck(self): # Функия перремешивания колоды
        shuffle(self.all_cards)
        return self.all_cards

    def back_to_deck(self,p1, p2):
        for el in p1:
            self.all_cards.append(el)
        for el in p2:
            self.all_cards.append(el)