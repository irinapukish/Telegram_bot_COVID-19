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
        btn_pl = types.KeyboardButton ('Polska')
        btn_ua = types.KeyboardButton ('Ukraina')
        btn_khnow =types.KeyboardButton('Dowiedzieć się więcej')
        markup_reply1.add(btn_coronapl, btn_savepl, btn_pl, btn_ua, btn_khnow)
        bot.send_message(call.message.chat.id, "Aby dowiedzieć się danych o koronawirusie 🦠,\nnapisz nazwę kraju 🌉",
        reply_markup= markup_reply1)
        
    elif call.data == 'ua':
        markup_reply2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
        btn_coronaua = types.KeyboardButton ('Коронавірус')
        btn_saveua = types.KeyboardButton ('Захисти себе')
        btn_pl2 = types.KeyboardButton ('Польща')
        btn_ua2 = types.KeyboardButton ('Україна')
        btn_khnow2 = types.KeyboardButton('Дізнатися більше')
        markup_reply2.add(btn_coronaua, btn_saveua, btn_pl2, btn_ua2, btn_khnow2)
        bot.send_message(call.message.chat.id, "Щоб дізнатися дані про коронавірус 🦠,\nнапишіть назву країни 🌉",
        reply_markup= markup_reply2)
    elif call.data == 'us':
        markup_reply3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2)
        btn_coronaus = types.KeyboardButton ('Coronavirus')
        btn_saveus = types.KeyboardButton ('Protect yourself')
        btn_pl3 = types.KeyboardButton ('Poland')
        btn_ua3 = types.InlineKeyboardButton ('Ukraine')
        markup_reply3.add(btn_coronaus, btn_saveus,btn_pl3, btn_ua3)
        bot.send_message(call.message.chat.id, "To find out about the coronavirus data 🦠,\nwrite the name of the country 🌉",
        reply_markup= markup_reply3)

    
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    
    get_message_bot = message.text.strip().lower()
    
    #dane z całego świata
    if  get_message_bot == "świat":
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
    #Dowiedzieć się więcej
    elif get_message_bot == "dowiedzieć się więcej":
        final_message = f"<b>🔎 Bardziej szczegółowe zapoznanie się z aktualnościami dotyczącymi koronawirusa można znaleźć tutaj:</b> \n https://www.gov.pl/web/koronawirus"

    elif get_message_bot == "дізнатися більше":
        final_message = f"<b>🔎 Для більш детальним ознайомлення з актуальностями про коронавірус можна дізнатися тут:</b> \n https://moz.gov.ua/koronavirus-2019-ncov"
   
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
    #usa
    elif get_message_bot == "stany zjednoczone":
        track_stats =  track.country_info_by_name('usa')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "usa":
        track_stats =  track.country_info_by_name('usa')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "сша":
        track_stats =  track.country_info_by_name('usa')
        final_message = build_ua_country_text(track_stats)
    #ukraina
    elif get_message_bot == "ukraina":
        track_stats =  track.country_info_by_name('ukraine')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "poland":
        track_stats =  track.country_info_by_name('ukraine')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "україна":
        track_stats =  track.country_info_by_name('ukraine')
        final_message = build_ua_country_text(track_stats)
    #polska
    elif get_message_bot == "polska":
        track_stats =  track.country_info_by_name('poland')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "poland":
        track_stats =  track.country_info_by_name('poland')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "польща":
        track_stats =  track.country_info_by_name('poland')
        final_message = build_ua_country_text(track_stats)
    #włochy
    elif get_message_bot == "włochy":
        track_stats =  track.country_info_by_name('italy')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "italy":
        track_stats =  track.country_info_by_name('italy')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "італія":
        track_stats =  track.country_info_by_name('italy')
        final_message = build_ua_country_text(track_stats)
    #Kazachstan
    elif get_message_bot == "kazachstan":
        track_stats =  track.country_info_by_name('kazakhstan')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "kazakhstan":
        track_stats =  track.country_info_by_name('kazakhstan')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "казахстан":
        track_stats =  track.country_info_by_name('kazakhstan')
        final_message = build_ua_country_text(track_stats)
    #Niemcy
    elif get_message_bot == "niemcy":
        track_stats =  track.country_info_by_name('germany')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "germany":
        track_stats =  track.country_info_by_name('germany')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "німеччина":
        track_stats =  track.country_info_by_name('germany')
        final_message = build_ua_country_text(track_stats)
    #Czechy
    elif get_message_bot == "czechy":
        track_stats =  track.country_info_by_name('czechia')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "czechia":
        track_stats =  track.country_info_by_name('czechia')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "чехія":
        track_stats =  track.country_info_by_name('czechia')
        final_message = build_ua_country_text(track_stats)
    #Węgry
    elif get_message_bot == "węgry":
        track_stats =  track.country_info_by_name('hungary')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "hungary":
        track_stats =  track.country_info_by_name('hungary')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "угорщина":
        track_stats =  track.country_info_by_name('hungary')
        final_message = build_ua_country_text(track_stats)
    #Białoruś
    elif get_message_bot == "białoruś":
        track_stats =  track.country_info_by_name('belarus')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "belarus":
        track_stats =  track.country_info_by_name('belarus')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "білорусь":
        track_stats =  track.country_info_by_name('belarus')
        final_message = build_ua_country_text(track_stats)
    #Rosja
    elif get_message_bot == "rosja":
        track_stats =  track.country_info_by_name('russia')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "russia":
        track_stats =  track.country_info_by_name('russia')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "росія":
        track_stats =  track.country_info_by_name('russia')
        final_message = build_ua_country_text(track_stats)
    #Dania
    elif get_message_bot == "hiszdaniapania":
        track_stats =  track.country_info_by_name('denmark')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "denmark":
        track_stats =  track.country_info_by_name('denmark')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "данія":
        track_stats =  track.country_info_by_name('denmark')
        final_message = build_ua_country_text(track_stats)
    #Francja
    elif get_message_bot == "francja":
        track_stats =  track.country_info_by_name('france')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "france":
        track_stats =  track.country_info_by_name('france')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "франція":
        track_stats =  track.country_info_by_name('france')
        final_message = build_ua_country_text(track_stats)
    #Hiszpania
    elif get_message_bot == "hiszpania":
        track_stats =  track.country_info_by_name('spain')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "spain":
        track_stats =  track.country_info_by_name('spain')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "іспанія":
        track_stats =  track.country_info_by_name('spain')
        final_message = build_ua_country_text(track_stats)
    #Słowacja
    elif get_message_bot == "słowacja":
        track_stats =  track.country_info_by_name('slovakia')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "slovakia":
        track_stats =  track.country_info_by_name('slovakia')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "словаччина":
        track_stats =  track.country_info_by_name('slovakia')
        final_message = build_ua_country_text(track_stats)
    #Chorwacja
    elif get_message_bot == "chorwacja":
        track_stats =  track.country_info_by_name('croatia')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "croatia":
        track_stats =  track.country_info_by_name('croatia')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "хорватія":
        track_stats =  track.country_info_by_name('croatia')
        final_message = build_ua_country_text(track_stats)
    #Słowenia
    elif get_message_bot == "słowenia":
        track_stats =  track.country_info_by_name('slovenia')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "slovenia":
        track_stats =  track.country_info_by_name('slovenia')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "словенія":
        track_stats =  track.country_info_by_name('slovenia')
        final_message = build_ua_country_text(track_stats)
    #Grecja
    elif get_message_bot == "grecja":
        track_stats =  track.country_info_by_name('greece')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "greece":
        track_stats =  track.country_info_by_name('greece')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "греція":
        track_stats =  track.country_info_by_name('greece')
        final_message = build_ua_country_text(track_stats)
    #Turcja
    elif get_message_bot == "turcja":
        track_stats =  track.country_info_by_name('turkey')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "turkey":
        track_stats =  track.country_info_by_name('turkey')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "туреччина":
        track_stats =  track.country_info_by_name('turkey')
        final_message = build_ua_country_text(track_stats)
    #Rumunia
    elif get_message_bot == "rumunia":
        track_stats =  track.country_info_by_name('romania')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "romania":
        track_stats =  track.country_info_by_name('romania')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "румунія":
        track_stats =  track.country_info_by_name('romania')
        final_message = build_ua_country_text(track_stats)
        #Bułgaria
    elif get_message_bot == "bułgaria":
        track_stats =  track.country_info_by_name('bulgaria')
        final_message = build_pl_country_text(track_stats)
    elif get_message_bot == "bulgaria":
        track_stats =  track.country_info_by_name('bulgaria')
        final_message = build_en_country_text(track_stats)
    elif get_message_bot == "болгарія":
        track_stats =  track.country_info_by_name('bulgaria')
        final_message = build_ua_country_text(track_stats)
    else:
        final_message = f"Proszę napisać nazwę kraju\n Jeśli chcesz dowiedzieć się dane z całego świata , napisz 'świat'"
    bot.send_message(message.chat.id, final_message, parse_mode='HTML')
     #texter
