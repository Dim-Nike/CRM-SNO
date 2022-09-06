from termcolor import cprint

PM1 = 'Наполнение контента'
PM2 = 'Менеджер по продажам'
PM3 = 'Системный администратор'
PM4 = 'PM менеджер'
PM5_0 = 'Разработчик'
PM5 = ['Backend', 'Frontend', 'ML', 'Верстальщик', 'FullStack', 'Web дизайнер']
stage_project = {0: 'Введутся переговоры',
                 1: 'Подписание договора',
                 2: 'В разработке',
                 3: 'Сдача проекта',
                 4: 'Проект закрыт'}


class Person:
    def __init__(self, name, lvl, date=False, rate=200, myself='Отсуствует', link='Отсуствует'):
        self.name = name
        self.myself = myself
        self.lvl = lvl
        self.date = date
        self.count_project = []
        self.payment = 0
        self.active_project = []
        self.link = link

        self.rate = rate

    def show_self(self):
        count_project = self.count_project if self.count_project != [] else 'Отсуствует'
        count_active_project = self.active_project if self.active_project != [] else 'Отсуствует'
        cprint(f'{self.name}\n'
               f'Дата вступление: {self.date}\n'
               f'Опыт/стэк технологий: {self.myself}\n'
               f'Активные проекты: {count_active_project}\n'
               f'Проекты: {count_project}\n'
               f'Всего проектов: {len(self.count_project)}\n'
               f'Ставка в час: {self.rate}\n'
               f'Выплаты: {self.payment}\n'
               f'Ссылка: {self.link}', 'cyan')

    def __str__(self):
        return self.name


