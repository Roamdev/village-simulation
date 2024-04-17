import psycopg2
from config import *


class DataBase:
    conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
    cur = conn.cursor()

    def __init__(self):
        self.conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
        self.cur = self.conn.cursor()

    def insert_person(self, gender, name, population, best_friend, alcohol,
                      sport, partner, never_given_birth, born_counter):
        self.cur.execute(
            "INSERT INTO persons (gender, name)"
            "VALUES (%s, %s);", [gender, name, population, best_friend, alcohol,
                                 sport, partner, never_given_birth, born_counter]
        )
        self.conn.commit()

    def get_all_persons(self):
        self.cur.execute(
            "SELECT * FROM persons;"
        )
        result = self.cur.fetchall()
        print(result)
        self.conn.commit()
        
    def close_connection(self):
        self.cur.close()
        self.conn.close()
    


# db = DataBase()
# db.insert_person(1,'Name')
print("Подключение установлено")
