def calculate_average_sleep(mydb):
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT round(avg(amount_sleep), 3) FROM daily_questions;")

    average_sleep = ""
    for row in my_cursor:
        average_sleep = row[0]

    return average_sleep


def calculate_nutrition_score(mydb):
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT round(avg(nutrition_score)) FROM daily_questions;")

    average_sleep = ""
    for row in my_cursor:
        average_sleep = row[0]

    return average_sleep


def calculate_average_exercise(mydb):
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT  round(avg(amount_exercise))  FROM daily_questions;")

    average_sleep = ""
    for row in my_cursor:
        average_sleep = row[0]

    return average_sleep



def calculate_average_social_activity(mydb):
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT round(avg(amount_social_activity))  FROM daily_questions;")

    average_sleep = ""
    for row in my_cursor:
        average_sleep = row[0]

    return average_sleep


def calculate_happiness_score(mydb):
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT round(avg(happiness_score)) FROM daily_questions;")

    average_sleep = ""
    for row in my_cursor:
        average_sleep = row[0]

    return average_sleep
