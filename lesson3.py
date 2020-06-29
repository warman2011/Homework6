class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

        def get_full_name(self):
            print('Staff full name: ', self.name, self.surname)

        def get_total_income(self):
            print('Total income: ', sum(self._income.values()))

a = Position('Ivan', 'Ivanov', 'Principal',10000, 5000)
a.get_full_name()
a.get_total_income()

