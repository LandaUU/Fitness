from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    lastname = State()
    middlename = State()
    firstname = State()
    fio = State()
    height = State()
    age = State()
    birthday = State()
    gender = State()
    oauth_token = State()
    oauth_secret = State()

    def get_user_data(self):
        return 'ФИО: {}\nВозраст:{}\nРост:{}\nПол: {}'.format(self.fio, self.age, self.height, self.gender)


class UserScenarioState(StatesGroup):
    begin = State()
    check = State()
    save = State()
    clear = State()
