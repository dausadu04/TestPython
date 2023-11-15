import random


class Man:

    def __init__(self, name):
        self.name = name
        self.food = 10
        self.fullness = 10
        self.money = 50
        self.perception = 'good'

    def eat(self):
        self.fullness += 10
        self.food -= 10
        self.perception = 'satisfied'
        print(f"{self.name} ate, now {self.perception}")
        print(f"Money - {self.money}, Food - {self.food}, Self-perception - {self.perception}, Fullness - {self.fullness}")


    def work(self):
        self.money += 50
        self.fullness -= 10
        self.perception = 'tired'
        print(f"{self.name} worked, now self-perception is {self.perception}")
        print(f"Money - {self.money}, Food - {self.food}, Self-perception - {self.perception}, Fullness - {self.fullness}")

    def play_the_game(self):
        self.perception = 'great'
        self.fullness -= 10
        print(f"{self.name} played, now self-perception is {self.perception}")
        print(f"Money - {self.money}, Food - {self.food}, Self-perception - {self.perception}, Fullness - {self.fullness}")

    def buying_the_food(self):
        self.money -= 25
        self.food += 25
        self.perception = 'good'
        print(f"{self.name} played, now self-perception is {self.perception}")
        print(f"Money - {self.money}, Food - {self.food}, Self-perception - {self.perception}, Fullness - {self.fullness}")

    def act(self):
        action = random.randint(1, 5)

        if action == 1:
            self.eat()
        elif action == 2:
            if self.fullness < 10:
                if self.money >= 10:
                    self.buying_the_food()
            self.work()
        else:
            if self.fullness < 10:
                if self.money >= 10:
                    self.buying_the_food()
                else:
                    if self.food == 0:
                        print("{} died!".format(self.name))
                    self.eat()
            self.play_the_game()


Daulet = Man('Daulet')
for day in range(1, 31):
    print("==================Day {}==================".format(day))
    Daulet.act()
    print()
