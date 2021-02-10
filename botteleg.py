import codecs
from string import Template
import telebot
from telebot import types
from covid19tracker import Tracker
from templates.txt_handler import get_from_txt

bot = telebot.TeleBot('TELEGRAM TOKEN')
track = Tracker()

database_path = 'users.json'
users = {}

info_corona_pl = ''
info_corona_ua = ''

en_country_text = get_from_txt("templates/en/country_text_en.txt")
pl_country_text = get_from_txt("templates/pl/country_text_pl.txt")
ua_country_text = get_from_txt("templates/ua/country_text_ua.txt")

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
            get_from_txt("templates/pl/countries_pl.txt"),
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
            btn_coronaua, btn_saveua, btn_pl2, btn_ua2, btn_khnow2)
        bot.send_message(
            call.message.chat.id,
            get_from_txt("templates/ua/countries_ua.txt"),
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
            get_from_txt("templates/en/countries_en.txt"),
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

    # Dowiedzieć się więcej
    if get_message_bot == "dowiedzieć się więcej":
        final_message = info_corona_pl

    elif get_message_bot == "дізнатися більше":
        final_message = info_corona_ua

    # Info o koronawirusie
    elif get_message_bot == "koronawirus":
        final_message = (get_from_txt("templates/pl/coronavirus_pl.txt"))
    elif get_message_bot == "коронавірус":
        final_message = (get_from_txt("templates/ua/coronavirus_ua.txt"))
    elif get_message_bot == "coronavirus":
        final_message = (get_from_txt("templates/en/coronavirus_en.txt"))
    # Protect yourself
    elif get_message_bot == "chroń siebie":
        final_message = (get_from_txt("templates/pl/protect_pl.txt"))
    elif get_message_bot == "захисти себе":
        final_message = (get_from_txt("templates/ua/protect_ua.txt"))
    elif get_message_bot == "protect yourself":
        final_message = (get_from_txt("templates/en/protect_en.txt"))

    # english, polish, ukrainian
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

            final_message = build_country_text(track_stats, language=index)

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


def build_country_text(country_stats, language):
    """Builds English version of covid info for taked country data"""

    template = None
    if language == 0:
        template = Template(en_country_text)
    if language == 1:
        template = Template(pl_country_text)
    if language == 2:
        template = Template(ua_country_text)

    final_message = template.substitute(
        population=country_stats['population'],
        total_cases=country_stats['total cases'],
        total_deaths=country_stats['total deaths'],
        total_recoveries=country_stats['total recoveries'],
        new_cases=country_stats['new cases'],
        new_deaths=country_stats['new deaths'],
        new_recoveries=country_stats['new recoveries'],
    )
    return final_message


bot.polling(none_stop=True, interval=0)
