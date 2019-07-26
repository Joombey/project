from function import SQL

class vkbot:
    def __init__(self, user_id):
        self.User_id = user_id
        self.Commands = ['старт', 'доход', 'расход', 'расчет']

    def new_msg(self, message):
        func = SQL(self.User_id)
        if message.lower() == self.Commands[0]:
            func.get_conn()
            func.add_data()
            return 'Финансовый помощник активирован'
        elif self.Commands[1] in message.lower():
            func.add_income(message[6:])
            return 'Принято'
        elif self.Commands[2] in message.lower():
            func.add_residue(message[7:])
            return 'Принято'
        elif message.lower() == self.Commands[3]:
            func.add_result()
            result = str(func.select_result)
            return 'Бюджет на день - ' + result
        else: return 'Неизвестная команда'
