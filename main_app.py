from tkinter import *
from tkcalendar import *

def showCalendar(year=[],month=[]):
    """
    Show the calendar view for a particular year and month
    :param year: Year of calendar
    :param month: Month of calendar
    :return: Calendar view
    """
    label.config(text=cal.get_date())


if __name__ == "__main__":
    root = Tk()
    root.geometry("1600x900")

    cal = Calendar(root, selectmode="day", year=2020, month=5, day=22)
    cal.pack(fill=BOTH, expand=1)

    button = Button(root, text="Get Date", command=showCalendar)
    button.pack(pady=20)

    label = Label(root, text="")
    label.pack(pady=20)

    root.mainloop()