class Project:
    def __init__(self, name, descriptions, date, stage=0, price=None):
        self.name = name
        self.descriptions = descriptions
        self.date = date
        self.price = price
        self.notes = 'Отсуствует'
        self.date_end = 0
        self.personnel_persons = {
            PM1: None,
            PM2: None,
            PM3: None,
            PM4: None,
            PM5_0: {PM5[0]: None,
                    PM5[1]: None,
                    PM5[2]: None,
                    PM5[3]: None,
                    PM5[4]: None}
        }
        self.persons = []
        self.tasks = {}
        self.stage = stage_project[stage]
        self.estimate = dict(amount_back=0, amount_front=0, amount_ml=0, amount_layout_designer=0, amount_fullstack=0,
                             amount_designer=0, amount_pm=0, amount_promotion=0, amount_system_admin=0, amount_sale=0,
                             amount_admin=0, amount_project=0)

    def add_persons(self, list_person, list_add):
        if len(list_add) == 10:
            for new_person in list_add:
                if list_person[new_person].name == 'Отсуствует':
                    continue
                else:
                    self.persons.append(list_person[new_person])

            self.personnel_persons[PM1] = list_person[list_add[0]]
            self.personnel_persons[PM2] = list_person[list_add[1]]
            self.personnel_persons[PM3] = list_person[list_add[2]]
            self.personnel_persons[PM4] = list_person[list_add[3]]
            self.personnel_persons[PM5_0][PM5[0]] = list_person[list_add[4]]
            self.personnel_persons[PM5_0][PM5[1]] = list_person[list_add[5]]
            self.personnel_persons[PM5_0][PM5[2]] = list_person[list_add[6]]
            self.personnel_persons[PM5_0][PM5[3]] = list_person[list_add[7]]
            self.personnel_persons[PM5_0][PM5[4]] = list_person[list_add[8]]
            self.personnel_persons[PM5_0][PM5[5]] = list_person[list_add[9]]

            for person in self.persons:
                if person == 'Отсуствует':
                    continue
                person.count_project.append(self.name)

            if self.stage != 'Проект закрыт':
                for person in self.persons:
                    if person == 'Отсуствует':
                        continue
                    person.active_project.append(self.name)

        else:
            print(f'В проект {self.name} введен неккоректный список данных')

    def add_notes(self, note):
        if not note:
            self.notes = 'Отсуствует'
        else:
            self.notes = note

    def add_task(self, person, task, date_start, date_end):
        self.tasks[self.personnel_persons[PM5_0][person]] = [task, date_start, date_end]

    def show_persons(self):
        for person in self.personnel_persons:
            if self.personnel_persons[person] is None:
                print(f'В проекте нет людей!')
                break
            else:
                if person == PM5_0:
                    for dev in self.personnel_persons[person]:
                        print(f'{dev}: {self.personnel_persons[person][dev]}')
                else:
                    print(f'{person}: {self.personnel_persons[person]}')

    def show_tasks(self):
        print(f'Проект: {self.name}\n'
              f'----------------')
        for task in self.tasks:
            print(f'Исполнитель: {task}\n'
                  f'Задача: {self.tasks[task][0]}\n'
                  f'Дата назначения: {self.tasks[task][1].strftime("%x")}\n'
                  f'Дедлайн: {self.tasks[task][2].strftime("%x")}\n')

    def show_self(self):
        print(f'---{self.name}---\n'
              f'Описание: {self.descriptions}\n'
              f'Дата запуска: {self.date.strftime("%x")}\n'
              f'Стадия: {self.stage}\n'
              f'Стоимость проекта: {self.price}\n'
              f'Заметки: {self.notes}\n'
              f'Дедлайн: {self.date_end}\n'
              f'Количество людей: {len(self.persons)}')
        print(f'Состав: ', end=': ')
        for person in self.persons:
            cprint(person.name, person.lvl, end=', ')
        print('\n')

    def determine_price_estimate(self, back, front, ml=0, layout_designer=0, fullstack=0, designer=0, pm=0, promotion=0,
                                 system_admin=0, active=False):
        self.estimate['amount_back'] = back * self.personnel_persons[PM5_0][PM5[0]].rate
        self.estimate['amount_front'] = front * self.personnel_persons[PM5_0][PM5[1]].rate
        self.estimate['amount_ml'] = ml * self.personnel_persons[PM5_0][PM5[2]].rate
        self.estimate['amount_layout_designer'] = layout_designer * self.personnel_persons[PM5_0][PM5[3]].rate
        self.estimate['amount_fullstack'] = fullstack * self.personnel_persons[PM5_0][PM5[4]].rate
        self.estimate['amount_designer'] = designer * self.personnel_persons[PM5_0][PM5[5]].rate
        self.estimate['amount_pm'] = pm * self.personnel_persons[PM4].rate
        self.estimate['amount_promotion'] = promotion * self.personnel_persons[PM1].rate
        self.estimate['amount_system_admin'] = system_admin * self.personnel_persons[PM3].rate

        for amount in self.estimate:
            if amount == 'amount_sale':
                self.estimate['amount_admin'] += self.estimate[amount] * 0.3
                continue
            self.estimate['amount_sale'] += self.estimate[amount] * 0.2
            self.estimate['amount_admin'] += self.estimate[amount] * 0.3

        if self.stage == 'Проект закрыт':
            self.personnel_persons[PM5_0][PM5[0]].payment += self.estimate['amount_back']
            self.personnel_persons[PM5_0][PM5[1]].payment += self.estimate['amount_front']
            self.personnel_persons[PM5_0][PM5[2]].payment += self.estimate['amount_ml']
            self.personnel_persons[PM5_0][PM5[3]].payment += self.estimate['amount_layout_designer']
            self.personnel_persons[PM5_0][PM5[4]].payment += self.estimate['amount_fullstack']
            self.personnel_persons[PM5_0][PM5[5]].payment += self.estimate['amount_designer']
            self.personnel_persons[PM4].payment += self.estimate['amount_pm']
            self.personnel_persons[PM1].payment += self.estimate['amount_promotion']
            self.personnel_persons[PM3].payment += self.estimate['amount_system_admin']
            self.personnel_persons[PM2].payment += self.estimate['amount_sale']

    def show_determine_price_estimate(self):
        print(f'{self.personnel_persons[PM5_0][PM5[0]]} - {self.estimate["amount_back"]}р\n'
              f'{self.personnel_persons[PM5_0][PM5[1]]} - {self.estimate["amount_front"]}р\n'
              f'{self.personnel_persons[PM5_0][PM5[2]]} - {self.estimate["amount_ml"]}р\n'
              f'{self.personnel_persons[PM5_0][PM5[3]]} - {self.estimate["amount_layout_designer"]}р\n'
              f'{self.personnel_persons[PM5_0][PM5[4]]} - {self.estimate["amount_fullstack"]}р\n'
              f'{self.personnel_persons[PM3]} - {self.estimate["amount_system_admin"]}р\n'
              f'{self.personnel_persons[PM1]} - {self.estimate["amount_promotion"]}р\n'
              f'{self.personnel_persons[PM5_0][PM5[5]]} - {self.estimate["amount_designer"]}р\n'
              f'{self.personnel_persons[PM4]} - {self.estimate["amount_pm"]}р\n'
              f'{self.personnel_persons[PM2]} - {self.estimate["amount_sale"]}р\n'
              f'Директор - {self.estimate["amount_admin"] // 2}р')

        for all_amount in self.estimate:
            self.estimate['amount_project'] += self.estimate[all_amount]
        print(f'Стоимость заказа - {self.estimate["amount_project"]}р')

    def __str__(self):
        return f'{self.name}: {self.stage}'
