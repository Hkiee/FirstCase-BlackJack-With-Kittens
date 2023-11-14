import time
from packages.Player import Player
from packages.BOT import Bot
from packages.Deck import Deck
from packages.Deck import Card

p = Player()
b = Bot()
d = Deck()
c = Card()


# КЛАСС С ОПИСАНИЕМ ИГРОВОЙ ЛОГИКИ.
class Game:
    def __init__(self):
        self.game_name = "BlackJack with Kittens."  # ПРИ СОЗДАНИИ ИМЕНИ ИГРЫ НИ ОДИН КОТЁНОК НЕ ПОСТРАДАЛ

    def loop_game(self): # Такая  же функция как starting_game()  только без создания колоды.
        d.back_to_deck(p.arms, b.bot_arms)
        p.clear_arm()
        b.bot_clear_arm()
        d.shuffle_deck()
        print("*Перемешивание колоды...*")
        time.sleep(1.2)
        return self.cards_for_the_suits()

    def wanna_play_one_more_time(self):#  Функция с преедложением сыграть ещё игру
        print("Распишем ещё одну пульку?")
        a = input("Да / Нет : ")
        if a.lower() == "да":
            return self.loop_game()
        if a.lower() == "нет":
            return "Ну, спасибо. Хорошо скоротал время."
        else:
            print("Ну так ты ответь нормально мне...")
            return self.wanna_play_one_more_time()


    def who_won_compare_arms(self, p1, p2): # Функция сравнивания рук игрока и оппонента для вывода информации о том кто победил
        if p1 > p2:
            print("Вы победили!")
        if p1 < p2:
            print("Вы проиграли!")
        if p1 == p2:
            print("Ничья!")
        return p.card_score_cleaner(), b.card_score_cleaner_bot(), self.wanna_play_one_more_time()



    def show_cards_end_game(self): # Функция для вывода состояния рук оппонента и игрока. Передача данных для вывода информации определения победителя
        p.card_score()
        print(f"Ваша рука {p.arms}. Суммарный счёт  карт = {sum(p.card_score_count)}")
        b.card_score_bot()
        print(f"Рука вашего оппонента {b.bot_arms}. Суммарный счёт карт = {sum(b.card_score_count_bot)}")
        return self.who_won_compare_arms(sum(p.card_score_count), sum(b.card_score_count_bot))




    def end_quest_for_open(self): # Призыв к выходу на этап конца игры
        print("Ну... тогда может раскрываемся?")
        a = input("Да / Нет :")
        if a.lower() == "да":
            return self.show_cards_end_game()
        if a.lower() == "нет":
            print("Не ну чё ты такой размазной. Раскрываемся и тчк.")
            return self.show_cards_end_game()
        else:
            print("Чего ты там бухтишь? Чётче говори.")
            return self.show_cards_end_game()

    def second_game_stage_add_cards(self): # Функция с выводом предложения взять карту
        print("Нужна ещё карта?")
        a = input("Да / Нет : ")
        if a.lower() == "да":
            p.get_card(d.all_cards)
            self.foo_for_return_result_player_arms()
            return  self.second_game_stage_add_cards()
        if a.lower() == 'нет':
            return self.end_quest_for_open()

        else:
            print("Ну что ты опять мямлишь а? А может тебе.....")
            time.sleep(1.2)
            return self.second_game_stage_add_cards()

    def first_game_stage_get_four_cards_from_deck(self):  # ВЫЗОВ ФУНКЦИИ РАВНОМЕРНОЙ РАЗДАЧИ КАРТ. ВЫЗОВ ФУНКЦИИ ФОРМИРОВАНИЯ ЦИФРОГО СЧЁТА КАРТ
        self.cycle_func_for_get_card(2)  # ВЫВОД В ТЕРМИНАЛ ИНФОРМАЦИЮ О ВАШЕЙ РУКЕ И ЕЁ СУММАРНОМ СЧЁТЕ
        self.foo_for_return_result_player_arms()
        return self.second_game_stage_add_cards()

    def cards_for_the_suits(
            self):  # ВО ВРЕМЯ ПЕРЕМЕШИВАНИЯ КОЛОДЫ ОППОНЕНТ СПРАШИВАЕТ СДАТЬ КОЛОДУ ПОД РУБАШКУ ( В БУДУЩЕМ БУДЕТ ВЛИЯТЬ НА ЛАКИ КАУНТ)
        print("Ну-ка, сдайка мне колоду под рубашку")  # ПРИ ОТКАЗЕ ШАНС БЫТЬ ШУЛЕРОМ НИЖЕ
        a = input("Сдать оппоненту под рубашку? Да / Нет: ")
        if a.lower() == "да":
            d.all_cards = d.all_cards[26:] + d.all_cards[0:27]
            return self.first_game_stage_get_four_cards_from_deck()
        if a.lower() == "нет":
            print("Ну,понятно что ты за фрукт, буду пристально следить за тобой")
            print("*Вы чувствуете пристальный, презренный взгляд. Оппонент словно охватывает вас взглядом до кончиков пальцев*")

    def starting_game(self, card, deck):  # ЭТАП ФОРМИРОВАНИЯ КОЛОДЫ
        d.deck_builder(c.ranks, c.suits)
        d.shuffle_deck()
        print("*Перемешивание колоды...*")
        time.sleep(1.2)
        return self.cards_for_the_suits()

    def start_game_answer_for_your_speech(self):  # ОЖИДАНИЕ ОТВЕТА НА ВОПРОС ПРЕДЛОЖЕНИЯ К ИГРЕ
        a = input("Да /  Нет :")
        if a.lower() == "да":
            return self.starting_game(c, d)

        if a.lower() == "нет":
            return print("Ну ладно, бывай тогда. Мир тебе.")

        else:
            print("Ну чё ты там мямлишь, так будем играть или нет?")
            return self.start_game_answer_for_your_speech()

    def start_game_question(self):  # ВОПРОС С ПРИЗЫВОМ К ИГРЕ...
        print(f"Сыграем с тобой в игру под названием : {self.game_name}?")
        return self.start_game_answer_for_your_speech()

    def foo_for_return_result_player_arms(self): # Промежуточная функция для быстрого выполнения ряда функнций по  вычислению  количества  балов Игрока
        p.card_score()
        print(f"Ваша рука {p.arms}. Суммарный счёт  карт = {sum(p.card_score_count)}")
        p.card_score_cleaner()

    def foo_for_return_result_bot_arms(self): # Промежуточная функция для быстрого выполнения ряда функнций по  вычислению  количества  балов БОТА
        b.card_score_bot()
        print(f"Рука вашего оппонента {b.bot_arms}. Суммарный счёт карт = {sum(b.card_score_count_bot)}")
        b.card_score_cleaner_bot()

    def cycle_func_for_get_card(self, card_count):  # ФУНКЦИЯ РАВНОМЕРНОГО РАЗДАЧИ КАРТУ ИГРОКУ И БОТУ
        i = 0
        while i < card_count:
            p.get_card(d.all_cards)
            b.get_card_bot(d.all_cards)
            i += 1