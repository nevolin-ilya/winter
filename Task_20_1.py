import datetime
class Person:
    def __init__(self, name):
        self.name = name
    def take_menu(self):


    def spend_many(self, card, cash):

class Day:
    def __init__(self, work_day, day_off):
        self.work_day = work_day
        self.day_off = day_off
    def calendar(self, work_day, day_off):
        day = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
        dn = datetime.datetime.now()
        dw = d.weekday()
        if day[dw] == day[0:4]:
            return self.work_day
        else:
            return self.day_off

class Menu:
    def __init__(self, cofe, cake):
        self.cofe = cofe
        self.cake = cake

class Pay:
    def __init__(self, card, cash):
        self.card = card
        self.cash = cash

