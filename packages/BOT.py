from packages.Deck import Deck
from packages.Deck import Card

d = Deck()
c = Card()

class Bot:
    def __init__(self):
        self.bot_arms = []
        self.card_score_count_bot = []
        self.lucky_count_score = 0

    def get_card_bot(self, card):
        self.bot_arms.append(card.pop(0))
        return self.bot_arms

    def end_hate_speech(self):
        self.bot_speech_won = ["Ну, жалко что ты конечно проиграл, ну ты же понимаешь,что хороший конец, бывает только в массажном салоне?"]
        self.bot_speech_lose =["Новичкам везёт....", "Фартануло тебе браза, ну ничего, давай дальше пульку расписывать."]

    def bot_clear_arm(self):
        self.bot_arms  = []

    def card_score_bot(self):
        for el in self.bot_arms:
            if el[0].isalpha():
                self.card_score_count_bot.append(c.value_card[el[0]])
            else:
                self.card_score_count_bot.append(int(el[0:2]))

    def card_score_cleaner_bot(self):
        self.card_score_count_bot = []