from telebot import types


def start_keyaboart():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton("🛢Нефть(BRENT)🛢")
    btn2 = types.KeyboardButton("💎Золото💎")
    btn3 = types.KeyboardButton("⛽️Газ⛽️")
    btn4 = types.KeyboardButton("💸Доллар💸")
    btn5 = types.KeyboardButton("💰Купить💰")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4, btn5)
    return markup


def buy_keyaboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton("Нефть(BRENT)🛢")
    btn2 = types.KeyboardButton("Золото💎")
    btn3 = types.KeyboardButton("Газ⛽️")
    btn4 = types.KeyboardButton("Доллар💸")
    btn5 = types.KeyboardButton("Назад🔙")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4, btn5)
    return markup


def analytics_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton("Новости📬")
    btn2 = types.KeyboardButton("Аналитика📊")
    btn3 = types.KeyboardButton("Назад")
    markup.add(btn1, btn2)
    markup.add(btn3)
    return markup


def button_url(url):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт", url=url)
    keyboard.add(url_button)
    return keyboard

def sale_and_purchase(url1, url2):
    keyboard = types.InlineKeyboardMarkup()
    url_button1 = types.InlineKeyboardButton(text="Купить", url=url1)
    url_button2 = types.InlineKeyboardButton(text="Продать", url=url2)
    keyboard.add(url_button1)
    keyboard.add(url_button2)
    return keyboard


