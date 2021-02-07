import codecs
import telebot
from telebot import types
from covid19tracker import Tracker

bot = telebot.TeleBot('TELEGRAM TOKEN')
track = Tracker() 

database_path = 'users.json'
users = {}

info_corona_pl = ''
info_corona_ua = ''


with open('texts.txt', mode='r', encoding='utf8') as texts_file:
    lines = texts_file.readlines()
    info_corona_pl = lines[0]
    info_corona_ua = lines[1]


def add_or_update_user(user_id: int, language: str):
    """Adds or updates user languaghe in the .json database"""
    if user_id in users.keys():
        users[user_id]['language'] = language
    else:
        users[user_id] = {}
        users[user_id]['language'] = language

    saveToFile(users)


def saveToFile(dict):
    """Saves dict database to .json file"""
    f = codecs.open(database_path, "w", "utf-8")
    f.write(str(dict))
    f.close()


@bot.message_handler(commands=["start"])
def start(message):
    """Function which is started at start of a bot by the user"""
    send_message = (
        f"<b>Hej {message.from_user.first_name}! 👋</b>\n"
        "Proszę wybrać język:\n"
    )
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton("🇵🇱", callback_data="pl")
    btn2 = types.InlineKeyboardButton("🇺🇦", callback_data="ua")
    btn3 = types.InlineKeyboardButton("🇬🇧", callback_data="us")
    markup.add(btn1, btn2, btn3)
    bot.send_message(
        message.chat.id, send_message, parse_mode="html", reply_markup=markup
    )
    add_or_update_user(message.from_user.id, "🇬🇧")


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    """This function is triggered when the user changes"
    "the language and returns the bot menu in that language
    """
    add_or_update_user(call.from_user.id, call.data)
    if call.data == "pl":
        markup_reply1 = types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            row_width=2
        )

        btn_coronapl = types.KeyboardButton("Koronawirus")
        btn_savepl = types.KeyboardButton("Chroń siebie")
        btn_pl = types.KeyboardButton("Polska")
        btn_ua = types.KeyboardButton("Ukraina")
        btn_khnow = types.KeyboardButton("Dowiedzieć się więcej")
        markup_reply1.add(btn_coronapl, btn_savepl, btn_pl, btn_ua, btn_khnow)
        bot.send_message(
            call.message.chat.id,
            "Aby dowiedzieć się o koronawirusie 🦠,\nnapisz nazwę kraju 🌉\n"
            "Dostępne kraje:\n"
            "Stany zjednoczone\n"
            "Ukraina\n"
            "Polska\n"
            "Włochy\n"
            "Kazachstan\n"
            "Niemcy\n"
            "Czechy\n"
            "Węgry\n"
            "Białoruś\n"
            "Rosja\n"
            "Dania\n"
            "Francja\n"
            "Hiszpania\n"
            "Słowacja\n"
            "Chorwacja\n"
            "Słowenia\n"
            "Grecja\n"
            "Turcja\n"
            "Rumunia\n"
            "Bułgaria\n",
            reply_markup=markup_reply1,
        )
    elif call.data == "ua":
        markup_reply2 = types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            row_width=2
        )

        btn_coronaua = types.KeyboardButton("Коронавірус")
        btn_saveua = types.KeyboardButton(
            "Захисти себе"
        )
        btn_pl2 = types.KeyboardButton("Польща")
        btn_ua2 = types.KeyboardButton("Україна")
        btn_khnow2 = types.KeyboardButton("Дізнатися більше")
        markup_reply2.add(
            btn_coronaua,
            btn_saveua,
            btn_pl2,
            btn_ua2,
            btn_khnow2)
        bot.send_message(
            call.message.chat.id,
            "Щоб дізнатися дані про коронавірус 🦠,\n"
            "напишіть назву країни 🌉\n"
            "Доступні країни:\n"
            "Сша\n"
            "Україна\n"
            "Польща\n"
            "Італія\n"
            "Казахстан\n"
            "Німеччина\n"
            "Чехія\n"
            "Угорщина\n"
            "Білорусь\n"
            "Росія\n"
            "Данія\n"
            "Франція\n"
            "Іспанія\n"
            "Словаччина\n"
            "Хорватія\n"
            "Словенія\n"
            "Греція\n"
            "Туреччина\n"
            "Румунія\n"
            "Болгарія\n",
            reply_markup=markup_reply2,
        )
    elif call.data == "us":
        markup_reply3 = types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            row_width=2)
        btn_coronaus = types.KeyboardButton("Coronavirus")
        btn_saveus = types.KeyboardButton("Protect yourself")
        btn_pl3 = types.KeyboardButton("Poland")
        btn_ua3 = types.InlineKeyboardButton("Ukraine")
        markup_reply3.add(btn_coronaus, btn_saveus, btn_pl3, btn_ua3)
        bot.send_message(
            call.message.chat.id,
            "To find out about the coronavirus data 🦠,\n"
            "write the name of the country 🌉\n"
            "Available countries:\n"
            "Usa\n"
            "Ukraine\n"
            "Poland\n"
            "Italy\n"
            "Kazakhstan \n"
            "Germany\n"
            "Czech republic\n"
            "Hungary\n"
            "Belarus\n"
            "Russia\n"
            "Denmark\n"
            "France\n"
            "Spain\n"
            "Slovakia\n"
            "Croatia\n"
            "Slovenia\n"
            "Greece\n"
            "Turkey\n"
            "Romania\n"
            "Bulgaria\n",
            reply_markup=markup_reply3,
        )

