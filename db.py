import psycopg2
from config import *

conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
cur = conn.cursor()


def insert_person(gender, name):
    cur.execute(
        "INSERT INTO persons (gender, name)"
        "VALUES (%s, %s);", [gender, name]
    )
insert_person(1, 'Mirza')
def get_all_persons():
    cur.execute(
        "SELECT * FROM persons;"
    )
    result = cur.fetchall()
    print(result)

get_all_persons()
conn.commit()
cur.close()

conn.close()

print("Подключение установлено")
