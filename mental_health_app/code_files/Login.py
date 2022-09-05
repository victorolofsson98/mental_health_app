from tkinter import *
from tkinter import messagebox
import MainMenu
from tkcalendar import *


def create_account(mydb):
    window = Tk()
    window.geometry("1000x600+50+50")
    window.title("Window Title")
    window.config(background="#806C70")

    frame = Frame(window, bg="gray", pady=10)

    # title.
    title = Label(frame, text="Creating An Account", font=("Arial", 30),
                  pady=10, padx=200, fg="blue", bg="gray")

    # labels and entries.
    first_name_label, last_name_label, date_of_birth_label = create_labels(frame)
    first_name, last_name, date_of_birth = create_entries(frame)

    # button.
    submit_button = create_submit_button(frame, window, first_name, last_name, date_of_birth, mydb)

    title.grid(row=0, column=0, columnspan=3)

    first_name_label.grid(row=1, column=0, pady=10, sticky="w")
    first_name.grid(row=1, column=1, columnspan=2)

    last_name_label.grid(row=2, column=0, pady=10, sticky="w")
    last_name.grid(row=2, column=1, columnspan=2)

    date_of_birth_label.grid(row=3, column=0, pady=10, sticky="w")
    date_of_birth.grid(row=3, column=1, columnspan=2)

    submit_button.grid(row=4, column=1, pady=5, padx=40)

    frame.pack()

    window.mainloop()


def create_labels(frame):
    first_name_label = Label(frame, text="Enter first name", font=("Arial", 20), fg="black", bg="gray")
    last_name_label = Label(frame, text="Enter last name", font=("Arial", 20), fg="black", bg="gray")
    date_of_birth_label = Label(frame, text="Enter date of birth(yyyy-mm-dd)", font=("Arial", 20), fg="black",
                                bg="gray")

    return first_name_label, last_name_label, date_of_birth_label


def create_entries(frame):
    first_name = Entry(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white", bd=1)
    last_name = Entry(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white", bd=1)
    date_of_birth = DateEntry(frame, selectmode='day', date_pattern='y-mm-dd')

    return first_name, last_name, date_of_birth


def create_submit_button(frame, window, first_name, last_name, date_of_birth, mydb):
    submit_button = Button(frame,
                           text="Create An Account",
                           font=("Arial", 15), borderwidth=3, pady=5,
                           command=lambda: onclick(window, first_name, last_name, date_of_birth, mydb))

    return submit_button


def onclick(window, first_name, last_name, date_of_birth, mydb):
    """inserts data in the database"""
    my_cursor = mydb.cursor()

    first_name = first_name.get()
    last_name = last_name.get()
    date_of_birth = date_of_birth.get()

    try:
        sql_command = "INSERT INTO USERS(first_name, last_name, date_of_birth) VALUES(%s, %s, %s);"
        variables = (first_name, last_name, date_of_birth)

        my_cursor.execute(sql_command, variables)
        mydb.commit()
    except Exception as e:
        print(e)
        messagebox.showerror(title="Error Message", message="Please enter valid input")
    else:
        window.destroy()
        MainMenu.main_menu(mydb)