@bot.message_handler(content_types=["text"])
def mess(message):
    """"This function is started at the incoming message and"
    "calculates the data for the country"
    "which the user will enter in that function"
    """
    bot.send_chat_action(message.chat.id, 'typing')

    final_message = "Please select language"
    if message.from_user.id in users.keys():
        if users[message.from_user.id]['language'] == "us":
            final_message = 'Type country name not wrong'
        if users[message.from_user.id]['language'] == "pl":
            final_message = 'Wpisz nazwę kraju poprawnie'
        if users[message.from_user.id]['language'] == "ua":
            final_message = 'Напиши назву країни правильно'

    get_message_bot = message.text.strip().lower()

    # dane z całego świata
    if (get_message_bot == "świat" or
            get_message_bot == "world" or
            get_message_bot == "світ"):
        cases = track.total_cases()
        deaths = track.total_deaths()
        rec = track.total_recoveries()

        if get_message_bot == "świat":
            final_message = "<i>Dane z całego świata 🌍:</i>\n"
            f"<b> 🤧 Zakażonych: </b>{cases:,}\n"
            f"<b> ☠️ Zgonów: </b>{deaths:,}\n"
            f"<b> 💪 Osoby, któte wyzdrowiały: </b>{rec:,}"

        elif get_message_bot == "world":
            final_message = "<i>Data from all over the world 🌍:</i>\n"
            f"<b> 🤧 Infected: </b>{cases:,}\n"
            f"<b> ☠️ Deaths: </b>{deaths:,}\n"
            f"<b> 💪 People who have recovered: </b>{rec:,}"

        elif get_message_bot == "світ":
            final_message = "<i>Дані з усього світу 🌍:</i>\n"
            f"<b> 🤧 Заражених: </b>{cases:,}\n"
            f"<b> ☠️ Смертей: </b>{deaths:,}\n"
            f"<b> 💪 Люди, які одужали: </b>{rec:,}"
    # Dowiedzieć się więcej
    elif get_message_bot == "dowiedzieć się więcej":
        final_message = info_corona_pl

    elif get_message_bot == "дізнатися більше":
        final_message = info_corona_ua

    # Info o koronawirusie
    elif get_message_bot == "koronawirus":
        final_message = (
            "COVID-19 🦠 wpływa na różnych ludzi na różne sposoby."
            "U większości zarażonych choroba rozwija się od łagodnej"
            "do umiarkowanej i wyzdrowieje bez hospitalizacji.\n"
            "<b>🔴 Najczęstsze objawy: </b>\n"
            "▪️ gorączka\n"
            "▪️ suchy kaszel\n"
            "▪️ zmęczenie\n"
            "<b>🔴 Mniej powszechne objawy: </b>\n"
            "▪️ bóle\n"
            "▪️ ból gardła\n"
            "▪️ biegunka\n"
            "▪️ zapalenie spojówek\n"
            "▪️ bół głowy\n"
            "▪️ utrata smaku lub zapachu\n"
            "▪️ wysypka na skórze lub przebarwienie palców rąk i nóg\n")

    elif get_message_bot == "коронавірус":
        final_message = (
            "COVID-19 🦠 по-різному впливає на різних людей."
            "У більшості інфікованих людей розвиватиметься хвороба легкого"
            "та середнього ступеня тяжкості та одужуватиме"
            "без госпіталізації.\n"
            "<b>🔴 Найпоширеніші симптоми: </b>\n"
            "▪️ лихоманка\n"
            "▪️ сухий кашель\n"
            "▪️ втома\n"
            "<b>🔴 Менш поширені симптоми: </b>\n"
            "▪️ ломота\n"
            "▪️ біль у горлі\n"
            "▪️ діарея\n"
            "▪️ кон’юнктивіт\n"
            "▪️ головний біль\n"
            "▪️ втрата смаку або запаху\n"
            "▪️ висип на шкірі або зміна кольору пальців рук або ніг\n")

    elif get_message_bot == "coronavirus":
        final_message = (
            "COVID-19 🦠 affects different people in different ways."
            "Most infected people will develop mild"
            "to moderate illness and recover"
            "without hospitalization.\n"
            "<b>🔴 Most common symptoms: </b>\n"
            "▪️ fever\n"
            "▪️ dry cough\n"
            "▪️ tiredness\n"
            "<b>🔴 Less common symptoms: </b>\n"
            "▪️ aches and pains\n"
            "▪️ sore throat\n"
            "▪️ diarrhoea\n"
            "▪️ кconjunctivitis\n"
            "▪️ headache\n"
            "▪️ loss of taste or smell\n"
            "▪️ a rash on skin, or discolouration of fingers or toes\n")
    # Protect yourself
    elif get_message_bot == "chroń siebie":
        final_message = (
            "📢 <i>Chroń siebie i innych wokół siebie, znając fakty"
            "i podejmując odpowiednie środki ostrożności."
            "Postępuj zgodnie z zaleceniami lokalnych władz zdrowotnych.</i>\n"
            "<b>🆘 Aby zapobiec rozprzestrzenianiu się COVID-19:</b>\n"
            "▪️ Często myj ręce. Użyj mydła i wody lub"
            "środka do dezynfekcji rąk na bazie alkoholu.\n"
            "▪️ Zachowaj bezpieczną odległość od każdego,"
            "kto kaszle lub kicha.\n"
            "▪️ Noś maskę, gdy dystans fizyczny nie jest możliwy.\n"
            "▪️ Nie dotykaj oczu, nosa ani ust.\n"
            "▪️ Zakrywaj nos i usta zgiętym łokciem lub chusteczką,"
            "gdy kaszlesz lub kichasz.\n"
            "▪️ Zostań w domu, jeśli źle się poczujesz.\n"
            "▪️ Jeśli masz gorączkę, kaszel i trudności w oddychaniu,"
            "zgłoś się do lekarza.\n"
            "<i>Zadzwoń z wyprzedzeniem, aby Twój lekarz szybko skierował Cię"
            "do właściwej placówki medycznej. Zapewnia to ochronę i"
            "zapobiega rozprzestrzenianiu się wirusów i innych infekcji.</i>")
    elif get_message_bot == "захисти себе":
        final_message = (
            "📢 <i>Захищайте себе та оточуючих, знаючи факти та вживаючи"
            "відповідних запобіжних заходів."
            "Дотримуйтесь порад, наданих місцевим"
            "органом охорони здоров’я.</i>\n"
            "<b>🆘 Щоб запобігти поширенню COVID-19: </b>\n"
            "▪️ Часто мийте руки. Використовуйте мило та воду"
            "або дезінфікуючий засіб для рук на спиртовій основі.\n"
            "▪️ Дотримуйтесь безпечної відстані від тих, хто кашляє чи чхає.\n"
            "▪️ Носіть маску, коли фізичне дистанціювання неможливе.\n"
            "▪️ Не торкайтесь очей, носа або рота.\n"
            "▪️ Під час кашлю чи чхання закривайте"
            "ніс і рот зігнутим ліктем або серветкою.\n"
            "▪️ Залишайтеся вдома, якщо вам погано.\n"
            "▪️ Якщо у вас температура, кашель і утруднення дихання,"
            "зверніться за медичною допомогою.\n"
            "<i>Заздалегідь зателефонувавши, ваш лікар може швидко"
            "направити вас до потрібного медичного закладу."
            "Це захищає вас і запобігає поширенню вірусів"
            "та інших інфекцій.</i>")
    elif get_message_bot == "protect yourself":
        final_message = (
            "📢 <i>Protect yourself and others around you"
            "by knowing the facts and taking appropriate precautions."
            "Follow advice provided by your local health authority.</i>\n"
            "<b>🆘 To prevent the spread of COVID-19: </b>\n"
            "▪️ Clean your hands often."
            "Use soap and water, or an alcohol-based hand sanitazer.\n"
            "▪️ Maintain a safe distance from"
            "anyone who is coughing or sneezing.\n"
            "▪️ Wear a mask when physical distancing is not possible.\n"
            "▪️ Don’t touch your eyes, nose or mouth.\n"
            "▪️ Cover your nose and mouth with your"
            "bent elbow or a tissue when you cough or sneeze.\n"
            "▪️ Stay home if you feel unwell.\n"
            "▪️ If you have a fever, cough and difficulty breathing,"
            "seek medical attention.\n"
            "<i>Calling in advance allows your healthcare provider to quickly"
            "direct you to the right health facility."
            "This protects you, and prevents the spread"
            "of viruses and other infections.</i>")

        # english: english, polish, ukrainian
    countries = [
        ["usa", "stany zjednoczone", "сша"],
        ["ukraine", "ukraina", "україна"],
        ["poland", "polska", "польща"],
        ["italy", "włochy", "італія"],
        ["kazakhstan", "kazachstan ", "казахстан"],
        ["germany", "niemcy", "німеччина"],
        ["czech republic", "czechy", "чехія"],
        ["hungary", "węgry", "угорщина"],
        ["belarus", "białoruś", "білорусь"],
        ["russia", "rosja", "росія"],
        ["denmark", "dania", "данія"],
        ["france", "francja", "франція"],
        ["spain", "hiszpania", "іспанія"],
        ["slovakia", "słowacja", "словаччина"],
        ["croatia", "chorwacja", "хорватія"],
        ["slovenia", "słowenia", "словенія"],
        ["greece", "grecja", "греція"],
        ["turkey", "turcja", "туреччина"],
        ["romania", "rumunia", "румунія"],
        ["bulgaria", "bułgaria", "болгарія"]
    ]

    for country in countries:
        if get_message_bot in country:
            index = country.index(get_message_bot)
            track_stats = track.country_info_by_name(country[0])

            if index == 0:  # english
                final_message = build_en_country_text(track_stats)
            if index == 1:  # polish
                final_message = build_pl_country_text(track_stats)
            if index == 2:  # ukrainian
                final_message = build_ua_country_text(track_stats)

            if final_message:
                bot.send_message(
                    message.chat.id,
                    final_message,
                    parse_mode='HTML')
            else:
                bot.send_message(
                    message.chat.id,
                    "Wystąpił błąd",
                    parse_mode='HTML')
            return

    bot.send_message(message.chat.id, final_message, parse_mode="HTML")


