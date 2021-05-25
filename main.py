from typing import Text
import telebot
import os.path
from token_key import key
from fpdf import FPDF
from telebot import types
from vendor.kermi.kermi_pdf import *

bot = telebot.TeleBot(key)

#---------------------------Кнопки клавиатуры-----------------------------------------------------
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    keyboard_main_menu   = types.InlineKeyboardMarkup()

    item_1   = types.InlineKeyboardButton(text = 'Тёплый пол', callback_data = 'item_1')
    item_2   = types.InlineKeyboardButton(text = 'Ничего',     callback_data = 'item_2')

    f = open('name.txt', 'w')
    f.write(message.from_user.first_name)
    f.close()

    bot.reply_to(message, f'Привет!, {message.from_user.first_name} Я помошник по расчётам систем отопления и водоснобжения!')
    keyboard_main_menu.add(item_1)
    keyboard_main_menu.add(item_2)
    bot.send_message(message.chat.id, 'Выбери что ты хочешь что бы я посчитал:', reply_markup=keyboard_main_menu)

@bot.callback_query_handler(func=lambda call:True)
def call_handler(call):

    keyboard_second_menu = types.InlineKeyboardMarkup()

    item_1_1 = types.InlineKeyboardButton(text = 'Kermi',      callback_data = 'item_1_1')
    item_1_2 = types.InlineKeyboardButton(text = 'Еще фирма',  callback_data = 'item_1_2')
    item_2_1 = types.InlineKeyboardButton(text = 'Ничего',     callback_data = 'item_2_1')
    item_2_2 = types.InlineKeyboardButton(text = 'Ничего',     callback_data = 'item_2_2')

    if call.data == "item_1":
        keyboard_second_menu.add(item_1_1)
        keyboard_second_menu.add(item_1_2)
        bot.send_message(call.message.chat.id, text="Выбери фирму производителя комплектующих", reply_markup=keyboard_second_menu)
    elif call.data == "item_1_1":
        call_address(call)
    elif call.data == "item_1_2":
        pass
    elif call.data == "item_2":
        keyboard_second_menu.add(item_2_1)
        keyboard_second_menu.add(item_2_2)
        bot.send_message(call.message.chat.id, text="Выбери ничего", reply_markup=keyboard_second_menu)
    elif call.data == "item_2_1":
        pass
    elif call.data == "item_2_2":
        pass

#------------------------Обработка кнопки item_1_1----------------------------------------------------------------------------
def call_address(call):
    msgPrice = bot.send_message(call.message.chat.id, 'Для начала введите адрес:')
    bot.register_next_step_handler(msgPrice, set_address)

def set_address(call):
    f = open('vendor/kermi/var/address.txt', 'w')
    f.write(call.text)
    f.close()
    msgPrice = bot.send_message(call.chat.id, 'Введите площадь отапливаемого помешения:')
    bot.register_next_step_handler(msgPrice, set_area)

def set_area(call):
    f = open('vendor/kermi/var/area.txt', 'w')
    f.write(call.text)
    f.close()
    msgPrice = bot.send_message(call.chat.id, 'Утеплен ли дом: введите 1 если да, 0 если нет')
    bot.register_next_step_handler(msgPrice, set_warm_house)

def set_warm_house(call):
    f = open('vendor/kermi/var/warm_house.txt', 'w')
    f.write(call.text)
    f.close()
    msgPrice = bot.send_message(call.chat.id, 'Количество комнат с теплым полом: 2 - 12:')
    bot.register_next_step_handler(msgPrice , set_number_of_rooms)

def set_number_of_rooms(call=1): 
    f = open('vendor/kermi/var/number_of_rooms.txt', 'w')
    f.write(call.text)
    f.close()
    create_pdf()
    bot.send_document(call.chat.id, open(r'vendor/kermi/your_calculation.pdf', 'rb'))

    os.remove('vendor/kermi/var/address.txt')
    os.remove('vendor/kermi/var/area.txt')
    os.remove('vendor/kermi/var/number_of_rooms.txt')
    os.remove('vendor/kermi/var/warm_house.txt')
    os.remove('name.txt')
    os.remove('vendor/kermi/your_calculation.pdf')

#------------------------Конец обработки кнопки item_1_1----------------------------------------------------------------------------

bot.polling(none_stop=True)
