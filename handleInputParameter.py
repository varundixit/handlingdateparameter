from datetime import date, timedelta
import datetime 
import sys

def handleInput():
	dataTypeExcecption = 0 

	if len(sys.argv) >= 3:
		dataFetchDate = sys.argv[1]
		daysToFetch = sys.argv[2]

	if len(sys.argv) == 2:
		dataFetchDate = sys.argv[1]
		daysToFetch = 1
		print("defaulting Count of Days to 1")

	if len(sys.argv) == 1:
		dataFetchDate = (date.today()-timedelta(days=1)).strftime("%Y-%m-%d")
		daysToFetch = 1
		print("defaulting run date to Yesterday and Count of Days to 1")

	try:
		dateFetchStartFrom = datetime.datetime.strptime(dataFetchDate, '%Y-%m-%d')
		print("date parameter Ok")
	except ValueError:
		print("Oops! That was not valid date format. Date formet expected is yyyy-mm-dd")
		dataTypeExcecption = 1 
		dataFetchDate=date.today() - timedelta(days=1)

	try:
		daysToFetchInt=int(daysToFetch)
		print("Count of days parameters Ok")
	except ValueError:
		print("Oops!  That was no valid number.")
		dataTypeExcecption = 1	
		daysToFetch = 1

	if dataTypeExcecption == 1 :
		print("Data type exception encountered, the expected format of the input strings are as follows: $ python filename.py {yyyy-mm-dd} {2}. default values for date is yesterday and count of days to run is 1")
		print("Current values that are defaulted to run are the following Date: {} and Run for Days : {}. if you want to continue please enter 1 else 0".format(dataFetchDate,daysToFetch))
		try:
			chooseDefaultOptions = int(input("Continue with the default options : "))
		except ValueError:
			print("Oops! That was not a valid number. Try running the program again...")
			raise SystemExit
		if chooseDefaultOptions!=1:
			raise SystemExit
	return dataFetchDate,daysToFetch

dataFetchDate,daysToFetch = handleInput()
#print("dataFetchDate:",dataFetchDate)
#print("daysToFetch:",daysToFetch)
#print ("Continue world!!!")