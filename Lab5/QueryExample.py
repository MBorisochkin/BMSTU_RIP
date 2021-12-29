from dotenv import load_dotenv

import os
import MySQLdb

load_dotenv()  # Загрузка из .env файла

# Подключение БД
db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd=os.getenv('DBPASS'),
    db="pizzapasta"
)

c = db.cursor()

# Вставка значения
c.execute("INSERT INTO pizza (name, topping, diameter) VALUES (%s, %s, %s);", ('Пицца с мандаринами',
                                                                               'Пицца, мандарины', '23'))
db.commit()

# Вывод таблицы
c.execute("SELECT * FROM pizza")
records = c.fetchall()
for record in records:
    print(record)

# Удаление всех строк таблицы
c.execute("TRUNCATE TABLE pizza")
db.commit()

c.close()
db.close()
