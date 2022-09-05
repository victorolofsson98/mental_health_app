import mysql.connector

import MainMenu
import Login


def main():
    # database setup.
    mydb = data_base_connection()
    my_cursor = mydb.cursor()

    user_exists = check_if_user_exists(my_cursor)

    # if there is no registered user,
    # this will call a function to create a user. else this will call the main menu.
    if user_exists == 0:
        Login.create_account(mydb)
    else:
        MainMenu.main_menu(mydb)


def data_base_connection():
    """creating a connection to the database."""
    url = "localhost"
    databaseName = "mental_health_app"
    userName = "mental_health_admin"
    password = "mental_health123"

    mydb = mysql.connector.connect(
        host=url,
        database=databaseName,
        user=userName,
        passwd=password,
    )

    return mydb

def check_if_user_exists(my_cursor):
    """checks if there is a registered user"""
    user_exists = 0

    my_cursor.execute("SELECT first_name from users;")
    rows = my_cursor.fetchall()

    if len(rows) != 0:
        user_exists = 1

    return user_exists


if __name__ == '__main__':
    main()
