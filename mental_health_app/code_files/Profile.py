from tkinter import *
from tkinter import messagebox
from code_files import MainMenu
from tkcalendar import *

def view(mydb):
    window = Tk()
    window.geometry("1000x600+50+50")
    window.title("Window Title")
    window.config(background="#806C70")

    first_name = ""
    last_name = ""
    date_of_birth = ""

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT first_name, last_name, date_of_birth from users;")

    for row in my_cursor:
        first_name = row[0]
        last_name = row[1]
        date_of_birth = row[2]

    frame = Frame(window, bg="gray", pady=10)

    title = Label(frame, text="Profile", font=("Arial", 30), pady=10, padx=200, fg="blue", bg="gray")

    first_name_label = Label(frame, text="First name", font=("Arial", 20),fg="black", bg="gray")
    first_name_entry = Entry(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white", bd=1)
    first_name_entry.insert(0, first_name)
    first_name_entry.config(state='readonly')

    last_name_label = Label(frame, text="Last name", font=("Arial", 20), fg="black", bg="gray")
    last_name_entry = Entry(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white")
    last_name_entry.insert(0, last_name)
    last_name_entry.config(state='readonly')

    date_of_birth_label = Label(frame, text="Enter date of birth(yyyy-mm-dd)",
                                font=("Arial", 20), fg="black", bg="gray")
    date_of_birth_entry = DateEntry(frame, selectmode='day', date_pattern='y-mm-dd')
    date_of_birth_entry.insert(0, date_of_birth)
    date_of_birth_entry.config(state='readonly')

    return_button = Button(frame, text="Return to main menu", font=("Arial", 15), borderwidth=3, pady=5,
                           command= lambda: return_to_main_menu(window, mydb))

    submit = Button(frame,
                    text="Submit",
                    font=("Arial", 15), borderwidth=3, pady=5, state='disabled',
                    command= lambda: onclick(window, first_name_entry, last_name_entry,
                                             date_of_birth_entry, mydb))

    edit_button = Button(frame,
                    text="Edit",
                    font=("Arial", 15), borderwidth=3, pady=5,
                    command= lambda: edit_button_onclick(window, first_name_entry,
                                                         last_name_entry, date_of_birth_entry, submit ))

    title.grid(row=0, column=0, columnspan=3)
    return_button.grid(row=5, column=0, columnspan=3 )

    first_name_label.grid(row=1, column=0, pady=10, sticky="w")
    first_name_entry.grid(row=1, column=1, columnspan=2)

    last_name_label.grid(row=2, column=0, pady=10, sticky="w")
    last_name_entry.grid(row=2, column=1, columnspan=2)

    date_of_birth_label.grid(row=3, column=0, pady=10, sticky="w")
    date_of_birth_entry.grid(row=3, column=1, columnspan=2)

    edit_button.grid(row=4, column=0, pady=15)

    submit.grid(row=4, column=1, pady=15)


    frame.pack()

    window.mainloop()


def return_to_main_menu(window, mydb):
    window.destroy()
    MainMenu.main_menu(mydb)


def edit_button_onclick (window, first_name_entry, last_name_entry, date_of_birth_entry, submit):

    if first_name_entry["state"] == "readonly":
        first_name_entry.config(state='normal')
        last_name_entry.config(state='normal')
        date_of_birth_entry.config(state='normal')

        submit.config(state='normal')


def onclick(window, first_name_entry, last_name_entry, date_of_birth_entry, mydb):
    userID = 0
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT userID from users limit 1;")

    for row in my_cursor:
        userID= row[0]

    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    date_of_birth = date_of_birth_entry.get()


    try:
        sql_command="UPDATE users SET first_name = %s, last_name = %s, date_of_birth = %s WHERE userID = %s;"
        variables=(first_name, last_name, date_of_birth, userID)

        my_cursor.execute(sql_command, variables)
        mydb.commit()
    except Exception as e:
        print(e)
        messagebox.showerror(title="Error Message", message="Please enter valid input")

    else:
        messagebox.showinfo(title="Confirmation", message="Profile was changed successfully")
        # Message_box.message_box("Confirmation", "Profile was changed successfully")
