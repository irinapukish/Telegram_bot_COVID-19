import telebot
from telebot import types
from covid19tracker import Tracker

bot = telebot.TeleBot('TELEGRAM TOKEN')
track = Tracker() 
@bot.message_handler(commands=['start'])
def start(message):
    send_message = f'<b>Hej {message.from_user.first_name}! 👋</b>\nProszę wybrać język:\n'
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton('🇵🇱', callback_data='pl')
    btn2 = types.InlineKeyboardButton('🇺🇦',callback_data='ua')
    btn3 = types.InlineKeyboardButton('🇬🇧',callback_data='us')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'pl':
        markup_reply1 = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width= 2)
        btn_coronapl = types.KeyboardButton ('Koronawirus')
        btn_savepl = types.KeyboardButton ('Chroń siebie')
        markup_reply1.add(btn_coronapl, btn_savepl)
        bot.send_message(call.message.chat.id, "Aby dowiedzieć się danych o koronawirusie 🦠,\nnapisz nazwę kraju 🌉",
        reply_markup= markup_reply1)
        
    elif call.data == 'ua':
        markup_reply2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
        btn_coronaua = types.KeyboardButton ('Коронавірус')
        btn_saveua = types.KeyboardButton ('Захисти себе')
        markup_reply2.add(btn_coronaua, btn_saveua)
        bot.send_message(call.message.chat.id, "Щоб дізнатися дані про коронавірус 🦠,\nнапишіть назву країни 🌉",
        reply_markup= markup_reply2)
    elif call.data == 'us':
        markup_reply3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
        btn_coronaus = types.KeyboardButton ('Coronavirus')
        btn_saveus = types.KeyboardButton ('Protect yourself')
        markup_reply3.add(btn_coronaus, btn_saveus)
        bot.send_message(call.message.chat.id, "To find out about the coronavirus data 🦠,\nwrite the name of the country 🌉",
        reply_markup= markup_reply3)

