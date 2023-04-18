class Tomato:
    states = {
        1: 'начальная',
        2: 'средняя',
        3: 'заключительная',
        4: 'салат'
    }

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[1]

        # print(f'{self._index}  {self._state}')

    def grow(self):
        now_state = self._state
        d = Tomato.states
        for k, v in d.items():
            if now_state == v:
                self._state = Tomato.states[k + 1]

        print(f'{self._index}  {self._state}')

    def is_ripe(self):
        return self._state == Tomato.states[4]


class TomatoBrush:
    counter = 0

    def __init__(self, counttomatos):
        self.xtomatos = [Tomato(TomatoBrush.counter) for _ in range(counttomatos)]
        TomatoBrush.counter += 1

    def grow_all(self):
        for i in self.xtomatos:
            i.grow()

    def all_are_ripe(self):
        for i in self.xtomatos:
            if i.is_ripe():
                return True

    def give_away_all(self):
        self.xtomatos.clear()


class Gardner:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe() == True:
            self._plant.give_away_all()
            print('урожай собран')
        else:
            print('еще не выросли')

    @staticmethod
    def knowledge_base():
        print('Садоводство супер')


if __name__ == "__main__":
    Tomats = TomatoBrush(3)
    Tomats2 = TomatoBrush(5)

    gard1 = Gardner('Ivan', Tomats)
    gard2 = Gardner('Anton', Tomats2)
    gard1.knowledge_base()

    gard1.work()
    gard2.work()
    gard1.work()
    gard1.work()
    gard1.harvest()
    gard2.work()
    gard2.harvest()