from . import users

def register_all_users_handlers(dp):
    users.register_all_main_handlers(dp)
    users.register_all_thresholds_handlers(dp)