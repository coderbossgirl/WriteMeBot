import telebot
import random

token = "5265410989:AAFo997eKZP-jcgWifghqJE7XIH5KtL-0VM"

bot = telebot.TeleBot(token)

RANDOM_TASKS = ['Провести время в медитации', 'Заняться своим хобби', 'Написать бота', 'Убрать свое рабочее место', 'Выучить Python', 'Записаться на курс', 'Посмотреть фильм', 'Заняться английским']

HELP = '''
Список доступных команд:
/show  - показать все задачи на заданную дату
/todo - добавить задачу
/random - добавить на сегодня случайную задачу
/help - вывести список доступных команд
'''

tasks = {}

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = f"Задача {task} добавлена на дату {date}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[]" + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
