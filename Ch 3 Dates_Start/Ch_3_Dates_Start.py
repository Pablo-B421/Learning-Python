from datetime import date
from datetime import time
from datetime import datetime

def main():
	#today = date.today()
	#print(" Today's date is ", today)

	#print("Date components:", today.day, today.month, today.year)

	#print("Today's weekday number is", today.weekday())
	#days=["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun" ]
	#print ("Whish is a:", days[today.weekday()])
	today = datetime.now()
	print("The current date and time is", today)

	t= datetime.time(datetime.now())
	print(t)






if __name__ == "__main__":
	main()