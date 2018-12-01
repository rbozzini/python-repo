# Python program to display calendar of given month of the year
import calendar

yy = int(input("Anno -> "))
mm = int(input("Mese -> "))

print(calendar.month(yy, mm))