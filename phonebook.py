import psycopg2
import csv   

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# ➤ INSERT
def insert_contact(name, phone):
    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Contact added")

# ➤ SELECT
def get_contacts():
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# ➤ UPDATE
def update_contact(name, new_phone):
    cur.execute(
        "UPDATE contacts SET phone=%s WHERE name=%s",
        (new_phone, name)
    )
    conn.commit()
    print("Updated")

# ➤ DELETE
def delete_contact(name):
    cur.execute(
        "DELETE FROM contacts WHERE name=%s",
        (name,)
    )
    conn.commit()
    print("Deleted")
def import_csv():
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()
    print("CSV imported")
# ➤ TEST MENU
while True:
    print("\n1. Add")
    print("2. Show")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    print("6. Import CSV")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        insert_contact(name, phone)

    elif choice == "2":
        get_contacts()

    elif choice == "3":
        name = input("Name: ")
        phone = input("New phone: ")
        update_contact(name, phone)

    elif choice == "4":
        name = input("Name: ")
        delete_contact(name)
    elif choice == "6":
        import_csv()
    elif choice == "5":
        break

def import_csv():
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()
    print("CSV imported")
