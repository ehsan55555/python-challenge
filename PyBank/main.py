# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources','budget_data.csv')

# Open the CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Skip the first row since we won't include header row ("Date" and "Profit/Loss") in calculation 
    next(csvreader)
    
    # Initializing variables
    months = 0
    net_profit_loss = 0
    total_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    # Sets empty string to store the corresponding month of the greatest increase and decrease in profits
    greatest_increase_month = ""
    greatest_decrease_month = ""
    # Stores previous month's profit/loss
    previous_profit_loss = 0

    # Start Loop
    for row in csvreader:
        # Count total number of months
        months += 1
        # Adds profit/loss value from each row in column 2
        net_profit_loss += int(row[1])            
       
        # Start conditional statements
        # This conditional statement checks if the current row is not the first row. The purpose of this is to skip the first row since it typically contains headers and not actual data
        if months > 1:
            # Subtracts the previous row's profit/loss value (stored in previous_profit_loss) from the current row's profit/loss value
            change = int(row[1]) - previous_profit_loss
            # Adds the change value to the total_change variable, which keeps track of the cumulative change in profit/loss over all the rows
            total_change += change

            # Checks if the current change value is greater than the greatest_increase value, which initially starts at 0
            if change > greatest_increase:
                # If it's greater, the greatest_increase and greatest_increase_month variables are updated with the current change value and the corresponding month from row[0] (column 1)
                greatest_increase = change
                greatest_increase_month = row[0]

            # Checks if the current change value is less than the greatest_decrease value, which initially starts at 0
            if change < greatest_decrease:
                # If it's less than, the greatest_decrease and greatest_decrease_month variables are updated with the current change value and the corresponding month from row[0] (column 1)
                greatest_decrease = change
                greatest_decrease_month = row[0]
        
        # Loop ends

        # Variable is updated with the profit/loss value from the current row in column 2, serving as the previous value for the next iteration
        previous_profit_loss = int(row[1])
   
    # Calculates average change by dividing the total_change by the number of months and skipping the first row, since it's a header
    # Even though the header is skipped, the variable, 'months' still counts it as a row, so we need to subtract 1 from months to get an accurate average change
    average_change = total_change / (months - 1)

    # Print the financial analysis results to the terminal
    
    print("Financial Analysis")
    print("----------------------------")
    # Displays total number of months over the entire period
    print(f"Total Months: {months}")
    # Displays total profit/loss over the entire period
    print(f"Total: ${net_profit_loss}")
    # Displays average of profit/loss changes over the entire period
    # Format specifier ':.2f' used to display the average change with two decimal places.
    print(f"Average Change: ${average_change:.2f}")
    # Displays the month and corresponding amount of the greatest increase in profits
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    # Displays the month and corresponding amount of the greatest decrease in profits
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

    # Save the analysis results to a text file
    output_file = "financial_analysis.txt"

    # Export the financial analysis results to a text file
    # Opens file in write mode and referred to as 'txtfile'    
    with open(output_file, "w") as txtfile:
        
       # Whenever '/n' is used, it instructs the program to move over to the next line after that point

        # Write the financial analysis results to the terminal
        txtfile.write("Financial Analysis\n") 
        txtfile.write("----------------------------\n")
        txtfile.write(f"Total Months: {months}\n")
        txtfile.write(f"Total: ${net_profit_loss}\n")
        txtfile.write(f"Average Change: ${average_change:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
        txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