def build_en_country_text(country_stats):
    """Builds English version of covid info for taked country data"""

    final_message = "<b><u>National data:</u></b>\n"\
        f"<b> 👫 Population: </b>{country_stats['population']}\n"\
        "<b>For all time:</b>\n"\
        f"🤧 Infected: {country_stats['total cases']}\n"\
        "☠️ Deaths: "\
        f"{country_stats['total deaths']}\n"\
        f"💪 People who have recovered: {country_stats['total recoveries']}\n"\
        f"<b>Today: </b>\n 🤧 Infected: {country_stats['new cases']}\n"\
        "☠️ Deaths: "\
        f"{country_stats['new deaths']}\n"\
        f"💪 People who have recovered: {country_stats['new recoveries']}"
    return final_message


def build_ua_country_text(country_stats):
    """Builds version of covid info"
    "for taken country data in Ukrainian language
    """
    final_message = "<b><u>Національні дані:</u></b>\n"\
        f"<b> 👫 Населення: </b>{country_stats['population']}\n"\
        "<b>За весь час:</b>\n"\
        f"🤧 Заражених: {country_stats['total cases']}\n"\
        "☠️ Смертей: "\
        f"{country_stats['total deaths']}\n"\
        f"💪 Люди, які одужали: {country_stats['total recoveries']}\n"\
        "<b>За сьогодні: </b>\n"\
        f"🤧 Заражених: {country_stats['new cases']}\n"\
        "☠️ Смертей: "\
        f"{country_stats['new deaths']}\n"\
        f"💪 Люди, які одужали: {country_stats['new recoveries']}"
    return final_message


def build_pl_country_text(country_stats):
    """Builds version of covid info"
    "for taken country data in Polish language
    """
    final_message = "<b><u>Dane krajowe:</u></b>\n"\
        f"<b> 👫 Populacja: </b>{country_stats['population']}\n"\
        "<b>Przez cały czas:</b>\n"\
        f"🤧 Zakażonych:{country_stats['total cases']}\n"\
        "☠️ Zgonów: "\
        f"{country_stats['total deaths']}\n"\
        f"💪 Osoby, króte wyzdrowiały: {country_stats['total recoveries']}\n"\
        "<b>Dzisiaj: </b>\n"\
        f"🤧 Zakażonych: {country_stats['new cases']}\n ☠️ Zgonów: "\
        f"{country_stats['new deaths']}\n"\
        f"💪 Osoby, króte wyzdrowiały: {country_stats['new recoveries']}"
    return final_message


bot.polling(none_stop=True, interval=0)
