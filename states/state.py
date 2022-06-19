from aiogram.dispatcher.filters.state import StatesGroup, State

class BotStates(StatesGroup):
    main_menu_state = State()
    buy_threshold_state = State()
    sell_threshold_state = State()