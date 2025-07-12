Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def main():
...     total_rainfall = 0.0
...     total_months = 0
...     years = int(input("Enter the number of years: "))
...     for year in range(1, years + 1):
...         print(f"\nYear {year}")
...         for month in range(1, 13):
...             rainfall = float(input(f" Enter rainfall for month {month} (in inches): "))
...             total_rainfall += rainfall
...             total_months += 1
...     average_rainfall = total_rainfall / total_months
...     print("\nRainfall Report")
...     print(f"Total months: {total_months}")
...     print(f"Total raindall: {total_rainfall:.2f} inches")
...     print(f"Average rainfall per month: {average_rainfall:.2f} inches")
... 
...     
>>> main()
Enter the number of years: 1

Year 1
 Enter rainfall for month 1 (in inches): 90
 Enter rainfall for month 2 (in inches): 1
 Enter rainfall for month 3 (in inches): 50
 Enter rainfall for month 4 (in inches): 67
 Enter rainfall for month 5 (in inches): 72
 Enter rainfall for month 6 (in inches): 99
 Enter rainfall for month 7 (in inches): 34
 Enter rainfall for month 8 (in inches): 21
 Enter rainfall for month 9 (in inches): 10
 Enter rainfall for month 10 (in inches): 14
 Enter rainfall for month 11 (in inches): 71
 Enter rainfall for month 12 (in inches): 89

Rainfall Report
Total months: 12
Total raindall: 618.00 inches
Average rainfall per month: 51.50 inches
