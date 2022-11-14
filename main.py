from random import *
from time import *
class Heros():
    def __init__(self, health, stamina, hunger, strenth):
        self.health = health
        self.stamina = stamina
        self.hunger = 100
        self.strenth = strenth

class Villagers():
    def __init__(self, health, hunger, happyness):
        self.health = health
        self.hunger = hunger
        self.happyness = happyness

class Animals():
    def __init__(self, health, damage):
        self.haelth = health
        self.damage = damage

class objects():
    def __init__(self, importance, weight):
        self.importance = importance
        self.weight = weight




def berries(num):
    p = ["1", "2", "3", "4", "5"]
    hung = 0
    while True:
        print(p)
        a = input("Введите номер куста в котором вы хотите пошарить")
        s = randint(0, 5)
        d = randint(1, 10)
        heal = 0
        if d == 7:
            print("Вы оказались таким неуклюжим что упали в куст и исцарапались\n Здоровье -10 ")
            heal = heal - 10
        if s != 0:
            print(f"Поздравляю, вы наш {s} ягод(ы)\nГолод: +{2 * s}")
            hung = hung + (s * 2)
        else:
            print("Увы, в кусте не оказалось ягод")
        p.remove(a)
        if p == []:
            break
    return hung

def shalash(self):
    print("Сейчас ваня находится в шалаше для создания лаборатории ему требуется 30 "
          "дерева для стен, 15 камней для фундамента")
    weapon = ["1 - Чтото похожее на топор", "2 - Длинная палка", "3 - Кусок крепкого камня"]
    wood = 30
    stone = 15
    while True:
        sleep(1)
        if wood <= 0:
            print("Ваня нарубил достаточное колво дров")
        else:
            print(f"Осталось нарубить {wood} единиц дров")
        if stone <= 0:
            print("Ваня смог добыть достаточнок кол-во камня")
        else:
            print(f"Ване осталось добыть {stone} единиц камня")
            start = input("Куда пойти ване?\n1)В лес\n2)В пещеру")
            if start == '1':
                pick = int(input(f"В шалаше есть {weapon}\nЧто ваня выберет?"))
                picked = weapon[pick-1]
                sleep(1)
                while True:
                    if pick == 1:
                        amou = randint(5, 10)
                        sleep(1)
                        print(f"Ваня взял {picked} ")
                        sleep(1)
                        print(f"Ваня нарубил {amou} дров, осталось {wood - amou} дров")
                        wood -= amou
                        break
                    else:
                        print("Хмм ваня не считает что это хороший выбор")
                        break
            elif start == '2':
                pick = int(input(f"В шалаше есть {weapon}\nЧто ваня выберет?"))
                picked = weapon[pick-1]
                sleep(1)
                while True:
                    if pick == 3:
                        amou = randint(3, 6)
                        print("Хмм вроде крепким камнем можно легко дробить другие камни,\n"
                              "вот только долго это все будет")
                        print(f'Удалось добыть {amou} камней\nОсталось {stone - amou}')
                        stone -= amou
                        break
                    else:
                        print('Ване кажется, это плохая идея')
                        break
        if wood and stone <= 0:
            print("Поздравляю вы смогли добыть достаточное колво ресурсов")
            break

def fight(self):

