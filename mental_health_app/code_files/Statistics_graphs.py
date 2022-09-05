import matplotlib.pyplot as plt


def create_sleep_amount_graph(mydb):
    dates = []
    values = []

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT amount_sleep FROM daily_questions;")
    for row in my_cursor:
        float_val = row[0]
        values.append(float_val)

    my_cursor.execute("SELECT for_date FROM daily_questions;")
    for row in my_cursor:
        str_val = row[0]
        dates.append(str_val)

    plt.figure(figsize=(7, 4))
    plt.bar(dates, values)

    plt.suptitle('Sleeping hours overview')
    plt.show()


def create_nutrition_graph(mydb):
    dates = []
    values = []

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT nutrition_score FROM daily_questions;")
    for row in my_cursor:
        float_val = row[0]
        values.append(float_val)

    my_cursor.execute("SELECT for_date FROM daily_questions;")
    for row in my_cursor:
        str_val = row[0]
        dates.append(str_val)

    plt.figure(figsize=(7, 4))
    plt.bar(dates, values)

    plt.suptitle('Nutrition score overview')
    plt.show()


def create_exercise_graph(mydb):
    dates = []
    values = []

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT amount_exercise FROM daily_questions;")
    for row in my_cursor:
        float_val = row[0]
        values.append(float_val)

    my_cursor.execute("SELECT for_date FROM daily_questions;")
    for row in my_cursor:
        str_val = row[0]
        dates.append(str_val)

    plt.figure(figsize=(7, 4))
    plt.bar(dates, values)

    plt.suptitle('Exercise score overview')
    plt.show()


def create_social_activity_graph(mydb):
    dates = []
    values = []

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT amount_social_activity FROM daily_questions;")
    for row in my_cursor:
        float_val = row[0]
        values.append(float_val)

    my_cursor.execute("SELECT for_date FROM daily_questions;")
    for row in my_cursor:
        str_val = row[0]
        dates.append(str_val)

    plt.figure(figsize=(7, 4))
    plt.bar(dates, values)

    plt.suptitle('Social activity overview')
    plt.show()


def create_happiness_graph(mydb):
    dates = []
    values = []

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT happiness_score FROM daily_questions;")
    for row in my_cursor:
        float_val = row[0]
        values.append(float_val)

    my_cursor.execute("SELECT for_date FROM daily_questions;")
    for row in my_cursor:
        str_val = row[0]
        dates.append(str_val)

    plt.figure(figsize=(7, 4))
    plt.bar(dates, values)

    plt.suptitle('Happiness score overview')
    plt.show()