@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    
    get_message_bot = message.text.strip().lower()
    

    #usa
    if get_message_bot == "stany zjednoczone":
        track_usa =  track.country_info_by_name('usa')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_usa['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_usa['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_usa['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_usa['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_usa['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_usa['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_usa['new recoveries']:,}"
    elif get_message_bot == "usa":
        track_usa =  track.country_info_by_name('usa')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_usa['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_usa['total cases']:,}\n ☠️ Deaths: "\
                f"{track_usa['total deaths']:,}\n 💪 People who have recovered: {track_usa['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_usa['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_usa['new deaths']:,}\n 💪 People who have recovered: {track_usa['new recoveries']:,}"
    elif get_message_bot == "сша":
        track_usa =  track.country_info_by_name('usa')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_usa['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_usa['total cases']:,}\n ☠️ Смертей: "\
                f"{track_usa['total deaths']:,}\n 💪 Люди, які одужали: {track_usa['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_usa['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_usa['new deaths']:,}\n 💪 Люди, які одужали: {track_usa['new recoveries']:,}"
    #ukraina
    elif get_message_bot == "ukraina":
        track_ukraine =  track.country_info_by_name('ukraine')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_ukraine['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_ukraine['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_ukraine['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_ukraine['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_ukraine['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_ukraine['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_ukraine['new recoveries']:,}"
    elif get_message_bot == "ukraine":
        track_ukraine =  track.country_info_by_name('ukraine')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_ukraine['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_ukraine['total cases']:,}\n ☠️ Deaths: "\
                f"{track_ukraine['total deaths']:,}\n 💪 People who have recovered: {track_ukraine['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_ukraine['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_ukraine['new deaths']:,}\n 💪 People who have recovered: {track_ukraine['new recoveries']:,}"
    elif get_message_bot == "україна":
        track_ukraine =  track.country_info_by_name('ukraine')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_ukraine['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_ukraine['total cases']:,}\n ☠️ Смертей: "\
                f"{track_ukraine['total deaths']:,}\n 💪 Люди, які одужали: {track_ukraine['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_ukraine['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_ukraine['new deaths']:,}\n 💪 Люди, які одужали: {track_ukraine['new recoveries']:,}"
    #polska
    elif get_message_bot == "polska":
        track_poland =  track.country_info_by_name('poland')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_poland['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_poland['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_poland['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_poland['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_poland['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_poland['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_poland['new recoveries']:,}"
    elif get_message_bot == "poland":
        track_poland =  track.country_info_by_name('poland')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_poland['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_poland['total cases']:,}\n ☠️ Deaths: "\
                f"{track_poland['total deaths']:,}\n 💪 People who have recovered: {track_poland['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_poland['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_poland['new deaths']:,}\n 💪 People who have recovered: {track_poland['new recoveries']:,}"
    elif get_message_bot == "польща":
        track_poland =  track.country_info_by_name('poland')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_poland['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_poland['total cases']:,}\n ☠️ Смертей: "\
                f"{track_poland['total deaths']:,}\n 💪 Люди, які одужали: {track_poland['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_poland['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_poland['new deaths']:,}\n 💪 Люди, які одужали: {track_poland['new recoveries']:,}"
    #włochy
    elif get_message_bot == "włochy":
        track_italy =  track.country_info_by_name('italy')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_italy['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_italy['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_italy['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_italy['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_italy['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_italy['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_italy['new recoveries']:,}"
    elif get_message_bot == "italy":
        track_italy =  track.country_info_by_name('italy')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_italy['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_italy['total cases']:,}\n ☠️ Deaths: "\
                f"{track_italy['total deaths']:,}\n 💪 People who have recovered: {track_italy['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_italy['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_italy['new deaths']:,}\n 💪 People who have recovered: {track_italy['new recoveries']:,}"
    elif get_message_bot == "італія":
        track_italy =  track.country_info_by_name('italy')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_italy['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_italy['total cases']:,}\n ☠️ Смертей: "\
                f"{track_italy['total deaths']:,}\n 💪 Люди, які одужали: {track_italy['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_italy['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_italy['new deaths']:,}\n 💪 Люди, які одужали: {track_italy['new recoveries']:,}"
    #Kazachstan
    elif get_message_bot == "kazakhstan":
        track_kazach =  track.country_info_by_name('kazakhstan')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_kazach['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_kazach['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_kazach['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_kazach['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_kazach['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_kazach['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_kazach['new recoveries']:,}"
    elif get_message_bot == "kazachstan":
        track_kazach =  track.country_info_by_name('kazakhstan')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_kazach['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_kazach['total cases']:,}\n ☠️ Deaths: "\
                f"{track_kazach['total deaths']:,}\n 💪 People who have recovered: {track_kazach['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_kazach['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_kazach['new deaths']:,}\n 💪 People who have recovered: {track_kazach['new recoveries']:,}"
    elif get_message_bot == "казахстан":
        track_kazach =  track.country_info_by_name('kazakhstan')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_kazach['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_kazach['total cases']:,}\n ☠️ Смертей: "\
                f"{track_kazach['total deaths']:,}\n 💪 Люди, які одужали: {track_kazach['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_kazach['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_kazach['new deaths']:,}\n 💪 Люди, які одужали: {track_kazach['new recoveries']:,}"
    #Niemcy
    elif get_message_bot == "niemcy":
        track_niemcy =  track.country_info_by_name('germany')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_niemcy['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_niemcy['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_niemcy['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_niemcy['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_niemcy['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_niemcy['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_niemcy['new recoveries']:,}"
    elif get_message_bot == "germany":
        track_niemcy =  track.country_info_by_name('germany')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_niemcy['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_niemcy['total cases']:,}\n ☠️ Deaths: "\
                f"{track_niemcy['total deaths']:,}\n 💪 People who have recovered: {track_niemcy['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_niemcy['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_niemcy['new deaths']:,}\n 💪 People who have recovered: {track_niemcy['new recoveries']:,}"
    elif get_message_bot == "німеччина":
        track_niemcy =  track.country_info_by_name('germany')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_niemcy['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_niemcy['total cases']:,}\n ☠️ Смертей: "\
                f"{track_niemcy['total deaths']:,}\n 💪 Люди, які одужали: {track_niemcy['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_niemcy['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_niemcy['new deaths']:,}\n 💪 Люди, які одужали: {track_niemcy['new recoveries']:,}"
    #Czechy
    elif get_message_bot == "czechy":
        track_сzechy =  track.country_info_by_name('czechia')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_сzechy['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_сzechy['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_сzechy['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_сzechy['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_сzechy['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_сzechy['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_сzechy['new recoveries']:,}"
    elif get_message_bot == "czechia":
        track_сzechy =  track.country_info_by_name('czechia')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_сzechy['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_сzechy['total cases']:,}\n ☠️ Deaths: "\
                f"{track_сzechy['total deaths']:,}\n 💪 People who have recovered: {track_сzechy['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_сzechy['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_сzechy['new deaths']:,}\n 💪 People who have recovered: {track_сzechy['new recoveries']:,}"
    elif get_message_bot == "чехія":
        track_сzechy =  track.country_info_by_name('czechia')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_сzechy['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_сzechy['total cases']:,}\n ☠️ Смертей: "\
                f"{track_сzechy['total deaths']:,}\n 💪 Люди, які одужали: {track_сzechy['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_сzechy['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_сzechy['new deaths']:,}\n 💪 Люди, які одужали: {track_сzechy['new recoveries']:,}"
    #Węgry
    elif get_message_bot == "węgry":
        track_wegry =  track.country_info_by_name('hungary')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_wegry['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_wegry['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_wegry['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_wegry['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_wegry['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_wegry['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_wegry['new recoveries']:,}"
    elif get_message_bot == "hungary":
        track_wegry =  track.country_info_by_name('hungary')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_wegry['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_wegry['total cases']:,}\n ☠️ Deaths: "\
                f"{track_wegry['total deaths']:,}\n 💪 People who have recovered: {track_wegry['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_wegry['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_wegry['new deaths']:,}\n 💪 People who have recovered: {track_wegry['new recoveries']:,}"
    elif get_message_bot == "угорщина":
        track_wegry =  track.country_info_by_name('hungary')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_wegry['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_wegry['total cases']:,}\n ☠️ Смертей: "\
                f"{track_wegry['total deaths']:,}\n 💪 Люди, які одужали: {track_wegry['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_wegry['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_wegry['new deaths']:,}\n 💪 Люди, які одужали: {track_wegry['new recoveries']:,}"
    #Białoruś
    elif get_message_bot == "białoruś":
        track_bialorus =  track.country_info_by_name('belarus')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_bialorus['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_bialorus['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_bialorus['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_bialorus['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_bialorus['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_bialorus['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_bialorus['new recoveries']:,}"
    elif get_message_bot == "belarus":
        track_bialorus =  track.country_info_by_name('belarus')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_bialorus['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_bialorus['total cases']:,}\n ☠️ Deaths: "\
                f"{track_bialorus['total deaths']:,}\n 💪 People who have recovered: {track_bialorus['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_bialorus['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_bialorus['new deaths']:,}\n 💪 People who have recovered: {track_bialorus['new recoveries']:,}"
    elif get_message_bot == "білорусь":
        track_bialorus =  track.country_info_by_name('belarus')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_bialorus['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_bialorus['total cases']:,}\n ☠️ Смертей: "\
                f"{track_bialorus['total deaths']:,}\n 💪 Люди, які одужали: {track_bialorus['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_bialorus['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_bialorus['new deaths']:,}\n 💪 Люди, які одужали: {track_bialorus['new recoveries']:,}"
    #Rosja
    elif get_message_bot == "rosja":
        track_rosja =  track.country_info_by_name('russia')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_rosja['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_rosja['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_rosja['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_rosja['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_rosja['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_rosja['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_rosja['new recoveries']:,}"
    elif get_message_bot == "russia":
        track_rosja =  track.country_info_by_name('russia')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_rosja['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_rosja['total cases']:,}\n ☠️ Deaths: "\
                f"{track_rosja['total deaths']:,}\n 💪 People who have recovered: {track_rosja['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_rosja['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_rosja['new deaths']:,}\n 💪 People who have recovered: {track_rosja['new recoveries']:,}"
    elif get_message_bot == "росія":
        track_rosja =  track.country_info_by_name('russia')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_rosja['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_rosja['total cases']:,}\n ☠️ Смертей: "\
                f"{track_rosja['total deaths']:,}\n 💪 Люди, які одужали: {track_rosja['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_rosja['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_rosja['new deaths']:,}\n 💪 Люди, які одужали: {track_rosja['new recoveries']:,}"
    #Dania
    elif get_message_bot == "dania":
        track_dania =  track.country_info_by_name('denmark')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_dania['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_dania['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_dania['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_dania['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_dania['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_dania['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_dania['new recoveries']:,}"
    elif get_message_bot == "denmark":
        track_dania =  track.country_info_by_name('denmark')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_dania['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_dania['total cases']:,}\n ☠️ Deaths: "\
                f"{track_dania['total deaths']:,}\n 💪 People who have recovered: {track_dania['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_dania['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_dania['new deaths']:,}\n 💪 People who have recovered: {track_dania['new recoveries']:,}"
    elif get_message_bot == "данія":
        track_dania =  track.country_info_by_name('denmark')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_dania['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_dania['total cases']:,}\n ☠️ Смертей: "\
                f"{track_dania['total deaths']:,}\n 💪 Люди, які одужали: {track_dania['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_dania['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_dania['new deaths']:,}\n 💪 Люди, які одужали: {track_dania['new recoveries']:,}"
    #Francja
    elif get_message_bot == "francja":
        track_francja =  track.country_info_by_name('france')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_francja['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_francja['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_francja['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_francja['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_francja['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_francja['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_francja['new recoveries']:,}"
    elif get_message_bot == "france":
        track_francja =  track.country_info_by_name('france')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_francja['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_francja['total cases']:,}\n ☠️ Deaths: "\
                f"{track_francja['total deaths']:,}\n 💪 People who have recovered: {track_francja['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_francja['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_francja['new deaths']:,}\n 💪 People who have recovered: {track_francja['new recoveries']:,}"
    elif get_message_bot == "франція":
        track_francja =  track.country_info_by_name('france')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_francja['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_francja['total cases']:,}\n ☠️ Смертей: "\
                f"{track_francja['total deaths']:,}\n 💪 Люди, які одужали: {track_francja['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_francja['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_francja['new deaths']:,}\n 💪 Люди, які одужали: {track_francja['new recoveries']:,}"
    #Hiszpania
    elif get_message_bot == "hiszpania":
        track_hiszpania =  track.country_info_by_name('spain')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_hiszpania['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_hiszpania['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_hiszpania['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_hiszpania['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_hiszpania['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_hiszpania['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_hiszpania['new recoveries']:,}"
    elif get_message_bot == "spain":
        track_hiszpania =  track.country_info_by_name('spain')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_hiszpania['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_hiszpania['total cases']:,}\n ☠️ Deaths: "\
                f"{track_hiszpania['total deaths']:,}\n 💪 People who have recovered: {track_hiszpania['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_hiszpania['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_hiszpania['new deaths']:,}\n 💪 People who have recovered: {track_hiszpania['new recoveries']:,}"
    elif get_message_bot == "іспанія":
        track_hiszpania =  track.country_info_by_name('spain')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_hiszpania['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_hiszpania['total cases']:,}\n ☠️ Смертей: "\
                f"{track_hiszpania['total deaths']:,}\n 💪 Люди, які одужали: {track_hiszpania['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_hiszpania['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_hiszpania['new deaths']:,}\n 💪 Люди, які одужали: {track_hiszpania['new recoveries']:,}"
    #Słowacja
    elif get_message_bot == "słowacja":
        track_slowacja =  track.country_info_by_name('slovakia')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_slowacja['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_slowacja['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_slowacja['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_slowacja['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_slowacja['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_slowacja['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_slowacja['new recoveries']:,}"
    elif get_message_bot == "slovakia":
        track_slowacja =  track.country_info_by_name('slovakia')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_slowacja['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_slowacja['total cases']:,}\n ☠️ Deaths: "\
                f"{track_slowacja['total deaths']:,}\n 💪 People who have recovered: {track_slowacja['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_slowacja['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_slowacja['new deaths']:,}\n 💪 People who have recovered: {track_slowacja['new recoveries']:,}"
    elif get_message_bot == "словаччина":
        track_slowacja =  track.country_info_by_name('slovakia')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_slowacja['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_slowacja['total cases']:,}\n ☠️ Смертей: "\
                f"{track_slowacja['total deaths']:,}\n 💪 Люди, які одужали: {track_slowacja['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_slowacja['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_slowacja['new deaths']:,}\n 💪 Люди, які одужали: {track_slowacja['new recoveries']:,}"
    #Chorwacja
    elif get_message_bot == "сhorwacja":
        track_сhorwacja =  track.country_info_by_name('croatia')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_сhorwacja['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_сhorwacja['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_сhorwacja['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_сhorwacja['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_сhorwacja['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_сhorwacja['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_сhorwacja['new recoveries']:,}"
    elif get_message_bot == "croatia":
        track_сhorwacja =  track.country_info_by_name('croatia')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_сhorwacja['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_сhorwacja['total cases']:,}\n ☠️ Deaths: "\
                f"{track_сhorwacja['total deaths']:,}\n 💪 People who have recovered: {track_сhorwacja['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_сhorwacja['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_сhorwacja['new deaths']:,}\n 💪 People who have recovered: {track_сhorwacja['new recoveries']:,}"
    elif get_message_bot == "хорватія":
        track_сhorwacja =  track.country_info_by_name('croatia')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_сhorwacja['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_сhorwacja['total cases']:,}\n ☠️ Смертей: "\
                f"{track_сhorwacja['total deaths']:,}\n 💪 Люди, які одужали: {track_сhorwacja['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_сhorwacja['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_сhorwacja['new deaths']:,}\n 💪 Люди, які одужали: {track_сhorwacja['new recoveries']:,}"
    #Słowenia
    elif get_message_bot == "słowenia":
        track_slowenia =  track.country_info_by_name('slovenia')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_slowenia['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_slowenia['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_slowenia['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_slowenia['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_slowenia['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_slowenia['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_slowenia['new recoveries']:,}"
    elif get_message_bot == "slovenia":
        track_slowenia =  track.country_info_by_name('slovenia')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_slowenia['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_slowenia['total cases']:,}\n ☠️ Deaths: "\
                f"{track_slowenia['total deaths']:,}\n 💪 People who have recovered: {track_slowenia['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_slowenia['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_slowenia['new deaths']:,}\n 💪 People who have recovered: {track_slowenia['new recoveries']:,}"
    elif get_message_bot == "словенія":
        track_slowenia =  track.country_info_by_name('slovenia')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_slowenia['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_slowenia['total cases']:,}\n ☠️ Смертей: "\
                f"{track_slowenia['total deaths']:,}\n 💪 Люди, які одужали: {track_slowenia['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_slowenia['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_slowenia['new deaths']:,}\n 💪 Люди, які одужали: {track_slowenia['new recoveries']:,}"
    #Grecja
    elif get_message_bot == "grecja":
        track_grecja =  track.country_info_by_name('greece')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_grecja['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_grecja['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_grecja['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_grecja['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_grecja['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_grecja['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_grecja['new recoveries']:,}"
    elif get_message_bot == "greece":
        track_grecja =  track.country_info_by_name('greece')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_grecja['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_grecja['total cases']:,}\n ☠️ Deaths: "\
                f"{track_grecja['total deaths']:,}\n 💪 People who have recovered: {track_grecja['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_grecja['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_grecja['new deaths']:,}\n 💪 People who have recovered: {track_grecja['new recoveries']:,}"
    elif get_message_bot == "греція":
        track_grecja =  track.country_info_by_name('greece')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_grecja['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_grecja['total cases']:,}\n ☠️ Смертей: "\
                f"{track_grecja['total deaths']:,}\n 💪 Люди, які одужали: {track_grecja['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_grecja['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_grecja['new deaths']:,}\n 💪 Люди, які одужали: {track_grecja['new recoveries']:,}"
    #Rumunia
    elif get_message_bot == "rumunia":
        track_rumunia =  track.country_info_by_name('romania')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_rumunia['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_rumunia['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_rumunia['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_rumunia['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_rumunia['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_rumunia['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_rumunia['new recoveries']:,}"
    elif get_message_bot == "romania":
        track_rumunia =  track.country_info_by_name('romania')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_rumunia['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_rumunia['total cases']:,}\n ☠️ Deaths: "\
                f"{track_rumunia['total deaths']:,}\n 💪 People who have recovered: {track_rumunia['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_rumunia['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_rumunia['new deaths']:,}\n 💪 People who have recovered: {track_rumunia['new recoveries']:,}"
    elif get_message_bot == "румунія":
        track_rumunia =  track.country_info_by_name('romania')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_rumunia['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_rumunia['total cases']:,}\n ☠️ Смертей: "\
                f"{track_rumunia['total deaths']:,}\n 💪 Люди, які одужали: {track_rumunia['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_rumunia['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_rumunia['new deaths']:,}\n 💪 Люди, які одужали: {track_rumunia['new recoveries']:,}"
    #Turcja
    elif get_message_bot == "turcja":
        track_turcja =  track.country_info_by_name('turkey')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_turcja['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_turcja['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_turcja['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_turcja['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_turcja['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_turcja['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_turcja['new recoveries']:,}"
    elif get_message_bot == "turkey":
        track_turcja =  track.country_info_by_name('turkey')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_turcja['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_turcja['total cases']:,}\n ☠️ Deaths: "\
                f"{track_turcja['total deaths']:,}\n 💪 People who have recovered: {track_turcja['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_turcja['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_turcja['new deaths']:,}\n 💪 People who have recovered: {track_turcja['new recoveries']:,}"
    elif get_message_bot == "туреччина":
        track_turcja =  track.country_info_by_name('turkey')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_turcja['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_turcja['total cases']:,}\n ☠️ Смертей: "\
                f"{track_turcja['total deaths']:,}\n 💪 Люди, які одужали: {track_turcja['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_turcja['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_turcja['new deaths']:,}\n 💪 Люди, які одужали: {track_turcja['new recoveries']:,}"
    #Bułgaria
    elif get_message_bot == "bułgaria":
        track_bulgaria =  track.country_info_by_name('bulgaria')
        final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{track_bulgaria['population']:,}\n"\
            f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {track_bulgaria['total cases']:,}\n ☠️ Zgonów: "\
                f"{track_bulgaria['total deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_bulgaria['total recoveries']:,}\n"\
                    f"<b>Dzisiaj:</b>\n 🤧 Zakażonych: {track_bulgaria['new cases']:,}\n ☠️ Zgonów: "\
                        f"{track_bulgaria['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {track_bulgaria['new recoveries']:,}"
    elif get_message_bot == "bulgaria":
        track_bulgaria =  track.country_info_by_name('bulgaria')
        final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{track_bulgaria['population']:,}\n"\
            f"<b>For all time:</b>\n 🤧 Infected: {track_bulgaria['total cases']:,}\n ☠️ Deaths: "\
                f"{track_bulgaria['total deaths']:,}\n 💪 People who have recovered: {track_bulgaria['total recoveries']:,}\n"\
                    f"<b>Today: </b>\n 🤧 Infected: {track_bulgaria['new cases']:,}\n ☠️ Deaths: "\
                        f"{track_bulgaria['new deaths']:,}\n 💪 People who have recovered: {track_bulgaria['new recoveries']:,}"
    elif get_message_bot == "болгарія":
        track_bulgaria =  track.country_info_by_name('bulgaria')
        final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{track_bulgaria['population']:,}\n"\
            f"<b>За весь час:\n</b> 🤧Заражених: {track_bulgaria['total cases']:,}\n ☠️ Смертей: "\
                f"{track_bulgaria['total deaths']:,}\n 💪 Люди, які одужали: {track_bulgaria['total recoveries']:,}\n"\
                    f"<b>За сьогодні:\n</b> 🤧 Заражених: {track_bulgaria['new cases']:,}\n ☠️ Смертей: "\
                        f"{track_bulgaria['new deaths']:,}\n 💪 Люди, які одужали: {track_bulgaria['new recoveries']:,}"
    #dane z całego świata
    elif  get_message_bot == "świat":
        cases = track.total_cases()
        deaths = track.total_deaths()
        rec = track.total_recoveries()

        final_message = f"<i>Dane z całego świata 🌍:</i>\n<b> 🤧 Zakażonych: </b>{cases:,}\n<b> ☠️ Zgonów: </b>{deaths:,}\n<b> 💪 Osoby, któte wyzdrowiały: </b>{rec:,}"

    elif  get_message_bot == "world":
        cases = track.total_cases()
        deaths = track.total_deaths()
        rec = track.total_recoveries()

        final_message = f"<i>Data from all over the world 🌍:</i>\n<b> 🤧 Infected: </b>{cases:,}\n<b> ☠️ Deaths: </b>{deaths:,}\n<b> 💪 People who have recovered: </b>{rec:,}"
    elif  get_message_bot == "світ":
        cases = track.total_cases()
        deaths = track.total_deaths()
        rec = track.total_recoveries()

        final_message = f"<i>Дані з усього світу 🌍:</i>\n<b> 🤧 Заражених: </b>{cases:,}\n<b> ☠️ Смертей: </b>{deaths:,}\n<b> 💪 Люди, які одужали: </b>{rec:,}"
    #Info o koronawirusie
    elif get_message_bot == 'koronawirus':
        final_message = f"COVID-19  🦠  wpływa na różnych ludzi na różne sposoby. U większości zarażonych choroba rozwija się od łagodnej do umiarkowanej i wyzdrowieje bez hospitalizacji.\n"\
            f"<b>🔴 Najczęstsze objawy: </b>\n"\
                f"▪️ gorączka\n"\
                    f"▪️ suchy kaszel\n"\
                        f"▪️ zmęczenie\n"\
                            f"<b>🔴 Mniej powszechne objawy: </b>\n"\
                                f"▪️ bóle\n"\
                                    f"▪️ ból gardła\n"\
                                        f"▪️ biegunka\n"\
                                            f"▪️ zapalenie spojówek\n"\
                                                f"▪️ bół głowy\n"\
                                                    f"▪️ utrata smaku lub zapachu\n"\
                                                        f"▪️ wysypka na skórze lub przebarwienie palców rąk i nóg\n"
    elif get_message_bot == "коронавірус":
        final_message = f"COVID-19  🦠  по-різному впливає на різних людей. У більшості інфікованих людей розвиватиметься хвороба легкого та середнього ступеня тяжкості та одужуватиме без госпіталізації.\n"\
        f"<b>🔴 Найпоширеніші симптоми: </b>\n"\
            f"▪️ лихоманка\n"\
                f"▪️ сухий кашель\n"\
                    f"▪️ втома\n"\
                        f"<b>🔴 Менш поширені симптоми: </b>\n"\
                            f"▪️ ломота\n"\
                                f"▪️ біль у горлі\n"\
                                    f"▪️ діарея\n"\
                                        f"▪️ кон’юнктивіт\n"\
                                            f"▪️ головний біль\n"\
                                                f"▪️ втрата смаку або запаху\n"\
                                                    f"▪️ висип на шкірі або зміна кольору пальців рук або ніг\n"

    elif get_message_bot == "coronavirus":
        final_message = f"COVID-19  🦠  affects different people in different ways. Most infected people will develop mild to moderate illness and recover without hospitalization.\n"\
        f"<b>🔴 Most common symptoms: </b>\n"\
            f"▪️ fever\n"\
                f"▪️ dry cough\n"\
                    f"▪️ tiredness\n"\
                        f"<b>🔴 Less common symptoms: </b>\n"\
                            f"▪️ aches and pains\n"\
                                f"▪️ sore throat\n"\
                                    f"▪️ diarrhoea\n"\
                                        f"▪️ кconjunctivitis\n"\
                                            f"▪️ headache\n"\
                                                f"▪️ loss of taste or smell\n"\
                                                    f"▪️ a rash on skin, or discolouration of fingers or toes\n"
    #Protect yourself
    elif get_message_bot == "chroń siebie":
        final_message = f"📢 <i>Chroń siebie i innych wokół siebie, znając fakty i podejmując odpowiednie środki ostrożności. Postępuj zgodnie z zaleceniami lokalnych władz zdrowotnych.</i>\n"\
            f"<b>🆘 Aby zapobiec rozprzestrzenianiu się COVID-19:</b>\n"\
                f"▪️ Często myj ręce. Użyj mydła i wody lub środka do dezynfekcji rąk na bazie alkoholu.\n"\
                    f"▪️ Zachowaj bezpieczną odległość od każdego, kto kaszle lub kicha.\n"\
                        f"▪️ Noś maskę, gdy dystans fizyczny nie jest możliwy.\n"\
                            f"▪️ Nie dotykaj oczu, nosa ani ust.\n"\
                                f"▪️ Zakrywaj nos i usta zgiętym łokciem lub chusteczką, gdy kaszlesz lub kichasz.\n"\
                                    f"▪️ Zostań w domu, jeśli źle się poczujesz.\n"\
                                        f"▪️ Jeśli masz gorączkę, kaszel i trudności w oddychaniu, zgłoś się do lekarza.\n"\
                                            f"<i>Zadzwoń z wyprzedzeniem, aby Twój lekarz szybko skierował Cię do właściwej placówki medycznej. Zapewnia to ochronę i zapobiega rozprzestrzenianiu się wirusów i innych infekcji.</i>"
    elif get_message_bot == "захисти себе":
        final_message = f"📢 <i>Захищайте себе та оточуючих, знаючи факти та вживаючи відповідних запобіжних заходів. Дотримуйтесь порад, наданих місцевим органом охорони здоров’я.</i>\n"\
            f"<b>🆘 Щоб запобігти поширенню COVID-19: </b>\n"\
                f"▪️ Часто мийте руки. Використовуйте мило та воду або дезінфікуючий засіб для рук на спиртовій основі.\n"\
                    f"▪️ Дотримуйтесь безпечної відстані від тих, хто кашляє чи чхає.\n"\
                        f"▪️ Носіть маску, коли фізичне дистанціювання неможливе.\n"\
                            f"▪️ Не торкайтесь очей, носа або рота.\n"\
                                f"▪️ Під час кашлю чи чхання закривайте ніс і рот зігнутим ліктем або серветкою.\n"\
                                    f"▪️ Залишайтеся вдома, якщо вам погано.\n"\
                                        f"▪️ Якщо у вас температура, кашель і утруднення дихання, зверніться за медичною допомогою.\n"\
                                            f"<i>Заздалегідь зателефонувавши, ваш лікар може швидко направити вас до потрібного медичного закладу. Це захищає вас і запобігає поширенню вірусів та інших інфекцій.</i>"
    elif get_message_bot == "protect yourself":
        final_message = f"📢 <i>Protect yourself and others around you by knowing the facts and taking appropriate precautions. Follow advice provided by your local health authority.</i>\n"\
            f"<b>🆘 To prevent the spread of COVID-19: </b>\n"\
                f"▪️ Clean your hands often. Use soap and water, or an alcohol-based hand sanitazer.\n"\
                    f"▪️ Maintain a safe distance from anyone who is coughing or sneezing.\n"\
                        f"▪️ Wear a mask when physical distancing is not possible.\n"\
                            f"▪️ Don’t touch your eyes, nose or mouth.\n"\
                                f"▪️ Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n"\
                                    f"▪️ Stay home if you feel unwell.\n"\
                                        f"▪️ If you have a fever, cough and difficulty breathing, seek medical attention.\n"\
                                            f"<i>Calling in advance allows your healthcare provider to quickly direct you to the right health facility. This protects you, and prevents the spread of viruses and other infections.</i>"

    else:
        final_message = f"Proszę napisać nazwę kraju\n Jeśli chcesz dowiedzieć się dane z całego świata , napisz 'świat'"
    bot.send_message(message.chat.id, final_message, parse_mode='HTML')

bot.polling(none_stop=True, interval = 0)


