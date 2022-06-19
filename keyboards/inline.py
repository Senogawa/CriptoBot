from aiogram import types

menu_board = types.InlineKeyboardMarkup(row_width = 2)
menu_board.add(
    types.InlineKeyboardButton("Порог покупки", callback_data = "buy_threshold"),
    types.InlineKeyboardButton("Порог продажи", callback_data = "sell_threshold")
)

back_board = types.InlineKeyboardMarkup(row_width = 1).add(types.InlineKeyboardButton("Назад", callback_data = "back"))
start_board = types.InlineKeyboardMarkup(row_width = 1).add(types.InlineKeyboardButton("Начать", callback_data = "start"))
set_menu_s_board = types.InlineKeyboardMarkup(row_width = 1).add(
    types.InlineKeyboardButton("Вернуться в меню", callback_data = "main_menu"),
    types.InlineKeyboardButton("Ввести еще раз", callback_data = "newtry_sell")
    )

set_menu_b_board = types.InlineKeyboardMarkup(row_width = 1).add(
    types.InlineKeyboardButton("Вернуться в меню", callback_data = "main_menu"),
    types.InlineKeyboardButton("Ввести еще раз", callback_data = "newtry_buy")
    )