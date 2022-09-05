import tkinter
from tkinter import *
import MainMenu
import mysql.connector.errors
from datetime import date
from tkinter import messagebox

# today date
todays_date = date.today()


def daily_questions(mydb):
    """Daily question frame"""

    window = Tk()
    window.geometry("1000x600+50+50")
    window.title("Window Title")
    window.config(background="#806C70")

    frame = Frame(window, bg="gray", pady=10)

    # title
    title = Label(frame, text="Daily Questions", font=("Arial", 30), pady=10, padx=200, fg="blue", bg="gray")

    # labels
    date_label, sleep_label, nutrition_label, exercise_label, social_activity_label, happiness_score_label \
        = create_labels(frame)

    # entries
    date_entry, sleep_entry, nutrition_entry, exercise_entry, social_activity_entry, happiness_score_entry = \
        create_entries(frame)

    return_button = Button(frame, text="Return to main menu", font=("Arial", 15), borderwidth=3, pady=5,
                           command=lambda: return_to_main_menu(window, mydb))

    submit = Button(frame,
                    text="Submit",
                    font=("Arial", 15), borderwidth=3, pady=5,
                    command=lambda: onclick(window, date_entry, sleep_entry, nutrition_entry, exercise_entry,
                                            social_activity_entry, happiness_score_entry, mydb))

    title.grid(row=0, column=0, columnspan=3)

    date_label.grid(row=1, column=0, pady=10, sticky="w")
    date_entry.grid(row=1, column=1, columnspan=2)

    sleep_label.grid(row=2, column=0, pady=10, sticky="w")
    sleep_entry.grid(row=2, column=1, columnspan=2)

    nutrition_label.grid(row=3, column=0, pady=10, sticky="w")
    nutrition_entry.grid(row=3, column=1, columnspan=2)

    exercise_label.grid(row=4, column=0, pady=10, sticky="w")
    exercise_entry.grid(row=4, column=1, columnspan=2)

    social_activity_label.grid(row=5, column=0, pady=10, sticky="w")
    social_activity_entry.grid(row=5, column=1, columnspan=2)

    happiness_score_label.grid(row=6, column=0, pady=10, sticky="w")
    happiness_score_entry.grid(row=6, column=1, columnspan=2)

    submit.grid(row=10, column=0, pady=15, columnspan=3)
    return_button.grid(row=11, column=0, columnspan=3)

    frame.pack()
    window.mainloop()


def create_labels(frame):
    """Function to create the labels for the input variables"""
    date_label = Label(frame, text="Enter date(yyyy-mm-dd)", font=("Arial", 20), fg="black", bg="gray")
    sleep_label = Label(frame, text="Amount of sleep(hh.mm)", font=("Arial", 20), fg="black", bg="gray")
    nutrition_label = Label(frame, text="How well did you eat(score 1 to 10)", font=("Arial", 20), fg="black",
                            bg="gray")
    exercise_label = Label(frame, text="Amount of exercise(hh.mm)", font=("Arial", 20), fg="black", bg="gray")
    social_activity_label = Label(frame, text="Amount of social activity(hh.mm)", font=("Arial", 20), fg="black",
                                  bg="gray")
    happiness_score_label = Label(frame, text="How did you feel today(score 1 to 10)", font=("Arial", 20), fg="black",
                                  bg="gray")

    return date_label, sleep_label, nutrition_label, exercise_label, social_activity_label, happiness_score_label


def create_entries(frame):
    """Function to set the value of the input variables"""
    how_well_did_you_eat_value = tkinter.IntVar()
    how_did_you_feel_today_value = tkinter.IntVar()
    how_well_did_you_sleep = tkinter.DoubleVar()
    amount_of_exercise = tkinter.DoubleVar()
    social_activity_value = tkinter.DoubleVar()

    # set current date automatically instead of having to input it
    entry_date = StringVar(frame, value=f'{todays_date.year}-{todays_date.month}-{todays_date.day}')

    # Date
    date_entry = Entry(frame, textvariable=entry_date)

    # Sleep
    sleep_entry = Scale(frame, from_=0.00, to=9.00, digits=2, resolution=0.5, orient='horizontal',
                        variable=how_well_did_you_sleep)
    # Eat
    nutrition_entry = Scale(frame, from_=1, to=10, orient='horizontal', variable=how_well_did_you_eat_value)

    # Exercise
    exercise_entry = Scale(frame, from_=0.00, to=9.00, digits=2, resolution=0.5, orient='horizontal',
                           variable=amount_of_exercise)
    # Social
    social_activity_entry = Scale(frame, from_=0.00, to=9.00, digits=2, resolution=0.5, orient='horizontal',
                                  variable=social_activity_value)

    # Feeling
    happiness_score_entry = Scale(frame, from_=1, to=10, orient='horizontal',
                                  variable=how_did_you_feel_today_value)

    return date_entry, sleep_entry, nutrition_entry, exercise_entry, social_activity_entry, happiness_score_entry


def return_to_main_menu(window, mydb):
    """Back to main menu function"""
    window.destroy()
    MainMenu.main_menu(mydb)


def onclick(window, date_entry, sleep_entry, nutrition_entry, exercise_entry, social_activity_entry,
            happiness_score_entry, mydb):
    """Onclick event handler function"""

    my_cursor = mydb.cursor()

    date = date_entry.get()
    userID = get_userID(mydb)
    sleep = sleep_entry.get()
    nutrition = nutrition_entry.get()
    exercise = exercise_entry.get()
    social_activity = social_activity_entry.get()
    happiness_score = happiness_score_entry.get()

    try:
        sql_command = "INSERT INTO daily_questions(for_date, userID, amount_sleep, nutrition_score, amount_exercise, " \
                      "amount_social_activity, happiness_score) VALUES(%s, %s, %s, %s, %s, %s, %s);"
        variables = (date, userID, sleep, nutrition, exercise, social_activity, happiness_score)

        my_cursor.execute(sql_command, variables)
        mydb.commit()
    except mysql.connector.errors.IntegrityError as err:
        print(err)
        messagebox.showerror(title="Error Message",
                             message="Duplicate dates")
        # Message_box.message_box("Error", "Duplicate dates")

    except Exception as e:
        print(e)
        messagebox.showerror(title="Error Message",
                             message="Please enter valid input")
        # Message_box.message_box("Error", "Please enter valid input")
    else:
        messagebox.showinfo(title='Confirmation', message="Data added successfully")
        # Message_box.message_box("confirmation", "Data added successfully")


def get_userID(mydb):
    """Gets the userID from the database"""

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT userID FROM users;")

    userID = ""
    for row in my_cursor:
        userID = row[0]

    return userID
