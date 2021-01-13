from random import randint
from termcolor import cprint


def start():
    class Man:

        def __init__(self, name):
            self.name = name
            self.fullness = 50
            self.house = None

        def __str__(self):
            return 'Я - {}, сытость {}'.format(
                self.name, self.fullness)

        def eat(self):
            if self.house.food >= 10:
                cprint('{} поел'.format(self.name), color='green')
                self.fullness += 10
                self.house.food -= 10
            else:
                cprint('{} нет еды'.format(self.name), color='green')

        def work(self):
            cprint('{} сходил на работу'.format(self.name), color='green')
            self.house.money += 150
            self.fullness -= 10

        def watch_MTV(self):
            cprint('{} смотрел MTV целый день'.format(self.name), color='green')
            self.fullness -= 10

        def shopping(self):
            if self.house.money >= 50:
                cprint('{} сходил в магазин за едой'.format(self.name), color='green')
                self.house.money -= 50
                self.house.food += 50
            else:
                cprint('{} деньги кончились!'.format(self.name), color='green')

        def buy_feed_for_cat(self):
            if self.house.money >= 50:
                cprint('{} сходил в магазин за кормом для кота'.format(self.name), color='green')
                self.house.money -= 50
                self.house.bowl += 50
            else:
                self.work()

        def clean_the_house(self):
            if self.fullness > 20:
                cprint('{} убрался в доме'.format(self.name), color='green')
                self.fullness -= 20
                self.house.mud -= 20
            else:
                cprint('{} закончилась энергия! Не может приступить к уборке'.format(self.name), color='green')

        def go_to_the_house(self, house):
            self.house = house
            self.fullness -= 10
            cprint('{} Вьехал в дом'.format(self.name), color='green')

        def get_cat(self):
            citizens.append(cat)
            cprint('{} подобрал кота и назвал его {}'.format(self.name, cat.name), color='cyan')
            cat.go_to_the_house(house=my_sweet_home)

        def act(self):
            if self.fullness <= 0:
                cprint('{} умер...'.format(self.name), color='red')
                return
            dice = randint(1, 6)
            if self.fullness < 20:
                self.eat()
            elif self.house.food < 10:
                self.shopping()
            elif self.house.bowl < 10:
                self.buy_feed_for_cat()
            elif self.house.money < 50:
                self.work()
            elif dice == 1:
                self.work()
            elif dice == 2:
                self.eat()
            else:
                if cat not in citizens:
                    self.get_cat()
                elif self.house.bowl < 10:
                    self.buy_feed_for_cat()
                elif self.house.mud >= 20:
                    self.clean_the_house()
                else:
                    self.watch_MTV()

    class Cat():

        def __init__(self, name):
            self.name = name
            self.fullness = 50
            self.house = None

        def __str__(self):
            return 'Я - {}, сытость {}'.format(
                self.name, self.fullness)

        def go_to_the_house(self, house):
            self.house = house
            self.fullness -= 10
            cprint('{} теперь живет с людьми в одном доме'.format(self.name), color='cyan')

        def sleep(self):
            self.fullness -= 10
            cprint('{} спит'.format(self.name), color='cyan')

        def eat(self):
            self.fullness += 20
            self.house.bowl -= 10
            cprint('{} кушает'.format(self.name), color='cyan')

        def tears_wallpaper(self):
            self.fullness -= 10
            self.house.mud += 5
            cprint('{} дерет обои'.format(self.name), color='cyan')

        def act(self):
            if self.fullness <= 0:
                cprint('{} умер...'.format(self.name), color='red')
                return
            dice = randint(1, 6)
            if self.fullness < 20:
                self.eat()
            elif dice == 1:
                self.tears_wallpaper()
            else:
                self.sleep()

    class House:

        def __init__(self):
            self.food = 50
            self.money = 0
            self.bowl = 0
            self.mud = 0

        def __str__(self):
            return 'В доме еды осталось {}, денег осталось {}, еды в миске осталось {}, грязь {}'.format(
                self.food, self.money, self.bowl, self.mud)

    citizens = [
        Man(name='Бивис'),
        Man(name='Батхед'),
        Man(name='Кенни'),
    ]
    cat = Cat(name='Кот')

    my_sweet_home = House()
    for citisen in citizens:
        citisen.go_to_the_house(house=my_sweet_home)

    for day in range(1, 366):
        print('================ день {} =================='.format(day))
        for citisen in citizens:
            citisen.act()
        print('--- в конце дня ---')
        for citisen in citizens:
            print(citisen)
        print(my_sweet_home)


if __name__ == '__main__':
    start()
