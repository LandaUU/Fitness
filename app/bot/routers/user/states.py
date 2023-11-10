from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    lastname = State()
    middlename = State()
    firstname = State()
    fio = State()
    height = State()
    physical_level = State()
    sickness = State()
    losing_weight_level = State()
    losing_weight_in_half_year_level = State()
    age = State()
    birthday = State()
    gender = State()
    oauth_token = State()
    oauth_secret = State()

    def get_user_data(self):
        return 'ФИО: {}\nВозраст:{}\nРост:{}\nПол: {}\nУровень физ.нагрузок: {}\nДиагностированные заболевания: {}\nОпыт похудения: {}\nХудел(а) ли в последние полгода: {}'.format(self.fio, self.age, self.height, self.gender, self.physical_level, self.sickness, self.losing_weight_level, self.losing_weight_in_half_year_level)


class UserScenarioState(StatesGroup):
    begin = State()
    check = State()
    save = State()
    clear = State()
