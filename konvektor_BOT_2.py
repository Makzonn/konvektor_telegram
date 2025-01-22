import requests
import json
import telebot

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("список")
    markup.add("конвектор")
    bot.send_message(message.chat.id, 'Добро пожаловать в конвектор валюты:)', reply_markup=markup)
    bot.send_message(message.chat.id, 'если хотите узнать список валют напишите "список", а если перевести валюту напишите "конвектор"')

text_valut = [
    'AED Объединенные Арабские Эмираты', 'AFN Афганистан', 'ALL Албания', 'AMD Армения', 'ANG Нидерландские Антильские Острова',
    'AOA Ангола', 'ARS Аргентина', 'AUD Австралия', 'AWG Аруба', 'AZN Азербайджан', 'BAM Босния и Герцеговина', 'BBD Барбадос',
    'BDT Бангладеш', 'BGN Болгария', 'BHD Бахрейн', 'BIF Бурунди', 'BMD Бермудские острова', 'BND Бруней', 'BOB Боливия',
    'BRL Бразилия', 'BSD Багамские острова', 'BTN Бутан', 'BWP Ботсвана', 'BYN Беларусь', 'BZD Белиз', 'CAD Канада',
    'CDF Демократическая Республика Конго', 'CHF Швейцария', 'CLP Чили', 'CNY Китай', 'COP Колумбия', 'CRC Коста-Рика',
    'CUP Куба', 'CVE Кабо - Верде', 'CZK Чешская Республика', 'DJF Джибути', 'DKK Дания', 'DOP Доминиканская Республика',
    'DZD Алжир', 'EGP Египет', 'ERN Эритрея', 'ETB Эфиопия', 'EUR Европейский Союз', 'FJD Фиджи', 'FKP Фолклендские острова',
    'FOK Фарерские острова', 'GBP Великобритания', 'GEL Грузия', 'GGP Гернси', 'GHS Гана', 'GIP Гибралтар', 'GMD Гамбия',
    'GNF Гвинея', 'GTQ Гватемала', 'GYD Гайана', 'HKD Гонконг', 'HNL Гондурас', 'HRK Хорватия', 'HTG Гаити', 'HUF Венгрия',
    'IDR Индонезия', 'ILS Израиль', 'IMP Остров Мэн', 'INR Индия', 'IQD Ирак', 'IRR Иран', 'ISK Исландия', 'JEP Джерси',
    'JMD Ямайка', 'JOD Иордания', 'JPY Япония', 'KES Кения', 'KGS Кыргызстан', 'KHR Камбоджа', 'KID Кирибати',
    'KMF Коморские острова', 'KRW ЮЖНАЯ КОРЕЯ', 'KWD Кувейт', 'KYD Каймановы Острова', 'KZT Казахстан', 'LAK Лаос',
    'LBP Ливан', 'LKR Шри - Ланка', 'LRD Либерия', 'LSL Лесото', 'LYD Ливия', 'MAD Марокко', 'MDL Молдова', 'MGA Мадагаскар',
    'MKD Северная Македония', 'MOP Макао', 'MRU Мавритания', 'MUR Маврия', 'MVR Мальдивы', 'MWK Малави', 'MXN Мексика',
    'MYR Малайзия', 'MZN Мозамбик', 'NAD Намбия', 'NGN Нигерия', 'NIO Никарагуа', 'NOK Норвегия', 'NPR Непал',
    'NZD Новая Зеландия', 'OMR Оман', 'PAB Панама', 'PEN Перу', 'PGK Папуа-Новая Гвинея', 'PHP Филиппины', 'PKR Пакистан',
    'PLN Польша', 'PYG республика Парагва', 'QAR Катар', 'RON Румыния', 'RSD Сербия', 'RUB Россия', 'RWF Руанда',
    'SAR Саудовская Аравия', 'SBD Соломоновы Острова', 'SCR Сейшельские острова', 'SDG Судан', 'SEK Швеция', 'SGD Сингапур',
    'SHP Остров Святой Елены', 'SLE Сьерра - Леоне', 'SOS Сомали', 'SRD Суринам', 'SSP Южный Судан', 'STN São Tomé and Príncipe',
    'SYP Сирия', 'SZL Эсватини', 'THB Таиланд', 'TJS Таджикистан', 'TMT Туркменистан', 'TND Тунис', 'TOP Tonga', 'TRY Турция',
    'TTD Тринидад и Тобаго', 'TVD Тувалу', 'TWD Тайвань', 'TZS Танзания', 'UAH Украина', 'UGX Уганда', 'USD США', 'UYU Уругвай',
    'UZS Узбекистан', 'VES Венисуэла', 'VND Вьетнам', 'VUV Вануату', 'WST Самоа', 'XAF CEMAC', 'XCD Организация Восточнокарибских государств',
    'XDR Международный Валютный фонд', 'XOF западноафриканский франк', "XPF Collectivités d'Outre-Mer", 'YER Йемен', 'ZAR Южная Африка',
    'ZMW Замбия', 'ZWL Зимбабве'
]

@bot.message_handler(regexp='список')
def send_valut(message):
    bot.send_message(message.chat.id, "\\n".join(text_valut))

@bot.message_handler(regexp='конвектор')
def send_konvektor(message):
    msg = bot.send_message(message.chat.id, 'Напишите 3 основные букв валюты которую хотите перевести (например: USD):')
    bot.register_next_step_handler(msg, in_money)

def in_money(message):
    from_currency = message.text.upper()
    msg = bot.send_message(message.chat.id, 'Напишите 3 основные букв валюты в которую хотите перевести (например: USD):')
    bot.register_next_step_handler(msg, num_money, from_currency)

def num_money(message, from_currency):
    to_currency = message.text.upper()
    msg = bot.send_message(message.chat.id, 'Напишите сколько валюты хотите перевести:')
    bot.register_next_step_handler(msg, konv, from_currency, to_currency)

def konv(message, from_currency, to_currency):
    try:
        amount = float(message.text)
        response = requests.get(f'https://open.er-api.com/v6/latest/{from_currency}')
        if response.status_code == 200:
            data = response.json()
            if to_currency in data['rates']:
                rate = data['rates'][to_currency]
                converted_amount = amount * rate
                bot.send_message(message.chat.id, f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')
            else:
                bot.send_message(message.chat.id, 'Валюта для конвертации не найдена.')
        else:
            bot.send_message(message.chat.id, 'Ошибка при получении данных от API.')
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное число.')

bot.infinity_polling()
