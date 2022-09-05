from tkinter import *
import MainMenu


def feedback_view(mydb):
    window = Tk()
    window.geometry("1000x600+50+50")
    window.title("Feedback")
    window.config(background="#806C70")
    
    frame = Frame(window, bg="gray", pady=10)

    # title
    title = Label(frame, text="Feedback", font=("Arial", 30),
                  pady=10, padx=200, fg="blue", bg="gray")
    title.grid(row=0, column=0, columnspan=3)

    #labels and entries
    feedback_rating_label = Label(
        frame, text='\tPlease rate your experience from 1 - 10.', font=("Arial", 18), fg="black", bg="gray")
    feedback_rating_entry = Scale(frame, font=(
        "Arial", 15), borderwidth=3, fg="black", bg="white", orient=HORIZONTAL, from_=1, to=10)

    feedback_label = Label(frame, text="Would you like to\n further elaborate? (Optional)", font=(
        "Arial", 18), fg="black", bg="gray")
    feedback_entry = Text(frame, font=("Arial", 18),width=30, height=8, borderwidth=5, fg="black", bg="white")

    # Grid
    feedback_rating_label.grid(row=1, column=0, pady=10)
    feedback_rating_entry.grid(row=1, column=1, pady=10)

    feedback_label.grid(row=4, column=0, pady=10)
    feedback_entry.grid(row=6, column=0, pady=10)

    submit_button = Button(frame, text="Submit", font=("Arial", 15), borderwidth=3, pady=5,
                           command=lambda: return_to_main_menu(window, mydb))

    return_button = Button(frame, text="Return to main menu", font=("Arial", 15), borderwidth=3, pady=5,
                           command=lambda: return_to_main_menu(window, mydb))

    return_button.grid(row=30, column=0, pady=5)
    submit_button.grid(row=10, column=0, pady=5)

    frame.pack()

    window.mainloop()


def return_to_main_menu(window, mydb):
    window.destroy()
    MainMenu.main_menu(mydb)
