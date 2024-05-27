import psycopg2
from config import *


class DataBase:
    conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
    cur = conn.cursor()
    
    def __init__(self):
        self.conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
        self.cur = self.conn.cursor()
    
    def insert_person(self, gender, name, population=None, best_friend=None, alcohol=False,
                      sport=False, partner=None, never_given_birth=False, born_counter='0'):
        self.cur.execute(
            "INSERT INTO persons (gender, name, population, best_friend, alcohol,"
            "sport, partner, never_given_birth, born_counter)"
            "VALUES (%s, %s, %s, %s,%s, %s,%s, %s, %s);", [gender, name, population, best_friend, alcohol,
                                                           sport, partner, never_given_birth, born_counter]
        )
        self.conn.commit()
    
    # population, best_friend, alcohol, sport, partner,"
    #             "never_given_birth, born_counter)"
    #             "VALUES (%s, %s);", [gender, name, population, best_friend, alcohol,
    #                                  sport, partner, never_given_birth, born_counter]
    #         )
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
