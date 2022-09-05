from tkinter import *
import Calculations
from code_files import MainMenu
import Statistics_graphs
from tkinter import messagebox

def view(mydb):
    window = Tk()
    window.geometry("1000x600+50+50")
    window.title("Statistics")
    window.config(background="#806C70")

    frame = Frame(window, bg="gray", pady=10)

    # title
    title = Label(frame, text="Statistics", font=("Arial", 30), pady=10, padx=200, fg="blue", bg="gray")

    # labels, entries and graph buttons.
    average_sleep_label = Label(frame, text="Average amount of sleep", font=("Arial", 20), fg="black", bg="gray")
    average_sleep_entry = create_sleep_entry(frame, mydb)
    average_sleep_graphButton = Button(frame, text="show graph", font=("Arial", 10), borderwidth=3,
                                       command=lambda : open_sleep_graph(mydb))

    nutrition_score_label = Label(frame, text="Nutrition score", font=("Arial", 20), fg="black", bg="gray")
    nutrition_score_entry = create_nutrition_score_entry(frame, mydb)
    nutrition_graphButton = Button(frame, text="show graph", font=("Arial", 10), borderwidth=3,
                                   command=lambda: open_nutrition_score_graph(mydb))


    average_exercise_label = Label(frame, text="Average amount of exercise", font=("Arial", 20), fg="black", bg="gray")
    average_exercise_entry = create_exercise_entry(frame, mydb)
    average_exercise_graphButton = Button(frame, text="show graph", font=("Arial", 10), borderwidth=3,
                                          command=lambda: open_exercise_graph(mydb))


    average_social_activity_label = Label(frame, text="Average social activity per day", font=("Arial", 20),
                                          fg="black", bg="gray")
    average_social_activity_entry = create_average_social_activity_entry(frame, mydb)
    average_social_activity_graphButton = Button(frame, text="show graph", font=("Arial", 10), borderwidth=3,
                                                 command=lambda: open_average_social_activity_graph(mydb))


    happiness_score_label = Label(frame, text="Happiness score", font=("Arial", 20), fg="black", bg="gray")
    happiness_score_entry = create_happiness_score_entry(frame, mydb)
    happiness_score_graphButton = Button(frame, text="show graph", font=("Arial", 10), borderwidth=3,
                                         command=lambda: open_happiness_score_activity_graph(mydb))

    # return button
    return_button = Button(frame, text="Return to main menu", font=("Arial", 15), borderwidth=3, pady=5,
                           command=lambda: return_to_main_menu(window, mydb))

    title.grid(row=0, column=0, columnspan=3)

    average_sleep_label.grid(row=1, column=0, pady=10, sticky="w")
    average_sleep_entry.grid(row=1, column=1, columnspan=2)
    average_sleep_graphButton.grid(row=1, column=2, sticky="e")

    nutrition_score_label.grid(row=2, column=0, pady=10, sticky="w")
    nutrition_score_entry.grid(row=2, column=1, columnspan=2)
    nutrition_graphButton.grid(row=2, column=2, sticky="e")

    average_exercise_label.grid(row=3, column=0, pady=10, sticky="w")
    average_exercise_entry.grid(row=3, column=1, columnspan=2)
    average_exercise_graphButton.grid(row=3, column=2, sticky="e")

    average_social_activity_label.grid(row=4, column=0, pady=10, sticky="w")
    average_social_activity_entry.grid(row=4, column=1, columnspan=2)
    average_social_activity_graphButton.grid(row=4, column=2, sticky="e")

    happiness_score_label.grid(row=5, column=0, pady=10, sticky="w")
    happiness_score_entry.grid(row=5, column=1, columnspan=2)
    happiness_score_graphButton.grid(row=5, column=2, sticky="e")

    return_button.grid(row=6, column=0, columnspan=3)

    frame.pack()
    window.mainloop()


def create_sleep_entry(frame, mydb):
    average_sleep_entry = Entry(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white", bd=1)
    average_sleep = Calculations.calculate_average_sleep(mydb)
    if average_sleep is None:
        average_sleep = " "
    average_sleep_entry.insert(0, average_sleep)
    average_sleep_entry.config(state='readonly')

    return average_sleep_entry


def create_nutrition_score_entry(frame, mydb):
    nutrition_score_entry = Entry(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white")
    nutrition_score = Calculations.calculate_nutrition_score(mydb)
    if nutrition_score is None:
        nutrition_score = " "
    nutrition_score_entry.insert(0, nutrition_score)
    nutrition_score_entry.config(state='readonly')

    return nutrition_score_entry


def create_exercise_entry(frame, mydb):
    average_exercise_entry = Entry(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white")
    average_exercise = Calculations.calculate_average_exercise(mydb)
    if average_exercise is None:
        average_exercise = " "
    average_exercise_entry.insert(0, average_exercise)
    average_exercise_entry.config(state='readonly')

    return average_exercise_entry


def create_average_social_activity_entry(frame, mydb):
    average_social_activity_entry = Entry(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white")
    average_activity = Calculations.calculate_average_social_activity(mydb)
    if average_activity is None:
        average_activity = " "
    average_social_activity_entry.insert(0, average_activity)
    average_social_activity_entry.config(state='readonly')

    return average_social_activity_entry


def create_happiness_score_entry(frame, mydb):
    happiness_score_entry = Entry(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white")
    happiness_score = Calculations.calculate_happiness_score(mydb)
    if happiness_score is None:
        happiness_score = " "
    happiness_score_entry.insert(0, happiness_score)
    happiness_score_entry.config(state='readonly')

    return happiness_score_entry


#
def open_sleep_graph(mydb):
    minimum_number_reached = check_number_of_rows(mydb)

    if minimum_number_reached:
        Statistics_graphs.create_sleep_amount_graph(mydb)


def open_nutrition_score_graph(mydb):
    minimum_number_reached = check_number_of_rows(mydb)

    if minimum_number_reached:
        Statistics_graphs.create_nutrition_graph(mydb)


def open_exercise_graph(mydb):
    minimum_number_reached = check_number_of_rows(mydb)

    if minimum_number_reached:
        Statistics_graphs.create_exercise_graph(mydb)


def open_average_social_activity_graph(mydb):
    minimum_number_reached = check_number_of_rows(mydb)

    if minimum_number_reached:
        Statistics_graphs.create_social_activity_graph(mydb)


def open_happiness_score_activity_graph(mydb):
    minimum_number_reached = check_number_of_rows(mydb)

    if minimum_number_reached:
        Statistics_graphs.create_happiness_graph(mydb)


def return_to_main_menu(window, mydb):
    window.destroy()
    MainMenu.main_menu(mydb)


def check_number_of_rows(mydb):

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT count(*) FROM daily_questions;")

    number_of_rows = 0
    for row in my_cursor:
        number_of_rows = row[0]

    if number_of_rows < 3:
        messagebox.showerror(title="Error Message",
                             message="There must be at-least 3 days of registered data before the graph can be shown")
        return False
    else:
        return True