import telebot
from telebot import types  # для указание типов
bot = telebot.TeleBot('5944257263:AAHtYaf1P_XpqreRrLBOLLSOINfS5qxgXW8')

yearsWorld = [2002, 2006, 2010, 2014, 2018]
yearsEurope = [2000, 2004, 2008, 2012, 2016, 2020]
yearsAmerica = [2001, 2004, 2007, 2011, 2015, 2016, 2019, 2021]
yearsAsia = [2000, 2004, 2007, 2011, 2015, 2019]
yearsAfrica = [2000, 2002, 2004, 2006, 2008,
               2010, 2010, 2013, 2015, 2017, 2019, 2021]
World = ["Бразилия", "Италия", "Испания", "Испания" "Германия", "Франция"]
Europe = ["Франция", "Греция", "Испания", "Португалия", "Италия"]
America = ["Колумбия", "Бразилия", "Бразилия",
           "Уругвай", "Чили", "Чили", "Бразилия", "Аргентина"]
Asia = ["Япония", "Япония", "Ирак", "Япония", "Австралия", "Катар"]
Africa = ["Камерун", "Камерун", "Тунис", "Египет", "Египет", "Египет",
          "Замбия", "Нигерия", "Кот-дИвуар", "Камерун", "Алжир", "Сенегал"]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    keyboard = types.InlineKeyboardMarkup()

    # По очереди готовим текст и обработчик для каждого знака зодиака
    keyWorld = types.InlineKeyboardButton(
        text='Чемпионат мира', callback_data='world')
    keyboard.add(keyWorld)
    keyEurope = types.InlineKeyboardButton(
        text='Чемпионат Европы', callback_data='europe')
    keyboard.add(keyEurope)
    keyAmerica = types.InlineKeyboardButton(
        text='Кубок Америки', callback_data='america')
    keyboard.add(keyAmerica)
    keyAsia = types.InlineKeyboardButton(
        text='Кубок Азии', callback_data='asia')
    keyboard.add(keyAsia)
    keyAfrica = types.InlineKeyboardButton(
        text='Кубок Африки', callback_data='africa')
    keyboard.add(keyAfrica)
    bot.send_message(message.from_user.id,
                     text='Выбери турнир', reply_markup=keyboard)


# Года проведения турниров
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "world":
        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(yearsWorld)):
            keyWorldChampYear = types.InlineKeyboardButton(
                text=yearsWorld[i], callback_data='worldChampYear' + str(i))
            keyboard.add(keyWorldChampYear)
        bot.send_message(call.from_user.id,
                         text='Выбери год проведения турнира', reply_markup=keyboard)

    if call.data == "europe":
        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(yearsEurope)):
            keyEuropeChampYear = types.InlineKeyboardButton(
                text=yearsEurope[i], callback_data='europeChampYear' + str(i))
            keyboard.add(keyEuropeChampYear)
        bot.send_message(call.from_user.id,
                         text='Выбери год проведения турнира', reply_markup=keyboard)

    elif call.data == "america":
        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(yearsAmerica)):
            keyAmericaChampYear = types.InlineKeyboardButton(
                text=yearsAmerica[i], callback_data='americaChampYear' + str(i))
            keyboard.add(keyAmericaChampYear)
        bot.send_message(call.from_user.id,
                         text='Выбери год проведения турнира', reply_markup=keyboard)

    elif call.data == "asia":
        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(yearsAsia)):
            keyAsiaChampYear = types.InlineKeyboardButton(
                text=yearsAsia[i], callback_data='asiaChampYear' + str(i))
            keyboard.add(keyAsiaChampYear)
        bot.send_message(call.from_user.id,
                         text='Выбери год проведения турнира', reply_markup=keyboard)

    elif call.data == "africa":
        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(yearsAfrica)):
            keyAfricaChampYear = types.InlineKeyboardButton(
                text=yearsAfrica[i], callback_data='africaChampYear' + str(i))
            keyboard.add(keyAfricaChampYear)
        bot.send_message(call.from_user.id,
                         text='Выбери год проведения турнира', reply_markup=keyboard)
    else:
        msg = "Победитель турнира "
        if 'worldChampYear' in call.data:
            for i in range(len(yearsWorld)):
                if call.data == 'worldChampYear' + str(i):
                    msg += str(yearsWorld[i]) + " года: " + World[i]
                    break
            bot.send_message(call.message.chat.id, msg)
        elif 'europeChampYear' in call.data:
            for i in range(len(yearsEurope)):
                if call.data == 'europeChampYear' + str(i):
                    msg += str(yearsEurope[i]) + " года: " + Europe[i]
                    break
            bot.send_message(call.message.chat.id, msg)
        elif 'americaChampYear' in call.data:
            for i in range(len(yearsAmerica)):
                if call.data == 'americaChampYear' + str(i):
                    msg += str(yearsAmerica[i]) + " года: " + America[i]
                    break
            bot.send_message(call.message.chat.id, msg)
        elif 'asiaChampYear' in call.data:
            for i in range(len(yearsAsia)):
                if call.data == 'asiaChampYear' + str(i):
                    msg += str(yearsAsia[i]) + " года: " + Asia[i]
                    break
            bot.send_message(call.message.chat.id, msg)
        elif 'africaChampYear' in call.data:
            for i in range(len(yearsAfrica)):
                if call.data == 'africaChampYear' + str(i):
                    msg += str(yearsAfrica[i]) + " года: " + Africa[i]
                    break
            bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
