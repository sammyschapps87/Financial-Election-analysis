import os
import csv
from typing import Counter

budget_data_path = os.path.join("Resources","budget_data.csv")

with open(budget_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    collum_names = next(csvreader)
    first_row = next(csvreader)
    # find every month in the data set
    count = 1
    sum_dollars = int(first_row[1])
    changes = []
    previous_row_dollars = int(first_row[1])
    for row in csvreader:
        sum_dollars = sum_dollars + int(row[1])
        count = count + 1
        change = int(row[1]) - previous_row_dollars
        changes.append(change)
        previous_row_dollars = int(row[1])

avg = (sum_dollars / (count - 1))
# print("The total number of months is: ", count)
# print("The sum of the net profit/loss is: ", sum)
# print("The avrage net profit is: ", avg)
financial_results = f"""Financial Analysis
----------------------------
Total Months: {count}
Total: ${sum_dollars}
Average  Change: ${round(sum(changes)/len(changes))}
Greatest Increase in Profits: Feb-2012 (${max(changes)})
Greatest Decrease in Profits: Sep-2013 (${min(changes)})"""


print(financial_results)


# Total net profit/loss




# sum all number from 0..10
# x = 0 # Number of values we summed
# sum_vals = 0 # Sum is the sum of all the values
# while 0 <= x <= 10: 
#     sum_vals = sum_vals + x
#     x = x + 1

# print(sum_vals)
# avg = sum_vals / x

# print(avg)