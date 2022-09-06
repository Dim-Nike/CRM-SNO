from controller import Person, Project
import datetime

lvl_1 = 'red'
lvl_2 = 'yellow'
lvl_3 = 'green'

list_person = []
list_project = []

# todo ДОБАВИТЬ ЛЮДЕЙ
dict_participants = {'Петченко': [lvl_1, datetime.datetime(2022, 6, 24), 'база C#, C++', 'https://vk.com/katriiiiiiiiiiiiiiiiiin'],  # 0
                     'Левшов': [lvl_3, datetime.datetime(2022, 6, 24), 'Линукс администрирование, проектирование сетей', 'https://vk.com/masyrne_games'],  # 1
                     'Стукалов': [lvl_2, datetime.datetime(2022, 6, 24), 'Диплом 1C, Python, sql', 'https://vk.com/stason2001'],  # 2
                     'Морозов': [lvl_1, datetime.datetime(2022, 6, 24), 'С++(8 лет), C#(1 год) тестирование(4 года)', 'https://vk.com/vmoroz_yt'],  # 3
                     'Башкирова': [lvl_1, datetime.datetime(2022, 6, 24), 'Vue js', 'https://vk.com/tvoymim'],  # 4
                     'Гопани': [lvl_2, datetime.datetime(2022, 6, 24), 'Верстка, Node js, изучает React js, , хорошо верстаю', 'https://vk.com/ft_bluecheeze'],  # 5
                     'Литвинов': [lvl_3, datetime.datetime(2022, 6, 24), 'Знаком с Data Science, есть навыки Front and Back', 'https://vk.com/nikerty'],  # 6
                     'Морозюк': [lvl_1, datetime.datetime(2022, 6, 24), 'Администирование Linux-серверов, знает WordPress, изучаю Python, владеет Figma', 'https://vk.com/morozdan2003'],  # 7
                     'Часнык': [lvl_1, datetime.datetime(2022, 6, 24), 'Верстка,  изучаю js, ', 'https://vk.com/zardera'],  # 8
                     'Молчанов': [lvl_1, datetime.datetime(2022, 6, 24), 'Изучаю js, мало опыта', 'https://vk.com/yatwoo7'],  # 9
                     'Еременко': [lvl_3, datetime.datetime(2022, 6, 24), 'Python, нейронки', 'https://vk.com/vladmir0512'],  # 10
                     'Романенко': [lvl_2, datetime.datetime(2022, 6, 24), 'Несложные таски на node js and  js', 'https://vk.com/nazardenr'],  # 11
                     'Христенко': [lvl_2, datetime.datetime(2022, 6, 24), 'Закончил три проекта на js', 'https://vk.com/eliteworldproject'],  # 12
                     'Агеев': [lvl_2, datetime.datetime(2022, 6, 24), 'Изучает Js', 'https://vk.com/n0t_likeotherssss'],  # 13
                     'Сапего': [lvl_3, datetime.datetime(2022, 6, 24), 'Вертсаю по Figma, C++', 'https://vk.com/desap0'],  # 14
                     'Романов': [lvl_3, datetime.datetime(2022, 6, 24), 'Знаю React, Node js', 'https://vk.com/chowomint'],  # 15
                     'Кузьмин': [lvl_3, datetime.datetime(2022, 6, 24), '', 'https://vk.com/sergeikuzmin241'],  # 16
                     'Селима': [lvl_2, datetime.datetime(2022, 6, 24), '', 'https://vk.com/id380301137'],  # 17
                     'Карлов': [lvl_3, datetime.datetime(2022, 6, 24), 'React, вертска, хорошие качества капитана', 'https://vk.com/nikkarlov'],  # 18
                     'Кабанов': [lvl_3, datetime.datetime(2022, 6, 24), 'Знаю Figma, знаком с фотошопом, естьнавыки работы с юнити', 'https://vk.com/ghostwithaplan'],  # 19
                     'Савенко': [lvl_2, datetime.datetime(2022, 6, 24), '', 'https://vk.com/i.savenko0'],  # 20
                     'Рябоволова': [lvl_2, datetime.datetime(2022, 6, 24), 'Опыт работы: онлайн школа(2 нед), теле-2(4 месяца), парфюмерия и косметика(на данный момент)', 'https://vk.com/drshaa'],  # 21
                     'Филонова': [lvl_3, datetime.datetime(2022, 6, 24), 'Node js, Vue js, PostrgreSQL, Управленческие качества', 'https://vk.com/mfilonova2000'],  # 22
                     'Щупакевич': [lvl_1, datetime.datetime(2022, 6, 24), 'Знаю C#, есть опыт напсиание серверной части в рамках курсовой работы', 'https://vk.com/exxxplosionnn'],  # 23
                     'Берест': [lvl_3, datetime.datetime(2022, 6, 24), 'ASP.NET + JQ(1 год коммерческого опыта), навыки xamarin и WDF(в рамках курсовой работы)', 'https://vk.com/id169979785'],  # 24




                     'Отсуствует': [lvl_1, datetime.datetime(2022, 6, 24), '', ''],  # -1
                     }



# todo ДОБАВИТЬ ПРОЕКТ
dict_projects = {'Бетон': ['Создать интернет магазин без платежки',
                           datetime.datetime(2022, 7, 15),
                           0],
                 'Галлерея картин': ['Ошибка публикации записей',
                                     datetime.datetime(2022, 7, 21),
                                     4],
                 'Репетитор': ['Создать лендинг',
                               datetime.datetime(2022, 7, 15),
                               0],
                 'Гостиница': ['Создать лендинг',
                                       datetime.datetime(2022, 7, 28),
                                       1],

                 }

for person in dict_participants:
    list_person.append(
        Person(name=person, lvl=dict_participants[person][0], date=dict_participants[person][1],
               myself=dict_participants[person][2], link=dict_participants[person][3]))

for project in dict_projects:
    list_project.append(Project(name=project, descriptions=dict_projects[project][0], date=dict_projects[project][1],
                                stage=dict_projects[project][2]))



# todo ДОБАВИТЬ ЛЮДЕЙ В ПРОЕКТ
list_project[0].add_persons(list_person=list_person,
                            list_add=[20, 16, 1, 10, -1, -1, -1, 5, 15, 18])
list_project[1].add_persons(list_person=list_person, list_add=[-1, 21, -1, -1, 15, -1, -1, -1, -1, -1])
list_project[3].add_persons(list_person=list_person, list_add=[-1, -1, -1, 13,  -1, -1, -1, -1, -1, 7])






# todo СМЕТА ПРОЕКТА
list_project[0].determine_price_estimate(back=0, front=0, layout_designer=40, fullstack=260, designer=15, pm=30, system_admin=5)
list_project[1].determine_price_estimate(back=3, front=0)


# todo ДОБАВИТЬ ЗАДАЧУ
list_project[1].add_task(person='Backend', task='Изучить код на сервере', date_start=datetime.datetime(2022, 7, 23), date_end=datetime.datetime(2022, 7, 28))
list_project[3].add_task(person='Web дизайнер', task='Сделать первую версию дизайна', date_start=datetime.datetime(2022, 8, 9), date_end=datetime.datetime(2022, 8, 10))



# todo ДОБАВИТЬ ЗАМЕТКУ
list_project[0].add_notes(note='Созвон по дс с заказчиком во вторник')
list_project[1].add_notes(note='Клиент был доволен, ждем его предложение о поддержки сайта')
list_project[3].add_notes(note='Ожидается первая версия дизайна')