import sqlite3 as sql
import calendar
import datetime

#user = input()

class SQL:
    def __init__(self, user):
        self.User = 'name'+str(user)
    
    def open_conn(self):
        self.conn = sql.connect("base_db.sqlite")
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def close_conn(self, conn, cur):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def get_conn(self):
        conn, cur = self.open_conn()
        cur.execute("CREATE TABLE IF NOT EXISTS %s (income INTEGER, residue INTEGER, daily_res INTEGER, data TEXT)" %self.User)
        self.close_conn(conn, cur)

    def add_income(self, value):
        conn, cur = self.open_conn()
        cur.execute("UPDATE %s SET income = %s WHERE data = %s" %(self.User, value, str(datetime.datetime.now())[:10].replace('-', '')))
        self.close_conn(conn, cur)

    def add_residue(self, value):
        conn, cur = self.open_conn()
        cur.execute("UPDATE %s SET residue = %s WHERE data = %s" %(self.User, value, str(datetime.datetime.now())[:10].replace('-', '')))
        self.close_conn(conn, cur)

    def add_data(self):
        conn, cur = self.open_conn()
        temp = str(datetime.datetime.now())[:10].replace('-', '')
        print(temp)
        cur.execute("INSERT INTO %s (data) VALUES (%s)" %(self.User, temp)) 
        self.close_conn(conn, cur)

    def add_result(self):
        conn, cur = self.open_conn()
        now = datetime.datetime.now()
        temp = str(now)[:10].replace('-', '')
        days = calendar.monthrange(now.year, now.month)[1]
        cur.execute("SELECT (income) FROM %s WHERE data = %s" %(self.User, temp))
        for i in cur: 
            temp_income = i[0]
        cur.execute("SELECT (residue) FROM %s WHERE data = %s" %(self.User, temp))
        for i in cur:
            temp_residue = i[0]
        cur.execute("UPDATE %s SET daily_res = %d" %(self.User, (temp_income - temp_residue)/days))
        self.close_conn(conn, cur)

    def select_result(self):
        conn, cur = self.open_conn()
        cur.execute("SELECT (daily_res) FROM %s WHERE data = %s" %(self.User, str(datetime.datetime.now())[:10]))
        for i in cur: 
            daily_res_send = i[0]
        if cur.fetchall() == (): daily_res_send = 'Неполный ввод'
        self.close_conn(conn, cur)
        return daily_res_send
