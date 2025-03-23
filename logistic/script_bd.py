import sqlite3
from datetime import datetime

# Подключение к базе данных (файл базы данных будет создан, если его нет)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Создание таблицы Cargo, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS cargo_cargo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    weight DECIMAL(10, 2) NOT NULL,
    length DECIMAL(10, 2) NOT NULL,
    width DECIMAL(10, 2) NOT NULL,
    height DECIMAL(10, 2) NOT NULL,
    departure_point TEXT NOT NULL,
    destination_point TEXT NOT NULL,
    departure_date DATETIME NOT NULL,
    arrival_date DATETIME NOT NULL,
    company TEXT NOT NULL
)
''')

# Данные для заполнения таблицы
cargo_data = [
    (500.50, 2.5, 1.8, 1.2, "Москва", "Санкт-Петербург", "2023-10-01 08:00:00", "2023-10-02 18:00:00", 'ООО "Ромашка"'),
    (750.75, 3.0, 2.0, 1.5, "Екатеринбург", "Новосибирск", "2023-10-03 09:00:00", "2023-10-04 19:00:00", 'ИП "Иванов"'),
    (1000.00, 4.0, 2.5, 2.0, "Казань", "Уфа", "2023-10-05 10:00:00", "2023-10-06 20:00:00", 'ЗАО "ТехноПро"'),
    (300.25, 1.5, 1.0, 0.8, "Краснодар", "Ростов-на-Дону", "2023-10-07 07:00:00", "2023-10-08 17:00:00", 'ООО "Грузовичок"'),
    (900.90, 3.5, 2.2, 1.8, "Владивосток", "Хабаровск", "2023-10-09 11:00:00", "2023-10-10 21:00:00", 'АО "СтройМир"'),
]

# Вставка данных в таблицу
cursor.executemany('''
INSERT INTO cargo_cargo (
    weight, length, width, height,
    departure_point, destination_point,
    departure_date, arrival_date, company
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', cargo_data)

# Сохранение изменений
conn.commit()

# Закрытие соединения с базой данных
conn.close()

print("Таблица cargo_cargo успешно заполнена данными!")