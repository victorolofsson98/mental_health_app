from tkinter import *
import Profile
import DeleteAccount
import Articles
import DailyQuestions
import Statistics
import snake_main
import Feedback


def main_menu(mydb):
    window = Tk()
    window.geometry("1000x600+50+50")
    window.title("Main menu")
    window.config(background="#806C70")

    frame = Frame(window, bg="gray")

    # title
    label1 = Label(frame, text="Main Menu", font=("Arial", 30), pady=10, padx=200, fg="blue", bg="gray")

    # menu buttons
    button1 = Button(frame, text="Daily questions", font=("Arial", 20), width=15, height=5,
                     command=lambda: daily_questions_onclick(window, mydb))

    button2 = Button(frame, text="Statistics", font=("Arial", 20), width=15, height=5,
                     command=lambda: statistics_onclick(window, mydb))

    button3 = Button(frame, text="Are you bored?\n Play a game", font=("Arial", 20), width=15, height=5,
                     command=lambda: game_onclick())

    button4 = Button(frame, text="Profile", font=("Arial", 20), width=15, height=5,
                     command=lambda: profile_onclick(window, mydb))

    button5 = Button(frame, text="Helpful Articles", font=("Arial", 20), width=15, height=5,
                     command=lambda: helpful_articles_onclick(window, mydb))

    button6 = Button(frame, text="Delete Account", font=("Arial", 20), width=15, height=5,
                     command=lambda: DeleteAccount.onclick(window, mydb))

    button7 = Button(frame, text="Feedback", font=("Arial", 20), width=15, height=5,
                     command=lambda: feedback_page(window, mydb))

    label1.grid(row=0, column=0, columnspan=3)
    button1.grid(row=1, column=0)
    button2.grid(row=1, column=1)
    button3.grid(row=1, column=2)
    button4.grid(row=2, column=0)
    button5.grid(row=2, column=1)
    button6.grid(row=2, column=2)
    button7.grid(row=3, column=0)

    frame.pack()

    window.mainloop()


def daily_questions_onclick(window, mydb):
    window.destroy()
    DailyQuestions.daily_questions(mydb)


def statistics_onclick(window, mydb):
    window.destroy()
    Statistics.view(mydb)


def profile_onclick(window, mydb):
    window.destroy()
    Profile.view(mydb)


def helpful_articles_onclick(window, mydb):
    window.destroy()
    Articles.view(mydb)


def game_onclick():
    snake_main.main()



def feedback_page(window, mydb):
    window.destroy()
    Feedback.feedback_view(mydb)

