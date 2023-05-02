# Напишите генератор, который на вход получает список чисел и возвращает только те числа, которые делятся на 3 без остатка.

def generat(list1):
    for i in list1:
        if i % 3 == 0:
            yield i


list123 = [1, 3, 6, 7, 8, 9, 2, 12]

lst2 = generat(list123)
for i in lst2:
    print(i)



# Напишите генератор, который на вход получает два списка чисел и возвращает только те числа, которые есть в обоих списках.

def gen3(lst1, lst2):
    for i in lst1:
        if i in lst2:
            yield i


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8]

lstw = gen3(list1, list2)

for i in lstw:
    print(i)

# Напишите генератор, который на вход получает список строк и возвращает только те строки, которые содержат букву "a"

def generat4(str1spis):
    for i in str1spis:
        if 'a' in i:
            yield i


spis1 = ['string1', 'dragon', 'worlda', 'BMW']
spis2 = generat4(spis1)
for i in spis2:
    print(i)


# Напишите итератор, который на вход получает список чисел и возвращает каждый третий элемент этого списка
class box:

    def __init__(self, list1):
        self.lst1 = list1

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < len(self.lst1):
            resut = self.lst1[self.value]
            self.value += 3
            return resut
        else:
            raise StopIteration


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
str2 = box(lst1)
for i in str2:
    print(i)


# Реализуйте итератор колоды карт (52 штуки) CardDeck.
# Каждая карта представлена в виде строки типа «2 Пик».
# При вызове функции next() будет представлена
# следующая карта. По окончании перебора всех
# лементов возникнет ошибка StopIteration.

class cardDeck:
    cards = []

    def __init__(self):
        self.value = 0
        suits = ['пик', 'треф', 'бубен', 'червей']
        nominals = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
        for i in nominals:
            for j in suits:
                self.cards.append(f'{i},{j}')

    def __iter__(self):

        return self

    def __next__(self):
        if self.value < len(self.cards):
            result = self.cards[self.value]
            self.value += 1
            return result
        else:
            raise StopIteration

    def next(self):
        curent = self.cards[self.value]
        if curent in self.cards:

            self.value += 1

            print(self.cards[self.value])



car1 = cardDeck()
car1.next()
car1.next()
car1.next()
car1.next()