from db import list_project, list_person
from termcolor import colored, cprint
import datetime


def time_format(date):
    date = str(date)
    call =0
    if date[5:6] == '0':
        return f'({date[0:4]}, {date[6: 7]}, {date[8: 10]})'
    if date[8:9] == '0':
        return f'({date[0:4]}, {date_person[5: 7]}, {date[9: 10]})'
    if date[5:6] and date[8:9] == '0':
        return f'({date[0:4]}, {date[6: 7]}, {date[9: 10]})'


start_text = colored('---WEB STUDIO СОКОЛ---', 'red', attrs=['blink'])
print(start_text)
cprint('ОБЩАЯ СТАТИСТИКА:', attrs=['underline'])
for project in list_project:
    color_project = ''
    if project.stage == 'Введутся переговоры':
        color_project = 'red'
    elif project.stage == 'Подписание договора':
        color_project = 'yellow'
    elif project.stage == 'В разработке':
        color_project = 'blue'
    elif project.stage == 'Сдача проекта':
        color_project = 'magenta'
    elif project.stage == 'Проект закрыт':
        color_project = 'green'
    cprint(project, color_project)

while True:
    main_choice = int(input('Выбери пункт:\n'
                            '1. Участники\n'
                            '2. Проекты\n'))
    if int(main_choice) == 1:
        while True:
            person_choice = int(input('Выбери пункт:\n'
                                      '1. Посмотреть конкретного человека\n'
                                      '2. Посмотреть людей в проекте\n'
                                      '3. Посмотреть людей без проекта\n'
                                      '4. Посмотреть выплаты\n'
                                      '---------------\n'
                                      '5. Добавить участника\n'))
            if person_choice == 1:
                for i, person in enumerate(list_person):
                    cprint(f'{i + 1}. {person}', person.lvl)
                one_person_choice = int(input('Выбери человека\n'))
                one_person_choice -= 1
                list_person[one_person_choice].show_self()

            if person_choice == 2:
                for i, person in enumerate(list_person):
                    if person.active_project:
                        print(f'{i}. {person.name} - {person.active_project}')
                    else:
                        continue

            if person_choice == 3:
                for i, person in enumerate(list_person):
                    if person.active_project:
                        continue
                    else:
                        print(f'{i}. {person.name}')

            if person_choice == 4:
                for person in list_person:
                    if person.payment != 0:
                        print(f'{person.name} - {person.payment}р')
                    else:
                        continue

            if person_choice == 5:
                name_person = input('Фамилия участника\n')
                lvl_person = input('Уровень знаний участника:\n'
                                   '1. Начинающий (lvl_1)\n'
                                   '2. Средний (lvl_2)\n'
                                   '3. Высокий (lvl_3)\n')
                date_person = time_format(date=datetime.date.today())
                myself_person = input('Опыт/Стэк технологий участника\n')
                link_person = input('Ссылка на вк/тг участника\n')
                cprint('Скопируй код в раздел "ДОБАВИТЬ ЛЮДЕЙ"', 'yellow')
                cprint(f"'{name_person}': [{lvl_person}, datetime.datetime{date_person}, '{myself_person}', '{link_person}'],  # {len(list_person) - 1}", 'green')


    if main_choice == 2:
        while True:
            for i, project in enumerate(list_project):
                print(f'{i + 1}. {project}')
            project_choice = int(input('Выбери пункт:\n'
                                       '1. Посмотреть конкретный проект\n'
                                       '2. Посмотреть задачи\n'
                                       '3. Посмотреть заметки\n'))

            if project_choice == 1:
                for i, project in enumerate(list_project):
                    print(f'{i+1}. {project.name}')
                one_project_choice = int(input('Выбери проект\n'))
                one_project_choice -= 1
                list_project[one_project_choice].show_self()
                choice = int(input(f'1. Добавить людей\n'
                                   f'2. Добавить задачу\n'
                                   f'3. Добавить заметку\n'
                                   f'4. Просмотреть выплаты\n'))
                if choice == 1:
                    participants = dict(content_filling=0, sale=0, system_administrator=0, pm=0, backend=0, frontend=0,
                                        ML=0, layout_designer=0, fullstack=0, web_designer=0)
                    for i, persons in enumerate(list_person):
                        cprint(f'{i}. {persons}', 'cyan')
                    cprint('Заполни таблицу, если должность отсуствует, то поставь "-1"', 'yellow')
                    for i, participant in enumerate(participants):
                        while True:
                            value = int(input(f'{i + 1}, {participant} '))
                            if value <= len(list_person):
                                participants[participant] = value
                                break
                            else:
                                cprint('Неверное значение, повторите попытку!', 'red')
                                continue

                    cprint('Скопируй код в раздел "ДОБАВИТЬ ЛЮДЕЙ"', 'yellow')
                    cprint(f"list_project[{one_project_choice}].add_persons(list_person=list_person, list_add=[{participants['content_filling']}, {participants['sale']}, {participants['system_administrator']}, {participants['pm']}, "
                           f" {participants['backend']}, {participants['frontend']}, {participants['ML']}, {participants['layout_designer']}, {participants['fullstack']}, {participants['web_designer']}])",
                        'green')

                if choice == 2:
                    for person_project in list_project[one_project_choice].personnel_persons['Разработчик']:
                        if list_project[one_project_choice].personnel_persons['Разработчик'][person_project].name == 'Отсуствует':
                            continue
                        cprint(person_project, list_project[one_project_choice].personnel_persons['Разработчик'][person_project].lvl)
                    person = input('Кому назначить задачу? (---Написать текстом---)\n')
                    task = input('Какую задачу поставить?\n')
                    date_start = time_format(datetime.datetime.today())
                    date = input(f'Дедлайн задачи? || Пример: {str(datetime.datetime.today())[0: 10]} ')
                    date_end = time_format(date)
                    cprint('Скопируй код в раздел "ДОБАВИТЬ ЛЮДЕЙ"', 'yellow')
                    cprint(f"list_project[{one_project_choice}].add_task(person='{person}', task='{task}', date_start=datetime.datetime{date_start}, date_end=datetime.datetime{date_end})",
                        'green')

                if choice == 3:
                    new_note = input('Какая будет заметка? ')
                    cprint('Скопируй код в раздел "ДОБАВИТЬ ЛЮДЕЙ"', 'yellow')
                    cprint(f"list_project[{one_project_choice}].add_notes(note='{new_note}')",'green')

                if choice == 4:
                    list_project[one_project_choice].show_determine_price_estimate()

            if project_choice == 2:
                for project in list_project:
                    project.show_tasks()

            if project_choice == 3:
                for project in list_project:
                    print(f'{project.name} - {project.notes}')


