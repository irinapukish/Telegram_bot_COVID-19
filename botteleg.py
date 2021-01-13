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
        bot.send_message(call.message.chat.id, "Aby dowiedzieć się danych o koronawirusie 🦠,\nnapisz nawzę kraju 🌉",
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
        final_message = f"<u>Dane krajowe:</u>\n<b> 👫 Populacja: </b>{track_usa['population']:,}\n"\
            f"<b> 🤧 Zakażonych: </b>{track_usa['new cases']:,}\n<b> ☠️ Zgonów: </b>"\
                f"{track_usa['new deaths']:,}\n<b> 💪 Osoby, króte wyzdrowiały: </b>{track_usa['new recoveries']:,}"
    elif get_message_bot == "usa":
        track_usa =  track.country_info_by_name('usa')
        final_message = f"<u>National data:</u>\n<b> 👫 Population: </b>{track_usa['population']:,}\n"\
            f"<b> 🤧 Infected: </b>{track_usa['new cases']:,}\n<b> ☠️ Deaths: </b>"\
                f"{track_usa['new deaths']:,}\n<b> 💪 People who have recovered: </b>{track_usa['new recoveries']:,}"
    elif get_message_bot == "сша":
        track_usa =  track.country_info_by_name('usa')
        final_message = f"<u>Національні дані:</u>\n<b> 👫 Населення: </b>{track_usa['population']:,}\n"\
            f"<b> 🤧 Заражених: </b>{track_usa['new cases']:,}\n<b> ☠️ Смертей: </b>"\
                f"{track_usa['new deaths']:,}\n<b> 💪 Люди, які одужали: </b>{track_usa['new recoveries']:,}"
    #ukraina
    elif get_message_bot == "ukraina":
        track_ukraine =  track.country_info_by_name('ukraine')
        final_message = f"<u>Dane krajowe:</u>\n<b> 👫 Populacja: </b>{track_ukraine['population']:,}\n"\
            f"<b> 🤧 Zakażonych: </b>{track_ukraine['new cases']:,}\n<b> ☠️ Zgonów: </b>"\
                f"{track_ukraine['new deaths']:,}\n<b> 💪 Osoby, króte wyzdrowiały: </b>{track_ukraine['new recoveries']:,}"
    elif get_message_bot == "ukraine":
        track_ukraine =  track.country_info_by_name('ukraine')
        final_message = f"<u>National data:</u>\n<b> 👫 Population: </b>{track_ukraine['population']:,}\n"\
            f"<b> 🤧 Infected: </b>{track_ukraine['new cases']:,}\n<b> ☠️ Deaths: </b>"\
                f"{track_ukraine['new deaths']:,}\n<b> 💪 People who have recovered: </b>{track_ukraine['new recoveries']:,}"
    elif get_message_bot == "україна":
        track_ukraine =  track.country_info_by_name('ukraine')
        final_message = f"<u>Національні дані:</u>\n<b> 👫 Населення: </b>{track_ukraine['population']:,}\n"\
            f"<b> 🤧 Заражених: </b>{track_ukraine['new cases']:,}\n<b> ☠️ Смертей: </b>"\
                f"{track_ukraine['new deaths']:,}\n<b> 💪 Люди, які одужали: </b>{track_ukraine['new recoveries']:,}"
    #polska
    elif get_message_bot == "polska":
        track_poland =  track.country_info_by_name('poland')
        final_message = f"<u>Dane krajowe:</u>\n<b> 👫 Populacja: </b>{track_poland['population']:,}\n"\
            f"<b> 🤧 Zakażonych: </b>{track_poland['new cases']:,}\n<b> ☠️ Zgonów: </b>"\
                f"{track_poland['new deaths']:,}\n<b> 💪 Osoby, króte wyzdrowiały: </b>{track_poland['new recoveries']:,}"
    elif get_message_bot == "poland":
        track_poland =  track.country_info_by_name('poland')
        final_message = f"<u>National data:</u>\n<b> 👫 Population: </b>{track_poland['population']:,}\n"\
            f"<b> 🤧 Infected: </b>{track_poland['new cases']:,}\n<b> ☠️ Deaths: </b>"\
                f"{track_poland['new deaths']:,}\n<b> 💪 People who have recovered: </b>{track_poland['new recoveries']:,}"
    elif get_message_bot == "польща":
        track_poland =  track.country_info_by_name('poland')
        final_message = f"<u>Національні дані:</u>\n<b> 👫 Населення: </b>{track_poland['population']:,}\n"\
            f"<b> 🤧 Заражених: </b>{track_poland['new cases']:,}\n<b> ☠️ Смертей: </b>"\
                f"{track_poland['new deaths']:,}\n<b> 💪 Люди, які одужали: </b>{track_poland['new recoveries']:,}"
    #włochy
    elif get_message_bot == "włochy":
        track_italy =  track.country_info_by_name('italy')
        final_message = f"<u>Dane krajowe:</u>\n<b> 👫 Populacja: </b>{track_italy['population']:,}\n"\
            f"<b> 🤧 Zakażonych: </b>{track_italy['new cases']:,}\n<b> ☠️ Zgonów: </b>"\
                f"{track_italy['new deaths']:,}\n<b> 💪 Osoby, króte wyzdrowiały: </b>{track_italy['new recoveries']:,}"
    elif get_message_bot == "italy":
        track_italy =  track.country_info_by_name('italy')
        final_message = f"<u>National data:</u>\n<b> 👫 Population: </b>{track_italy['population']:,}\n"\
            f"<b> 🤧 Infected: </b>{track_italy['new cases']:,}\n<b> ☠️ Deaths: </b>"\
                f"{track_italy['new deaths']:,}\n<b> 💪 People who have recovered: </b>{track_italy['new recoveries']:,}"
    elif get_message_bot == "італія":
        track_italy =  track.country_info_by_name('italy')
        final_message = f"<u>Національні дані:</u>\n<b> 👫 Населення: </b>{track_italy['population']:,}\n"\
            f"<b> 🤧 Заражених: </b>{track_italy['new cases']:,}\n<b> ☠️ Смертей: </b>"\
                f"{track_italy['new deaths']:,}\n<b> 💪 Люди, які одужали: </b>{track_italy['new recoveries']:,}"
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
            f"<b>Najczęstsze objawy: </b>\n"\
                f"• gorączka\n"\
                    f"• suchy kaszel\n"\
                        f"• zmęczenie\n"\
                            f"<b>Mniej powszechne objawy: </b>\n"\
                                f"• bóle\n"\
                                    f"• ból gardła\n"\
                                        f"• biegunka\n"\
                                            f"• zapalenie spojówek\n"\
                                                f"• bół głowy\n"\
                                                    f"• utrata smaku lub zapachu\n"\
                                                        f"• wysypka na skórze lub przebarwienie palców rąk i nóg\n"
    elif get_message_bot == "коронавірус":
        final_message = f"COVID-19  🦠  по-різному впливає на різних людей. У більшості інфікованих людей розвиватиметься хвороба легкого та середнього ступеня тяжкості та одужуватиме без госпіталізації.\n"\
        f"<b>Найпоширеніші симптоми: </b>\n"\
            f"• лихоманка\n"\
                f"• сухий кашель\n"\
                    f"• втома\n"\
                        f"<b>Менш поширені симптоми: </b>\n"\
                            f"• ломота\n"\
                                f"• біль у горлі\n"\
                                    f"• діарея\n"\
                                        f"• кон’юнктивіт\n"\
                                            f"• головний біль\n"\
                                                f"• втрата смаку або запаху\n"\
                                                    f"• висип на шкірі або зміна кольору пальців рук або ніг\n"

    elif get_message_bot == "coronavirus":
        final_message = f"COVID-19  🦠  affects different people in different ways. Most infected people will develop mild to moderate illness and recover without hospitalization.\n"\
        f"<b> Most common symptoms: </b>\n"\
            f"• fever\n"\
                f"• dry cough\n"\
                    f"• tiredness\n"\
                        f"<b> Less common symptoms: </b>\n"\
                            f"• aches and pains\n"\
                                f"• sore throat\n"\
                                    f"• diarrhoea\n"\
                                        f"• кconjunctivitis\n"\
                                            f"• headache\n"\
                                                f"• loss of taste or smell\n"\
                                                    f"• a rash on skin, or discolouration of fingers or toes\n"
    #Protect yourself
    
    else:
        final_message = f"Proszę napisać nazwe kraju\n Jeśli chcesz dowiedzieć się dane z całego świata , napisz 'świat'"
    bot.send_message(message.chat.id, final_message, parse_mode='HTML')

bot.polling(none_stop=True, interval = 0)


