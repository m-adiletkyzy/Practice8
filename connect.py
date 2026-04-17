import psycopg2

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="1234",   # тот пароль, с которым ты зашла
    host="localhost",
    port="5432"
)

cur = conn.cursor()

print("Connected successfully!")
