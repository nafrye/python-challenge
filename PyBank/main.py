#import packages
import os
import csv

#define file with data
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#lists to store data
date = []
profit_or_loss = []

#read data from file
with open(budget_data_csv) as csvfile:
     csvreader = csv.reader(csvfile, delimiter= ",")
     for row in csvreader:
         date.append(row[0])
         profit_or_loss.append(row[1])

#count number of items in profit_or_loss, subtracting one to get rid of column header
num_profit_losss = len(profit_or_loss) -1

#count number of months, subtracting one to get rid of column header
num_months = str(len(date)-1)

#initialize total profit or loss at 0; add to that for each item in profit_or_loss list other than the first one
total_profit_or_loss = 0
for items in profit_or_loss[1:]:
     total_profit_or_loss = total_profit_or_loss + int(items)

#create list for change in profit or loss from previous day
change_profit_loss = []
for i in range(2, len(profit_or_loss)):
     change_profit_loss.append(int(profit_or_loss[i]) - int(profit_or_loss[i-1]))

average_change = sum(change_profit_loss)/len(change_profit_loss)

#find the row of the greatest profit and loss change; note this needs to have two added for the label of the row and because the difference score starts on the next row (Feb - Jan is first)
which_row_max = change_profit_loss.index(max(change_profit_loss)) + 2
which_row_min = change_profit_loss.index(min(change_profit_loss)) +2

#message to print to screen and write to file:
msg= ("Financial analysis" + 
      "\n" +
      "total months: " + num_months +
      "\n" +
      "Total profits and losses: $" + str(total_profit_or_loss) + 
      "\n" +
      "Average change: $" + str(round(average_change, 2)) +
      "\n" +
      "Greatest increase in profit: " + (str(date[which_row_max])) + " : ($" + (str(max(change_profit_loss))) + ")" +
      "\n" +
      "Greatst decrease in profit: " + (str(date[which_row_min])) + " : ($" + (str(min(change_profit_loss))) + ")")

print(msg)

#write output to file
budget_analysis = os.path.join("analysis", "budget_analysis.txt")
with open(budget_analysis, 'w') as f:
     f.write(msg)
