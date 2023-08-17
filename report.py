import os
from datetime import datetime, timedelta


class Report:
    """
    A class to generate reports.
    """

    @staticmethod
    def borrowing(student, title):
        """
        Generate a borrowing report.
        :param student: the borrower
        :param title: the title where one book is lent by the borrower
        :return: None
        """
        # Save the current date
        borrow_time = datetime.now()
        # Calculate the due date, 14 days from today
        due = borrow_time + timedelta(days=14)
        # Format of the dates to printed out
        date_format = "%d %B %Y"

        # Clear the console and make an empty screen
        os.system("clear")

        print("Borrowing Report")
        print("*****Borrower Information*****")
        print("Borrower ID: " + str(student.id))
        print("Borrower Name:" + student.name)

        print()
        print("*****Book Information*****")
        print("Book Name: " + title.name)
        print("Publisher: " + title.publisher)
        print("Genre: " + title.genre)

        print()
        print("*****Others*****")
        print("Date Loaned: " + borrow_time.strftime(date_format))
        print("Due Date: " + due.strftime(date_format))
