import LACDA_Core_Function_FINAL as LACDA
import LACDA_Hour_Analysis as Hour

def main():
	date1 = input("Report's start date: ")

	date2 = input("Report's end date: ")

	month = input("Report's month: ")

	string = input("Name of the insights xlsx file: ")

	lacda = LACDA.LACDA_Core(date1, date2, month, string)
	#lacda.export_docx()
	hour = Hour.Hour_Analysis(lacda)
	List = hour.Interval()
	#print(List['35']['like'])
	print(hour.norm_prob_less(30000, List['35']['like']))
	#print(hour.mean(hour.mergesort(List['35']['like'])))
	#print(hour.mean(List['35']['like']))

main()