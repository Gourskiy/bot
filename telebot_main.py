from pars import get_price, pars_gaz, pars_prime, pars_dollar, pars_zoloto, analytics_a, comparison
from config import bot
from main_keyboart import start_keyaboart, buy_keyaboard, analytics_keyboard, button_url, sale_and_purchase



@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Выберите интересующую вас функцию", reply_markup=start_keyaboart())

@bot.message_handler(content_types=["text"])
def command(message):
    if message.text == '⛽️Газ⛽️':
        news = pars_gaz()
        analytics = analytics_a('https://ru.tradingview.com/ideas/газ/')
        bot.send_message(message.chat.id, "Выберите интересующую вас функцию", reply_markup=analytics_keyboard())
        bot.register_next_step_handler(message, analytics_and_news, news, analytics)
    elif message.text == '🛢Нефть(BRENT)🛢':
        title = pars_prime()
        analytics = analytics_a('https://ru.tradingview.com/ideas/нефть/')
        bot.send_message(message.chat.id, "Выберите интересующую вас функцию", reply_markup=analytics_keyboard())
        bot.register_next_step_handler(message, analytics_and_news, title, analytics)
    elif message.text == '💎Золото💎':
        news = pars_zoloto()
        analytics = analytics_a('https://ru.tradingview.com/ideas/gold/')
        bot.send_message(message.chat.id, "Выберите интересующую вас функцию", reply_markup=analytics_keyboard())
        bot.register_next_step_handler(message, analytics_and_news, news, analytics)
    elif message.text == '💸Доллар💸':
        news = pars_dollar()
        analytics = analytics_a('https://ru.tradingview.com/ideas/доллар/')
        bot.send_message(message.chat.id, "Выберите интересующую вас функцию", reply_markup=analytics_keyboard())
        bot.register_next_step_handler(message, analytics_and_news, news, analytics)
    elif message.text == '💰Купить💰':
        bot.send_message(message.chat.id, "Выберите интересующую вас функцию", reply_markup=buy_keyaboard())
        bot.register_next_step_handler(message, buy_command)


def buy_command(message):
    text = message.text
    if text == 'Нефть(BRENT)🛢':
        price = get_price("oil")
        bot.send_message(message.from_user.id, f'Текущая цена на {message.text} - {price}')
        repeat_buy(message)
    elif text == 'Золото💎':
        price = get_price("gold")
        bot.send_message(message.from_user.id, f'Текущая цена на {message.text} - {price}')
        repeat_buy(message)
    elif text == 'Газ⛽️':
        price = get_price("gas")
        bot.send_message(message.from_user.id, f'Текущая цена на {message.text} - {price}')
        repeat_buy(message)
    elif text == 'Доллар💸':
        bot.send_message(message.from_user.id, f'Проверяем курсы...')
        price = comparison()
        bot.send_message(message.from_user.id, f'Покупка - {price[0].split(",: ")[0]}\nПродажа - {price[1].split(",: ")[0]}', reply_markup=sale_and_purchase(price[0].split(",: ")[1], price[1].split(",: ")[1]))
        repeat_buy(message)
    elif text == 'Назад🔙':
        bot.send_message(message.chat.id, "Выберите интересующую вас функцию", reply_markup=start_keyaboart())
        bot.register_next_step_handler(message, command)
    else:
        bot.send_message(message.chat.id, "Такой команды у меня нет😢\nПопробуйте еще раз...")
        repeat_buy(message)

def repeat_buy(message):
    bot.register_next_step_handler(message, buy_command)


def analytics_and_news(message, news, analytics):
    text = message.text
    if text == 'Новости📬':
        for new in news:
            bot.send_message(message.from_user.id, new.split(',:')[0], reply_markup=button_url(new.split(',: ')[1]))
        repeat_analytic_and_news(message, news, analytics)
    elif text == 'Аналитика📊':
        for analytic in analytics:
            bot.send_message(message.from_user.id, analytic, reply_markup=button_url(analytic.split(',: ')[1]))
        repeat_analytic_and_news(message, news, analytics)
    elif text == 'Назад':
        bot.send_message(message.chat.id, "Выберите интересующую вас функцию", reply_markup=start_keyaboart())
        bot.register_next_step_handler(message, command)

def repeat_analytic_and_news(message, news, analytics):
    bot.register_next_step_handler(message, analytics_and_news, news, analytics)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
