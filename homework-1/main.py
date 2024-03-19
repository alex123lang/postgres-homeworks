import csv
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="north",
    user="postgres",
    password="********",
    host="localhost",
)
cur = conn.cursor()


# Функция для вставки данных из CSV в таблицу
def insert_data_from_csv(table_name, csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            insert_query = "INSERT INTO {} VALUES ({})".format(
                table_name,
                ', '.join(['%s'] * len(row))
            )
            cur.execute(insert_query, row)
            conn.commit()


# Путь к CSV-файлам
employees_csv = 'north_data/employees_data.csv'
customers_csv = 'north_data/customers_data.csv'
orders_csv = 'north_data/orders_data.csv'

# Заполнение таблиц данными из CSV
insert_data_from_csv('employees', employees_csv)
insert_data_from_csv('customers', customers_csv)
insert_data_from_csv('orders', orders_csv)

# Закрытие соединения с базой данных
cur.close()
conn.close()


