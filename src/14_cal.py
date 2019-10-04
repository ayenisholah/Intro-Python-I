"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""


import sys
import calendar
import datetime
month = input('Enter a numeric representation of month (M): ')
try:
    value_month = int(month)
    if value_month:
        year = input('Enter a year')
        try:
            year_value = int(year)
            print(datetime.datetime(year_value, value_month, 7).strftime("%B - %Y"))
        except ValueError:
            print(datetime.datetime(2017, value_month, 7).strftime("%B"))
except ValueError:
    print(datetime.datetime.today().strftime("%B"))
