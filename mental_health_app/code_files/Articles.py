from tkinter import *
import MainMenu


def view(mydb):
    window = Tk()
    window.geometry("1000x600+50+50")
    window.title("Statistics")
    window.config(background="#806C70")

    frame = Frame(window, bg="gray", pady=10)

    # title
    title = Label(frame, text="Helpful Articles", font=("Arial", 30), pady=10, padx=200, fg="blue", bg="gray")

    # labels and entries.
    depression_article_label, loneliness_article_label, anxiety_article_label = create_labels(frame)

    average_sleep_entry = create_depression_article_entry(frame, mydb)
    nutrition_score_entry = create_loneliness_article_entry(frame, mydb)
    average_exercise_entry = create_anxiety_article_entry(frame, mydb)

    # return button
    return_button = Button(frame, text="Return to main menu", font=("Arial", 15), borderwidth=3, pady=5,
                           command=lambda: return_to_main_menu(window, mydb))

    title.grid(row=0, column=0, columnspan=3)

    depression_article_label.grid(row=1, column=0, pady=10, sticky="w")
    average_sleep_entry.grid(row=1, column=1, columnspan=2)

    loneliness_article_label.grid(row=2, column=0, pady=10, sticky="w")
    nutrition_score_entry.grid(row=2, column=1, columnspan=2)

    anxiety_article_label.grid(row=3, column=0, pady=10, sticky="w")
    average_exercise_entry.grid(row=3, column=1, columnspan=2)

    return_button.grid(row=6, column=0, columnspan=3)

    frame.pack()
    window.mainloop()


def create_labels(frame):
    depression_article_label = Label(frame, text="Articles about depression", font=("Arial", 20), fg="black", bg="gray")
    loneliness_article_label = Label(frame, text="Articles about loneliness", font=("Arial", 20), fg="black", bg="gray")
    anxiety_article_label = Label(frame, text="Articles about anxiety", font=("Arial", 20), fg="black", bg="gray")

    return depression_article_label, loneliness_article_label, anxiety_article_label


def create_depression_article_entry(frame, mydb):
    average_sleep_entry = Text(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white", bd=1, width=20,
                               height=5)

    average_sleep = get_depression_article(mydb)
    if average_sleep is None:
        average_sleep = " "
    average_sleep_entry.insert(1.0, average_sleep)
    average_sleep_entry.config(state='disabled')

    return average_sleep_entry


def create_loneliness_article_entry(frame, mydb):
    nutrition_score_entry = Text(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white", bd=1, width=20,
                                 height=5)
    nutrition_score = get_loneliness_article(mydb)
    if nutrition_score is None:
        nutrition_score = " "
    nutrition_score_entry.insert(1.0, nutrition_score)
    nutrition_score_entry.config(state='disabled')

    return nutrition_score_entry


def create_anxiety_article_entry(frame, mydb):
    average_exercise_entry = Text(frame, font=("Arial", 15), borderwidth=3, fg="black", bg="white", bd=1, width=20,
                                  height=5)
    average_exercise = get_anxiety_article(mydb)
    if average_exercise is None:
        average_exercise = " "
    average_exercise_entry.insert(1.0, average_exercise)
    average_exercise_entry.config(state='disabled')

    return average_exercise_entry


def get_depression_article(mydb):
    my_cursor = mydb.cursor()
    my_cursor.execute("select articleLink from articles where articleType = 'depression';")

    depression_articles = ''
    for row in my_cursor:
        depression_articles = row

    return depression_articles


def get_loneliness_article(mydb):
    my_cursor = mydb.cursor()
    my_cursor.execute("select articleLink from articles where articleType = 'loneliness';")

    average_sleep = ""
    for row in my_cursor:
        average_sleep = row[0]

    return average_sleep


def get_anxiety_article(mydb):
    my_cursor = mydb.cursor()
    my_cursor.execute("select articleLink from articles where articleType = 'anxiety';")

    average_sleep = ""
    for row in my_cursor:
        average_sleep = row[0]

    return average_sleep


def return_to_main_menu(window, mydb):
    window.destroy()
    MainMenu.main_menu(mydb)
