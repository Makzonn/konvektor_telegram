import requests
import json
from tkinter import *
from tkinter import messagebox, scrolledtext

def get_currency_list():
    return [
        'AED - Объединенные Арабские Эмираты',
        'AFN - Афганистан',
        'ALL - Албания',
        'AMD - Армения',
        'ANG - Нидерландские Антильские Острова',
        'AOA - Ангола',
        'ARS - Аргентина',
        'AUD - Австралия',
        'AWG - Аруба',
        'AZN - Азербайджан',
        #добавить
    ]

def convert_currency():
    from_currency = from_currency_entry.get().strip().upper()
    to_currency = to_currency_entry.get().strip().upper()
    amount = amount_entry.get().strip()

    if not amount.isdigit():
        messagebox.showerror("Ошибка", "Сумма должна быть числом.")
        return

    amount = float(amount)

    try:
        response = requests.get(f'https://open.er-api.com/v6/latest/{from_currency}')
        response.raise_for_status()
        rates = response.json().get('rates', {})
        if to_currency not in rates:
            messagebox.showerror("Ошибка", f"Валюта '{to_currency}' не найдена.")
            return

        conversion_rate = rates[to_currency]
        converted_amount = conversion_rate * amount
        result_text.set(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except requests.exceptions.RequestException:
        messagebox.showerror("Ошибка", "Ошибка при получении данных о валюте.")
    except KeyError:
        messagebox.showerror("Ошибка", "Ошибка в получении курса валют.")

def show_currency_list():
    currency_list = get_currency_list()
    currency_text = "\\n".join(currency_list)
    messagebox.showinfo("Список валют", currency_text)

#основное окно
window = Tk()
window.title("Конвертер валюты")

#поля для ввода
Label(window, text="Валюта из:").grid(row=0, column=0)
from_currency_entry = Entry(window)
from_currency_entry.grid(row=0, column=1)

Label(window, text="Валюта в:").grid(row=1, column=0)
to_currency_entry = Entry(window)
to_currency_entry.grid(row=1, column=1)

Label(window, text="Сумма:").grid(row=2, column=0)
amount_entry = Entry(window)
amount_entry.grid(row=2, column=1)

#кнопки
convert_button = Button(window, text="Конвертировать", command=convert_currency)
convert_button.grid(row=3, columnspan=2)

currency_list_button = Button(window, text="Показать список валют", command=show_currency_list)
currency_list_button.grid(row=4, columnspan=2)

#вывод поле
result_text = StringVar()
result_label = Label(window, textvariable=result_text)
result_label.grid(row=5, columnspan=2)

window.mainloop()