def build_en_country_text(country_stats):
    final_message = f"<b><u>National data:</u></b>\n<b> 👫 Population: </b>{country_stats['population']:,}\n"
    final_message += f"<b>For all time:</b>\n 🤧 Infected: {country_stats['total cases']:,}\n ☠️ Deaths: "
    final_message += f"{country_stats['total deaths']:,}\n 💪 People who have recovered: {country_stats['total recoveries']:,}\n"
    final_message +=  f"<b>Today: </b>\n 🤧 Infected: {country_stats['new cases']:,}\n ☠️ Deaths: "
    final_message +=  f"{country_stats['new deaths']:,}\n 💪 People who have recovered: {country_stats['new recoveries']:,}"
    return final_message

def build_ua_country_text(country_stats):
    final_message = f"<b><u>Національні дані:</u></b>\n<b> 👫 Населення: </b>{country_stats['population']:,}\n"
    final_message += f"<b>За весь час:</b>\n 🤧 Заражених: {country_stats['total cases']:,}\n ☠️ Смертей: "
    final_message += f"{country_stats['total deaths']:,}\n 💪 Люди, які одужали: {country_stats['total recoveries']:,}\n"
    final_message +=  f"<b>За сьогодні: </b>\n 🤧 Заражених: {country_stats['new cases']:,}\n ☠️ Смертей: "
    final_message +=  f"{country_stats['new deaths']:,}\n 💪 Люди, які одужали: {country_stats['new recoveries']:,}"
    return final_message

def build_pl_country_text(country_stats):
    final_message = f"<b><u>Dane krajowe:</u></b>\n<b> 👫 Populacja: </b>{country_stats['population']:,}\n"
    final_message += f"<b>Przez cały czas:</b>\n 🤧 Zakażonych: {country_stats['total cases']:,}\n ☠️ Zgonów: "
    final_message += f"{country_stats['total deaths']:,}\n 💪  Osoby, króte wyzdrowiały: {country_stats['total recoveries']:,}\n"
    final_message +=  f"<b>Dzisiaj: </b>\n 🤧 Zakażonych: {country_stats['new cases']:,}\n ☠️ Zgonów: "
    final_message +=  f"{country_stats['new deaths']:,}\n 💪 Osoby, króte wyzdrowiały: {country_stats['new recoveries']:,}"
    return final_message
    

bot.polling(none_stop=True, interval = 0)
