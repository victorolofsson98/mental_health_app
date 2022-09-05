
from tkinter import messagebox
import Login


def onclick(window, mydb):
    my_cursor = mydb.cursor()

    confirmation_msg = messagebox.askokcancel(title="Confirmation message",
                                              message="Are you sure you want to delete your account?")

    if confirmation_msg:

        try:
            sql_command = "delete from users;"
            my_cursor.execute(sql_command)
            mydb.commit()

        except Exception as e:
            print(e)
            messagebox.showerror(title="Error Message", message="Something went wrong")
            # Message_box.message_box("Error Message", "Something went wrong")
        else:
            window.destroy()
            Login.create_account(mydb)

    else:
        return
